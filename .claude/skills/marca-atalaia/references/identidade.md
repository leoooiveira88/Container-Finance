# Identidade visual da Atalaia — referência técnica

## Símbolo em SVG, para colar inline

Colar inline (e não `<img src>`) permite que a versão monocromática herde `currentColor` e funcione nos
dois temas.

```html
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Atalaia">
  <path fill="currentColor" fill-rule="evenodd"
    d="M13 24 H31 A7 7 0 0 1 38 31 V49 A7 7 0 0 1 31 56 H13
       A7 7 0 0 1 6 49 V31 A7 7 0 0 1 13 24 Z
       M14 50 L20 50 L30 30 L24 30 Z"/>
  <g fill="none" stroke="#F2893D" stroke-width="5" stroke-linecap="round">
    <path d="M30 17 A13 13 0 0 1 40 29"/>
    <path d="M33 9 A22 22 0 0 1 49 28"/>
  </g>
</svg>
```

Troque o `stroke` dos arcos conforme o fundo: `#F2893D` no escuro, `#B4560E` no claro.

**Versão reduzida** (abaixo de 32 px): mesmo `path` do bloco, com `viewBox="6 24 32 32"` e **sem o grupo
dos arcos**.

**Ícone de app e favicon**: não é o símbolo em fundo transparente — num navegador de tema escuro ele
desapareceria. É ladrilho cheio, com a fenda clara:

```html
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect width="64" height="64" rx="14" fill="#1B1E24"/>
  <path fill="#EDEAE4" d="M16 52 L28 52 L48 12 L36 12 Z"/>
</svg>
```

## Escala tipográfica

| Nível | Tamanho / entrelinha | Peso | Família | Uso |
|---|---|---|---|---|
| Display | 48 / 1.05 | 700 | Spectral | nome, capas |
| H1 | 32 / 1.15 | 700 | Spectral | título de página |
| H2 | 24 / 1.2 | 600 | Plex Sans | seção |
| Corpo | 16 / 1.55 | 400 | Plex Sans | texto corrido |
| Apoio | 13 / 1.4 | 500 | Plex Sans | legenda, origem do dado |
| Dado | 17 / 1.2 | 500 | Plex Mono | número em coluna — sempre `tabular-nums` |
| Micro | 11 / 1.3 | 700 | Plex Sans | tag e overline, caixa alta, `letter-spacing:.11em` |

## Formas

- **Raio:** 6 px em componentes, 3 px em chips e tags. Deriva do raio do símbolo (7 de 32 unidades).
- **Espaçamento:** base 8 px. Escala 4, 8, 12, 16, 24, 32, 48, 64 — nada fora dela.
- **Elevação:** uma só, `0 1px 3px rgba(22,24,28,.12)`. Hierarquia se faz com borda e fundo, não sombra.
- **Imagem:** a Atalaia quase não usa foto. A ilustração da marca é o próprio dado — gráfico, linha do
  tempo, tabela.

## Mínimos e proteção

- Área de proteção: 8 unidades do viewBox 64×64 (um quarto da altura do bloco).
- Tamanho mínimo: completo 32 px / 12 mm; reduzido 16 px / 6 mm.
- Centro óptico: (25, 36). Em contêiner quadrado ou redondo, `transform="translate(7, -4)"`.

## Proporção de cor

Cerca de 60% neutro, 30% azul, 10% acento. O acento é raro por definição: é o que faz "aja aqui"
continuar significando alguma coisa.
