#!/usr/bin/env python3
"""Gera os arquivos finais da marca a partir dos SVGs: PNGs em tamanho exato e favicon.ico.

Uso:
    python3 gerar_arquivos.py --svg icone-app.svg --tamanhos 512 180 48 32 16 --ico
    python3 gerar_arquivos.py --svg simbolo.svg --tamanhos 512 128 --cor "#1B1E24" --saida png/

Por que existe: exportar SVG para PNG parece trivial e nao e. Este script encapsula tres
armadilhas que custam tempo toda vez:

1. O headless deste ambiente tem PISO DE LARGURA de ~500px e DESCONTA ~87px de altura da
   janela. Pedir --window-size=64,64 devolve uma imagem cortada. A solucao e renderizar numa
   janela folgada e recortar o canto superior esquerdo no tamanho exato.
2. Remover width/height do SVG para ele preencher a pagina precisa ser feito SO na tag <svg>
   de abertura. Um replace ingenuo tambem apaga o width/height de <rect>, e o fundo do icone
   some sem erro nenhum.
3. Favicon com o simbolo em fundo transparente desaparece em aba de tema escuro. O icone de
   app deve ser LADRILHO CHEIO: fundo solido com a forma vazada em cor clara.

Precisa do Pillow para recortar e montar o .ico:  pip install pillow
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

PISO_LARGURA = 500   # largura minima da janela no headless
DESCONTO_ALTURA = 87  # altura de cromo descontada da janela

CANDIDATOS = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/google-chrome",
]


def achar_navegador():
    for c in CANDIDATOS:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    for nome in ("chromium", "chrome", "google-chrome", "google-chrome-stable"):
        achado = shutil.which(nome)
        if achado:
            return achado
    raiz = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    if os.path.isdir(raiz):
        for base, _, arquivos in os.walk(raiz):
            for arquivo in arquivos:
                if arquivo in ("chrome", "headless_shell"):
                    caminho = os.path.join(base, arquivo)
                    if os.access(caminho, os.X_OK):
                        return caminho
    return None


def renderizar(navegador, svg_path, destino, tamanho, cor):
    svg = open(svg_path, encoding="utf-8").read()
    # so a tag <svg> de abertura perde width/height — ver armadilha 2 no cabecalho
    svg = re.sub(r'(<svg\b[^>]*?)\s+width="[^"]*"\s+height="[^"]*"', r"\1", svg, count=1)
    html = (f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;padding:0}}'
            f'svg{{display:block;width:{tamanho}px;height:{tamanho}px;color:{cor}}}</style>{svg}')

    tmp_html = destino + ".tmp.html"
    bruto = destino + ".bruto.png"
    open(tmp_html, "w", encoding="utf-8").write(html)
    perfil = tempfile.mkdtemp(prefix="marca-")
    janela_l = max(PISO_LARGURA, tamanho + 40)
    janela_a = tamanho + DESCONTO_ALTURA + 40
    subprocess.run([
        navegador, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        f"--user-data-dir={perfil}", f"--window-size={janela_l},{janela_a}",
        f"--screenshot={bruto}", "--force-device-scale-factor=1",
        "--default-background-color=00000000", "file://" + os.path.abspath(tmp_html),
    ], capture_output=True, text=True)
    shutil.rmtree(perfil, ignore_errors=True)
    os.remove(tmp_html)

    from PIL import Image
    imagem = Image.open(bruto).convert("RGBA").crop((0, 0, tamanho, tamanho))
    imagem.save(destino)
    os.remove(bruto)
    return imagem


def main():
    parser = argparse.ArgumentParser(description="Gera PNGs e favicon.ico a partir de um SVG.")
    parser.add_argument("--svg", required=True, help="arquivo SVG de origem")
    parser.add_argument("--tamanhos", type=int, nargs="+", required=True,
                        help="tamanhos em px, ex.: 512 180 48 32 16")
    parser.add_argument("--cor", default="#1B1E24",
                        help="valor de currentColor para SVGs monocromaticos")
    parser.add_argument("--saida", default=".", help="pasta de destino")
    parser.add_argument("--prefixo", default=None, help="prefixo dos arquivos (padrao: nome do SVG)")
    parser.add_argument("--ico", action="store_true",
                        help="monta favicon.ico multi-resolucao com 16, 32 e 48")
    args = parser.parse_args()

    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        print("erro: este script precisa do Pillow.  pip install pillow", file=sys.stderr)
        return 1

    navegador = achar_navegador()
    if not navegador:
        print("erro: nenhum Chromium/Chrome encontrado.", file=sys.stderr)
        return 1
    if not os.path.isfile(args.svg):
        print(f"erro: SVG nao encontrado: {args.svg}", file=sys.stderr)
        return 1

    os.makedirs(args.saida, exist_ok=True)
    prefixo = args.prefixo or os.path.splitext(os.path.basename(args.svg))[0]
    geradas = {}
    for tamanho in args.tamanhos:
        destino = os.path.join(args.saida, f"{prefixo}-{tamanho}.png")
        geradas[tamanho] = renderizar(navegador, args.svg, destino, tamanho, args.cor)
        print(f"ok  {destino}  ({tamanho}x{tamanho})")

    if args.ico:
        faltando = [t for t in (16, 32, 48) if t not in geradas]
        if faltando:
            print(f"aviso: --ico pede os tamanhos 16, 32 e 48; faltaram {faltando}. "
                  f"O .ico foi montado com o que havia.", file=sys.stderr)
        maior = geradas[max(geradas)]
        alvo = os.path.join(args.saida, "favicon.ico")
        tamanhos_ico = [(t, t) for t in (16, 32, 48) if t in geradas] or [(32, 32)]
        maior.save(alvo, format="ICO", sizes=tamanhos_ico)
        print(f"ok  {alvo}  ({', '.join(str(t[0]) for t in tamanhos_ico)})")

    print("\nLembre: o icone de app nao e o simbolo em fundo transparente — use ladrilho cheio,\n"
          "ou ele some em aba de navegador com tema escuro.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
