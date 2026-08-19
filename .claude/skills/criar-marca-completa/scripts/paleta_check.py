#!/usr/bin/env python3
"""Matriz de contraste WCAG para a paleta da marca.

Uso:
    python3 paleta_check.py "#752F8A" "#FFCE01" "#1A1A1A" "#FFFFFF"
    python3 paleta_check.py --rotulos "Primaria=#752F8A" "Acento=#FFCE01" "Texto=#1A1A1A"

Por que existe: uma paleta bonita que reprova em contraste vira uma marca ilegivel em
etiqueta, tela de celular no sol e impressao barata -- e o erro so aparece depois de pronto.
Rode antes de fechar a paleta, nao depois.

Referencia: WCAG 2.1 -- 4.5:1 para texto corrido, 3:1 para texto grande (>=24px ou >=19px
em negrito) e para elementos graficos funcionais (bordas, icones de acao).
"""

import sys

AA_TEXTO = 4.5
AA_GRANDE = 3.0


def hex_para_rgb(valor):
    v = valor.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise ValueError(f"cor invalida: {valor!r} (use #RGB ou #RRGGBB)")
    try:
        return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError(f"cor invalida: {valor!r}")


def luminancia(rgb):
    canais = []
    for c in rgb:
        s = c / 255.0
        canais.append(s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4)
    r, g, b = canais
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = luminancia(hex_para_rgb(a)), luminancia(hex_para_rgb(b))
    claro, escuro = max(la, lb), min(la, lb)
    return (claro + 0.05) / (escuro + 0.05)


def veredito(razao):
    if razao >= 7:
        return "AAA  texto e grafico"
    if razao >= AA_TEXTO:
        return "AA   texto e grafico"
    if razao >= AA_GRANDE:
        return "AA   so texto grande / grafico"
    return "REPROVA"


def main(argv):
    args = [a for a in argv if a != "--rotulos"]
    if not args:
        print(__doc__)
        return 2

    cores = []
    for item in args:
        if "=" in item:
            rotulo, valor = item.split("=", 1)
        else:
            rotulo, valor = item, item
        hex_para_rgb(valor)  # valida cedo, com mensagem clara
        cores.append((rotulo.strip(), valor.strip()))

    largura = max(len(r) for r, _ in cores)
    print(f"\nMatriz de contraste WCAG ({len(cores)} cores)\n")

    reprovados = []
    for i, (ra, va) in enumerate(cores):
        for rb, vb in cores[i + 1:]:
            razao = contraste(va, vb)
            estado = veredito(razao)
            print(f"  {ra:<{largura}}  x  {rb:<{largura}}   {razao:5.2f}:1   {estado}")
            if razao < AA_GRANDE:
                reprovados.append((ra, rb, razao))

    print()
    if reprovados:
        print("Pares que nao servem para nenhuma sobreposicao de texto ou elemento funcional:")
        for ra, rb, razao in reprovados:
            print(f"  - {ra} sobre {rb} ({razao:.2f}:1) -- use so como fundo x fundo, nunca com texto")
        print("\nRegistre isso no manual em vez de deixar alguem descobrir na producao.")
    else:
        print("Nenhum par abaixo de 3:1. Ainda assim, so use como texto corrido os pares com AA (4.5:1+).")
    print()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ValueError as erro:
        print(f"erro: {erro}", file=sys.stderr)
        sys.exit(1)
