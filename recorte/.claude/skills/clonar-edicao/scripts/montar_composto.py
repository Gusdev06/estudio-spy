#!/usr/bin/env python3
"""Remonta a edicao de um criativo de referencia usando um talking head novo.

Reaproveita as faixas de baixo do original (screen recording, b-roll, barra de
caption) e troca so a faixa do sujeito.

  python3 montar_composto.py --ref original.mp4 --avatar novo.mp4 \
      --topo 279 --corte-ref 8.66 --corte 8.04 -o final.mp4

  # so ver as contas, sem renderizar
  python3 montar_composto.py --ref ... --avatar ... --topo 279 --dry-run

--topo e --corte-ref saem do analisar_estrutura.py. --corte e o instante no
video NOVO onde a parte dividida termina; deixe igual a --corte-ref se os dois
tem o mesmo ritmo, ou aponte para a emenda de clipe mais proxima.
"""
import argparse
import json
import subprocess
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("precisa de numpy: python3 -m pip install numpy")


def probe(caminho):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height:format=duration", "-of", "json", caminho],
        capture_output=True, text=True).stdout
    d = json.loads(out)
    return (int(d["streams"][0]["width"]), int(d["streams"][0]["height"]),
            float(d["format"]["duration"]))


def topo_da_cabeca(caminho, w, h, t=2.0):
    """Primeira linha com conteudo de sujeito, vindo de cima.

    Fundo de parede e liso (desvio horizontal baixo); cabelo e rosto tem
    textura. O salto de desvio marca onde o sujeito comeca -- e disso sai o
    quanto de ar sobra acima dele quando cortamos a faixa.
    """
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(t), "-i", caminho, "-vframes", "1",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    if len(p.stdout) < w * h * 3:
        return None
    img = np.frombuffer(p.stdout[:w * h * 3], dtype=np.uint8).reshape(h, w, 3).astype(np.float32)
    sd = img.mean(axis=2).std(axis=1)
    fundo = float(np.median(sd[:max(4, h // 20)]))
    lim = max(fundo * 2.5, fundo + 12)
    # Sujeito colado no topo (quadro cortado na testa) nao tem transicao
    # fundo->sujeito: a primeira linha ja e ele. Isso e 0, nao 'nao achei'.
    if sd[0] > lim:
        return 0
    for y in range(h):
        if sd[y] > lim and sd[y:y + max(4, h // 100)].min() > lim * 0.7:
            return y
    return None


def par(n):
    n = int(round(n))
    return n - (n % 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", required=True, help="criativo de referencia")
    ap.add_argument("--avatar", required=True, help="talking head novo")
    ap.add_argument("-o", "--saida", default="composto.mp4")
    ap.add_argument("--topo", type=int, required=True,
                    help="y onde termina a faixa do sujeito NA REFERENCIA (do analisar_estrutura)")
    ap.add_argument("--corte-ref", type=float, required=True, help="fim da parte dividida na referencia")
    ap.add_argument("--corte", type=float, help="fim da parte dividida no video novo (default: igual a --corte-ref)")
    ap.add_argument("--largura", type=int, default=1080, help="largura de saida (default 1080)")
    ap.add_argument("--escala", type=float, default=None,
                    help="escala do avatar dentro da faixa (default 0.70 — acerte olhando o --preview)")
    ap.add_argument("--headroom", type=float, default=0.08,
                    help="ar acima da cabeca, como fracao da faixa (default 0.08)")
    ap.add_argument("--sem-blur", action="store_true", help="preencher a lateral com preto em vez de desfoque")
    ap.add_argument("--crf", type=int, default=20)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--preview", metavar="JPG",
                    help="renderiza UM frame comparando referencia x composto e sai. "
                         "Use para acertar --escala antes de gastar minutos no video inteiro.")
    args = ap.parse_args()

    rw, rh, rdur = probe(args.ref)
    aw, ah, adur = probe(args.avatar)
    corte = args.corte if args.corte is not None else args.corte_ref

    W = par(args.largura)
    H = par(W * rh / rw)
    k = W / rw
    top_h = par(args.topo * k)
    bot_h = H - top_h
    bot_src_h = rh - args.topo

    # Escala do avatar. A referencia enquadra o sujeito de um jeito; colar o
    # avatar em escala 1 quase sempre deixa a cabeca grande demais, porque o
    # talking head novo foi gerado em quadro cheio e a faixa e mais baixa que
    # o quadro. Casamos a PROPORCAO que a cabeca ocupa na faixa.
    cab_ref = topo_da_cabeca(args.ref, rw, rh, min(2.0, rdur / 3))
    cab_av = topo_da_cabeca(args.avatar, aw, ah, min(2.0, adur / 3))

    # Escala nao e calculavel de forma confiavel sem medir o TAMANHO DA CABECA,
    # e "topo da cabeca ate o fim do quadro" nao e isso -- o quadro do avatar
    # desce ate o colo, o da referencia nao. Entao: 0.70 e um ponto de partida
    # que funcionou na pratica, e o jeito certo de acertar e olhar o --preview.
    escala = args.escala if args.escala is not None else 0.70
    origem = "informada" if args.escala is not None else "padrao — confira com --preview"

    sw, sh = par(aw * escala), par(ah * escala)
    x = par((W - sw) / 2)
    headroom = int(top_h * args.headroom)
    y = int(headroom - (cab_av or 0) * escala)

    print(f"referencia : {rw}x{rh}  {rdur:.2f}s   corte {args.corte_ref:.2f}s")
    print(f"avatar     : {aw}x{ah}  {adur:.2f}s   corte {corte:.2f}s")
    print(f"saida      : {W}x{H}   faixa topo {top_h}px + faixa baixo {bot_h}px")
    print(f"cabeca     : ref y={cab_ref}  avatar y={cab_av}")
    print(f"escala     : {escala:.3f}  ({origem})")
    print(f"overlay    : {sw}x{sh} em x={x} y={y}  (headroom {headroom}px)")
    if corte > adur:
        print(f"\nERRO: corte {corte}s passa da duracao do avatar ({adur:.2f}s)")
        return 1
    if args.corte_ref > rdur:
        print(f"\nERRO: corte-ref passa da duracao da referencia")
        return 1
    if args.dry_run:
        return 0

    # As duas faixas do trecho dividido precisam ter a MESMA duracao. Se o
    # painel de baixo for mais longo que o avatar, o vstack estica o mais
    # curto congelando o ultimo frame -- o video incha e o audio dessincroniza
    # do corte em diante. A duracao do trecho e a do corte no video NOVO.
    dur_split = corte
    if corte > args.corte_ref + 0.01:
        print(f"\nAVISO: o trecho dividido do novo ({corte:.2f}s) e mais longo que o da"
              f" referencia ({args.corte_ref:.2f}s).\n       O painel de baixo vai entrar na"
              f" parte de tela cheia da referencia. Corte antes, ou escolha outro ponto.")
    t_prev = min(args.corte_ref, corte) * 0.5

    fundo = (f"crop={W}:{top_h}:0:0,scale={W}:{top_h}" if args.sem_blur else
             f"scale={W}:-2,crop={W}:{top_h}:0:{max(0, int((ah*W/aw - top_h)/2))},"
             f"gblur=sigma={max(12, W//27)},eq=brightness=0.03")

    fc = (
        f"[0:v]trim=0:{corte},setpts=PTS-STARTPTS,split=2[bg][fg];"
        f"[bg]{fundo},setsar=1[blur];"
        f"[fg]scale={sw}:{sh}[small];"
        f"[blur][small]overlay={x}:{y},crop={W}:{top_h}:0:0,setsar=1[top1];"
        f"[1:v]trim=0:{dur_split},setpts=PTS-STARTPTS,"
        f"crop={rw}:{bot_src_h}:0:{args.topo},scale={W}:{bot_h}:flags=lanczos,setsar=1[bot1];"
        f"[top1][bot1]vstack=inputs=2[p1];"
        f"[0:v]trim={corte},setpts=PTS-STARTPTS,scale={W}:{H},setsar=1[p2];"
        f"[p1][p2]concat=n=2:v=1:a=0[vout]"
    )

    fc_frame = (
        f"[0:v]split=2[bg][fg];"
        f"[bg]{fundo},setsar=1[blur];"
        f"[fg]scale={sw}:{sh}[small];"
        f"[blur][small]overlay={x}:{y},crop={W}:{top_h}:0:0,setsar=1[top1];"
        f"[1:v]split=2[r1][r2];"
        f"[r1]crop={rw}:{bot_src_h}:0:{args.topo},scale={W}:{bot_h}:flags=lanczos,setsar=1[bot1];"
        f"[top1][bot1]vstack=inputs=2,scale=540:-2[novo];"
        f"[r2]scale=540:-2,setsar=1[velho];"
        f"[velho][novo]hstack=inputs=2[cmp]"
    )

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", args.avatar, "-i", args.ref,
           "-filter_complex", fc, "-map", "[vout]", "-map", "0:a?",
           "-c:v", "libx264", "-preset", "medium", "-crf", str(args.crf),
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
           "-movflags", "+faststart", args.saida]
    if args.preview:
        pv = (f"[0:v]scale={W}:-2,crop={W}:{top_h}:0:0,gblur=sigma=1[fake];" if False else "")
        cmd_pv = ["ffmpeg", "-y", "-loglevel", "error",
                  "-ss", f"{t_prev:.3f}", "-i", args.avatar,
                  "-ss", f"{t_prev:.3f}", "-i", args.ref,
                  "-filter_complex", fc_frame, "-map", "[cmp]", "-vframes", "1",
                  "-q:v", "3", args.preview]
        r = subprocess.run(cmd_pv)
        if r.returncode == 0:
            print(f"preview: {args.preview}  (esquerda = referencia, direita = composto)")
            print("Compare o TAMANHO DA CABECA nos dois. Maior no seu? baixe --escala.")
        return r.returncode

    print("\nrenderizando...")
    r = subprocess.run(cmd)
    if r.returncode != 0:
        return r.returncode

    ow, oh, odur = probe(args.saida)
    print(f"ok: {args.saida}  {ow}x{oh}  {odur:.2f}s")
    if bot_src_h * k > bot_src_h * 1.5:
        print(f"NOTA: a faixa de baixo foi ampliada {W/rw:.1f}x a partir de {rw}px de largura.")
        print("      Vai sair mole. Se conseguir a referencia em resolucao maior, remonte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
