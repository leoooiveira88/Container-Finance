---
name: marca-atalaia
description: >-
  Aplica a marca ATALAIA — a plataforma de inteligência operacional da Think — em qualquer material:
  tela e componente de produto, deck, e-mail, painel, documento, post interno ou peça de lançamento.
  Traz símbolo em SVG, paleta com o par claro/escuro obrigatório de cada acento, tipografia, tokens CSS,
  tom de voz com pares certo/errado e o vocabulário próprio (os alertas chamam-se "toques"). Use SEMPRE
  que o usuário mencionar Atalaia, TPI, Think Project Intelligence, "a plataforma de inteligência
  operacional", cartão de toque, motor de regras operacional, ou pedir qualquer material visual, texto de
  alerta, tela ou apresentação desse produto — inclusive quando disser só "monta a tela de alertas",
  "escreve o texto do aviso", "faz o post do lançamento" ou "aplica a marca do produto". NÃO use para
  CRIAR uma marca nova do zero (use criar-marca-completa) nem para material institucional da Think sem
  relação com a plataforma (use as skills THINK).
---

# Marca Atalaia

Plataforma de inteligência operacional da Think: lê Qualitor, Think Track, HubSpot, MS Project e as bases
de custo, aplica as regras do negócio e **avisa quando um projeto ou contrato sai do previsto — enquanto
ainda dá para corrigir**.

- **Nome:** Atalaia (artigo feminino: *a* Atalaia). Nunca "Think Atalaia" — o endosso vem pela assinatura
  conjunta, com a marca Think ao lado ou no rodapé.
- **Descritor:** Plataforma de inteligência operacional. Curto, para lockup: *Inteligência operacional*.
- **Tagline:** Ninguém decide no escuro. Só em capa, login e abertura — **nunca na mesma linha do
  descritor**.
- **Arquétipo:** Guardião–Sábio. Firme, atenta, econômica. Fala pouco e só quando tem o que dizer.

## O Princípio do Muro — a doutrina que decide tudo

O nome vem do árabe *aṭ-ṭalā'i'*: as sentinelas avançadas que a tropa mandava à frente para voltar
contando o que vinha. Não é a torre parada que vigia — é quem se adianta e traz a informação. Daí saem
três regras que valem para o texto e para o produto:

1. **Silêncio é falha.** Alerta que devia sair e não saiu é defeito, com a mesma gravidade de um número
   errado. Alerta suprimido fica registrado e auditável.
2. **Tocar transfere a decisão.** A plataforma avisa com clareza suficiente para a decisão ser possível —
   e para aí. Não decide, não executa, não cobra.
3. **O aviso tem que ser ouvível.** Chega a quem pode agir, no canal onde a pessoa está, com a saída
   sugerida junto. Nunca num relatório aberto na sexta.

**O corolário, que é a regra mais importante de todas:** a atalaia fica no muro olhando para fora. Ela não
observa a praça — o alerta é sobre o que vem, para quem pode agir, **nunca sobre quem errou**. Todo texto,
tela ou peça que violar isso está fora da marca, por mais bonito que esteja.

## Cores — e a regra que mais se erra

A paleta é herdada da Think, mas **os acentos institucionais reprovam em contraste sobre fundo claro**.
Por isso cada acento tem duas versões oficiais, e usar a errada para o fundo é o erro mais comum:

| Papel | Fundo escuro | Fundo claro |
|---|---|---|
| Acento (ação, alerta) | Fogo `#F2893D` — 6,70:1 sobre Noite | Fogo Escuro `#B4560E` — 4,91:1 sobre branco |
| Positivo (resolvido) | Lima `#C8D541` — 10,38:1 sobre Noite | Lima Escuro `#5F6B0F` — 5,84:1 sobre branco |

Base: Noite `#1B1E24` · Axon Blue `#193B68` · Synapse `#4A96D2` · Papel `#F4F6F9` · Tinta `#16181C` ·
Crítico `#C4362F`.

