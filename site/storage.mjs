// Storage das gerações: bucket privado no Supabase (interface S3, o mesmo projeto do HookMill). Chave = pedidos/<id>/<caminho em job/>.
// O cliente nunca recebe a chave: o servidor confere o dono e redireciona pra um link assinado que vale 1 hora.
import fs from 'node:fs'; import path from 'node:path';
import { S3Client, PutObjectCommand, GetObjectCommand, ListObjectsV2Command, DeleteObjectsCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const TIPOS = { '.mp4': 'video/mp4', '.mov': 'video/quicktime', '.m4v': 'video/mp4', '.webm': 'video/webm', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.png': 'image/png', '.webp': 'image/webp' };

export function abrirStorage(env, log) {
  if (!env.STORAGE_ENDPOINT || !env.STORAGE_BUCKET || !env.STORAGE_ACCESS_KEY_ID) return null;
  const s3 = new S3Client({ endpoint: env.STORAGE_ENDPOINT, region: env.STORAGE_REGION || 'us-east-1', forcePathStyle: true,
    credentials: { accessKeyId: env.STORAGE_ACCESS_KEY_ID, secretAccessKey: env.STORAGE_SECRET_ACCESS_KEY } });
  const Bucket = env.STORAGE_BUCKET;
  const chave = (id, rel) => `pedidos/${id}/${rel}`;
  return {
    origem: new URL(env.STORAGE_ENDPOINT).origin,
    // sobe com 3 tentativas; devolve true quando o arquivo está no bucket
    async subir(id, rel, arq) {
      const tipo = TIPOS[path.extname(arq).toLowerCase()] || 'application/octet-stream';
      for (let i = 0; i < 3; i++) {
        try { const st = fs.statSync(arq);
          await s3.send(new PutObjectCommand({ Bucket, Key: chave(id, rel), Body: fs.createReadStream(arq), ContentType: tipo, ContentLength: st.size }));
          return true;
        } catch (e) { if (i === 2) log({ erro: 'storage-subir', id, rel, msg: String(e.message || e).slice(0, 300) }); else await new Promise((r) => setTimeout(r, 2000 * (i + 1))); }
      }
      return false;
    },
    url(id, rel, { baixar = false } = {}) {
      const nome = path.basename(rel).replace(/[^\w.\-]/g, '_');
      return getSignedUrl(s3, new GetObjectCommand({ Bucket, Key: chave(id, rel), ...(baixar ? { ResponseContentDisposition: `attachment; filename="${nome}"` } : {}) }), { expiresIn: 3600 });
    },
    async apagar(id) {
      try { let token;
        do { const r = await s3.send(new ListObjectsV2Command({ Bucket, Prefix: `pedidos/${id}/`, ContinuationToken: token }));
          if (r.Contents?.length) await s3.send(new DeleteObjectsCommand({ Bucket, Delete: { Objects: r.Contents.map((o) => ({ Key: o.Key })) } }));
          token = r.IsTruncated ? r.NextContinuationToken : undefined; } while (token);
      } catch (e) { log({ erro: 'storage-apagar', id, msg: String(e.message || e).slice(0, 300) }); }
    },
  };
}
