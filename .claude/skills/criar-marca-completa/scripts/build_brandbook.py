#!/usr/bin/env python3
"""Valida o manual de marca e exporta para PDF/PNG.

Uso:
    python3 build_brandbook.py manual-marca.html --pdf manual-marca.pdf
    python3 build_brandbook.py post.html --png post.png --tamanho 1080x1350
    python3 build_brandbook.py manual-marca.html --so-validar

Duas coisas acontecem aqui, nessa ordem:

1. VALIDACAO -- procura placeholder sobrevivente ({{...}}, "Lorem ipsum", "Nome do produto",
   "#XXXXXX"). Um manual com placeholder e pior do que nenhum manual: quem for aplicar a marca
   perde a confianca no documento inteiro na primeira pagina em que topa com um.
2. EXPORTACAO -- usa o Chromium ja instalado no ambiente, sem dependencia extra de Python.
   O PDF sai do mesmo HTML que voce publica, entao os dois nunca divergem.

Se a validacao falhar, a exportacao nao acontece (a menos que voce passe --forcar).
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

PADROES_SUSPEITOS = [
    (r"\{\{[^}]{1,80}\}\}", "placeholder do template nao preenchido"),
    (r"(?i)lorem ipsum", "texto de preenchimento"),
    (r"(?i)nome do (produto|neg[oó]cio|cliente|marca)\b", "rotulo generico do template"),
    (r"#XXXXXX|#xxxxxx", "cor nao definida"),
    # sem (?i) de proposito: "todo" e "preencher" sao palavras comuns em portugues e
    # gerariam falso positivo em texto legitimo do manual.
    (r"\bTODO\b|\bTBD\b|\bFIXME\b|\bPREENCHER\b|\bXXX\b", "marcacao de pendencia"),
]

CANDIDATOS_CHROMIUM = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]


def achar_chromium():
    for caminho in CANDIDATOS_CHROMIUM:
        if os.path.isfile(caminho) and os.access(caminho, os.X_OK):
            return caminho
    for nome in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        achado = shutil.which(nome)
        if achado:
            return achado
    # ultimo recurso: procurar dentro do diretorio de browsers do playwright
    raiz = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    if os.path.isdir(raiz):
        for base, _, arquivos in os.walk(raiz):
            for arquivo in arquivos:
                if arquivo in ("chrome", "headless_shell"):
                    caminho = os.path.join(base, arquivo)
                    if os.access(caminho, os.X_OK):
                        return caminho
    return None


def validar(caminho_html):
    with open(caminho_html, encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    problemas = []
    for numero, linha in enumerate(linhas, 1):
        for padrao, motivo in PADROES_SUSPEITOS:
            for achado in re.finditer(padrao, linha):
                trecho = linha.strip()
                if len(trecho) > 100:
                    trecho = trecho[:97] + "..."
                problemas.append((numero, achado.group(0), motivo, trecho))
    return problemas


def rodar_chromium(argumentos_extra, url):
    binario = achar_chromium()
    if not binario:
        print("erro: Chromium nao encontrado. Instale um navegador ou exporte o HTML manualmente.",
              file=sys.stderr)
        return 1
    perfil = tempfile.mkdtemp(prefix="brandbook-")
    comando = [
        binario, "--headless", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", f"--user-data-dir={perfil}",
    ] + argumentos_extra + [url]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    shutil.rmtree(perfil, ignore_errors=True)
    if resultado.returncode != 0:
        print(resultado.stderr[-2000:], file=sys.stderr)
    return resultado.returncode


def main():
    parser = argparse.ArgumentParser(description="Valida e exporta o manual de marca.")
    parser.add_argument("html", help="arquivo HTML do manual (ou de uma peca)")
    parser.add_argument("--pdf", help="caminho de saida do PDF")
    parser.add_argument("--png", help="caminho de saida do PNG")
    parser.add_argument("--tamanho", default="1200x1600",
                        help="LARGURAxALTURA em px para o PNG (padrao 1200x1600)")
    parser.add_argument("--so-validar", action="store_true", help="nao exporta, so valida")
    parser.add_argument("--forcar", action="store_true",
                        help="exporta mesmo com placeholder pendente")
    args = parser.parse_args()

    if not os.path.isfile(args.html):
        print(f"erro: arquivo nao encontrado: {args.html}", file=sys.stderr)
        return 1

    problemas = validar(args.html)
    if problemas:
        print(f"\n{len(problemas)} pendencia(s) no HTML:\n")
        for numero, achado, motivo, trecho in problemas[:40]:
            print(f"  linha {numero:>4}: {achado!r} -- {motivo}")
            print(f"              {trecho}")
        if len(problemas) > 40:
            print(f"  ... e mais {len(problemas) - 40}.")
        print("\nTroque cada um por conteudo real do produto antes de entregar.\n")
    else:
        print("Validacao ok: nenhum placeholder sobrevivente.")

    if args.so_validar:
        return 1 if problemas else 0
    if problemas and not args.forcar:
        print("Exportacao cancelada. Corrija as pendencias ou rode de novo com --forcar.",
              file=sys.stderr)
        return 1

    url = "file://" + os.path.abspath(args.html)
    codigo = 0

    if args.pdf:
        codigo |= rodar_chromium(
            [f"--print-to-pdf={os.path.abspath(args.pdf)}", "--no-pdf-header-footer"], url)
        if os.path.isfile(args.pdf):
            print(f"PDF gerado: {args.pdf} ({os.path.getsize(args.pdf) // 1024} KB)")

    if args.png:
        try:
            largura, altura = (int(v) for v in args.tamanho.lower().split("x"))
        except ValueError:
            print(f"erro: --tamanho invalido: {args.tamanho} (use 1080x1350)", file=sys.stderr)
            return 1
        codigo |= rodar_chromium(
            [f"--screenshot={os.path.abspath(args.png)}",
             f"--window-size={largura},{altura}",
             "--force-device-scale-factor=2"], url)
        if os.path.isfile(args.png):
            print(f"PNG gerado: {args.png} ({largura}x{altura} @2x)")

    if not args.pdf and not args.png:
        print("Nada a exportar: passe --pdf e/ou --png.")

    return codigo


if __name__ == "__main__":
    sys.exit(main())