**Nunca combine** Fogo ou Lima com branco/Papel, nem Noite com Axon (1,48:1 — só fundo sobre fundo).

O acento significa **"aja aqui"**. Se aparecer em título, ícone decorativo e fundo, deixa de significar e
o alerta perde força. Em qualquer peça, o laranja é a única superfície de ação.

## Símbolo

A fenda de observação: bloco sólido — o muro — cortado por uma abertura diagonal, com o toque saindo por
ela. Os arquivos estão em `assets/`; o SVG completo também está reproduzido em
`references/identidade.md` para colar inline.

**Sistema de duas densidades, obrigatório:**
- **32 px ou mais** → símbolo completo (bloco + arcos): `assets/simbolo-completo.svg`
- **abaixo de 32 px** → só o bloco: `assets/simbolo-reduzido.svg` — e ele continua apontando, porque o
  corte é diagonal. Nunca reduza o completo "só um pouquinho": troque de versão.

**Alinhamento óptico.** O símbolo é assimétrico nos dois eixos, então centralizar pela caixa delimitadora
deixa a marca torta. Centro óptico em **(25, 36)** do viewBox 64×64 — em contêiner quadrado ou redondo
aplique `transform="translate(7, -4)"`, ou use `assets/simbolo-centrado.svg`, que já vem corrigido. Ao
lado da marca Think, alinhe pela base do bloco (`y = 56`), não pelo centro vertical.

**Área de proteção:** 8 unidades do viewBox (um quarto da altura do bloco). **Mínimos:** completo 32 px /
12 mm; reduzido 16 px / 6 mm.

Nunca: encostar o corte nos cantos (vira placa de proibido), trocar a cor dos arcos, girar, espelhar ou
inclinar o conjunto.

## Tipografia

**Spectral** (serifada) no nome, capas e frases de destaque. **IBM Plex Sans** em todo o resto.
**IBM Plex Mono** em todo número que aparece em coluna, tabela ou comparação, sempre com
`font-variant-numeric: tabular-nums` — número que dança de largura destrói a leitura de um painel, e
painel é o que a Atalaia é. Ambas de licença aberta, com acentuação portuguesa completa.

## Tom de voz e vocabulário

Leia `references/voz.md` antes de escrever qualquer alerta, e-mail, post ou microcópia — é lá que estão os
pares certo/errado e o glossário. O essencial:

Os alertas chamam-se **toques**. Em português "dar um toque" já significa avisar de forma direta e gentil:
é a trombeta do muro e a gíria brasileira na mesma palavra, e é o que impede o alerta de soar como
cobrança. Nunca escreva "notificação" ou "alerta do sistema".

## Ao construir tela ou componente

Use os tokens de `assets/tokens.css` e os padrões de `references/componentes.md`, que trazem o cabeçalho
da plataforma e o cartão de toque nos três estados, prontos para colar.

A regra de produto que não se negocia: **cartão sem saída sugerida só existe no estado resolvido.** Em
qualquer outro, alerta sem saída é toque incompleto — é o Princípio do Muro virando interface.

## Ao montar deck

O deck vai na **marca Think** (use a skill `slides-think-html`, BU `think`) e a Atalaia entra como
conteúdo, não como tema — é o modelo de endosso funcionando. Aplique a marca Atalaia por inteiro só em
material do próprio produto: tela, e-mail automático, tela de login, ícone.

## Arquivos desta skill

- `assets/simbolo-completo.svg`, `simbolo-completo-negativo.svg`, `simbolo-completo-mono.svg`,
  `simbolo-reduzido.svg`, `simbolo-centrado.svg`, `icone-app.svg`
- `assets/tokens.css` — variáveis prontas para o repositório do produto
- `references/identidade.md` — SVG inline, escala tipográfica, formas e mínimos
- `references/voz.md` — tom de voz com pares certo/errado, regras de escrita, glossário e mensagens-chave
- `references/componentes.md` — cabeçalho, cartão de toque nos três estados e assinatura de e-mail
