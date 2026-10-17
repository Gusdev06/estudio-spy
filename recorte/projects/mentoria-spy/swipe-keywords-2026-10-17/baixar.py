# Baixa a mídia dos anúncios relevantes da coleta (URLs do fbcdn expiram em horas).
import json, glob, os, re, subprocess, hashlib, unicodedata
HOSTS = ["love-vision.site","tryfidelo.com","spygran.site","raygort.site","igyhall.com","acessosegurosite","deepscanner.app","socialcatfish.com","Lens AI","apps.apple.com"]
def rel(a):
    s = a['link'] + ' ' + a['pagina']
    return any(h in s for h in HOSTS)
slug = lambda s: re.sub(r'[^a-z0-9]+','-', unicodedata.normalize('NFD', s.lower()).encode('ascii','ignore').decode()).strip('-')
vistos, man = {}, []
for f in sorted(glob.glob('coleta/*.json')):
    d = json.load(open(f))
    for a in d['anuncios']:
        if not rel(a) or not a['midia'] or a['id'] in vistos: continue
        host = a['link'].split('/')[2] if a['link'].count('/')>=2 else ''
        ext = 'mp4' if a['formato']=='video' else 'jpg'
        arq = f"anuncios/{slug(host or 'sem-link')}__{slug(a['pagina'])}-{a['id']}.{ext}"
        r = subprocess.run(['curl','-sSfL','-o',arq,a['midia']])
        if r.returncode: print('✗', a['id']); continue
        md5 = hashlib.md5(open(arq,'rb').read()).hexdigest()
        vistos[a['id']] = 1
        man.append({**{k:a[k] for k in ('id','pagina','inicio','versoes','formato','link','copy')}, 'host':host, 'busca':d['busca'], 'arquivo':arq, 'md5':md5})
json.dump(man, open('manifest.json','w'), ensure_ascii=False, indent=1)
print(len(man), 'baixados')
