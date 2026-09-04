---
name: criar-marca-completa
description: >-
  Cria uma marca completa do zero para um produto, serviço ou negócio — do briefing ao manual de marca (brand book)
  entregue como página HTML navegável e PDF: naming, posicionamento, público, arquétipo, proposta de valor, paleta de
  cores validada em contraste, tipografia, logo em SVG com variações, tom de voz e kit de aplicações. Use SEMPRE que o
  usuário mencionar criar, desenvolver, renovar ou repensar uma marca, identidade visual, brand book, manual de marca,
  naming, nome para um produto, logo, paleta da marca, tom de voz, rebranding, ou disser coisas como "não sei que cara
  dar pro meu produto", "preciso dar nome pra isso", "quero que pareça profissional", "vou lançar e não tenho nada de
  visual". Use também quando o usuário pedir só uma parte (só o nome, só as cores, só o logo), porque a skill entrega a
  parte pedida sem perder a coerência do conjunto. NÃO use para aplicar uma marca que JÁ existe dentro de um documento
  (deck, planilha, painel) — nesse caso use a skill específica daquela marca.
---

# Criar marca completa

Conduz alguém da ideia crua ("tenho um produto, não tenho marca") até um manual de marca completo e utilizável.

O entregável final é um **brand book em HTML de arquivo único**, publicado como Artifact e exportado em PDF, contendo:
estratégia (posicionamento, público, arquétipo, proposta de valor), naming, sistema visual (logo em SVG, paleta,
tipografia, grid), sistema verbal (tom de voz, mensagens-chave) e aplicações prontas para usar.

## Como pensar sobre este trabalho

Três coisas fazem a diferença entre um manual de marca que é usado e um que morre na pasta de downloads:

**Decisão antes de decoração.** Cor e fonte são consequência, não ponto de partida. Uma marca resolve um problema de
escolha: por que alguém escolheria isto e não a alternativa óbvia? Se você pular direto para a paleta, vai entregar um
moodboard bonito que não sustenta nenhuma decisão futura — e o usuário vai voltar em duas semanas perguntando "posso
usar essa cor no botão de compra?" sem ter como responder sozinho.

**Uma bifurcação, não trinta perguntas.** Ninguém quer preencher formulário de agência. Faça um briefing curto e
enxuto, preencha os buracos com hipóteses declaradas, e apresente **rotas de marca** — direções inteiras e distintas
entre as quais a pessoa escolhe. É muito mais fácil reagir a três caminhos concretos do que responder "qual é a
personalidade da sua marca?" no vazio.

**Regra sem exemplo não é regra.** "Tom de voz: próximo e direto" não ensina ninguém a escrever. "Próximo e direto"
com um par certo/errado ao lado ensina. Todo princípio no manual precisa vir com pelo menos um exemplo concreto do
produto real do usuário — nunca com texto genérico de lorem ipsum.

## Fluxo

Cinco fases com **dois checkpoints** com o usuário (fim da Fase 1 e fim da Fase 2). Fora esses dois momentos, avance
sozinho: interromper a cada micro-decisão cansa e não melhora o resultado.

### Fase 0 — Descoberta silenciosa

Antes de perguntar qualquer coisa, colete o que já existe. Isso encurta o briefing e demonstra atenção.

- Vasculhe o diretório de trabalho por sinais da marca: `index.html`, `README`, planilhas, decks, logos, cores em CSS
  (`--primary`, `:root`), fontes carregadas do Google Fonts, textos de site.
- Se o usuário citar concorrentes, um site, um Instagram ou um nome de mercado, pesquise (WebSearch/WebFetch) para
  entender o território competitivo — o que todo mundo já faz é justamente o que a marca precisa evitar parecer.
- Se já existir uma marca parcial (um nome, uma cor, um logo tosco feito no Canva), trate como **restrição herdada** e
  pergunte no briefing se é para preservar ou substituir. Jogar fora um ativo com que o cliente já se identificou é o
  erro mais caro dessa conversa.

Resuma em 3 linhas o que encontrou antes de seguir. Se não encontrou nada, siga direto — não invente descoberta.

### Fase 1 — Briefing enxuto

Use `AskUserQuestion` em **uma única rodada** com no máximo 4 perguntas, sempre com opções concretas e uma
recomendação marcada. Leia `references/briefing.md` para o roteiro completo, os defaults e como transformar respostas
vagas em decisão.

O núcleo mínimo que você precisa arrancar:

1. **O que é o produto e para quem** — em uma frase, incluindo o momento de uso ("marmita congelada para quem treina e
   não quer cozinhar de domingo a domingo").
2. **Contra quem você compete e o que quer que digam de você** — define o eixo de diferenciação.
3. **Faixa de preço / posicionamento** — popular, intermediário ou premium. Isso muda tudo: tipografia, densidade
   visual, vocabulário, até o nome.
4. **Restrições** — nome já existe? cor obrigatória? canal principal (Instagram, PDV físico, app, marketplace)? o
   canal principal determina qual aplicação precisa ficar impecável.

Se o usuário responder de forma vaga ou disser "faz do seu jeito", **não insista**. Assuma, declare a hipótese em uma
linha ("estou assumindo posicionamento intermediário, canal principal Instagram") e siga. Hipótese declarada é
corrigível; pergunta repetida é irritante.

**Checkpoint 1:** devolva o briefing consolidado em ~8 linhas e pergunte só "está de pé?".

### Fase 2 — Rotas de marca (o checkpoint que importa)

Construa **3 rotas** distintas. Cada rota é uma marca inteira em miniatura, não uma variação de cor. Rotas que só
diferem no tom do azul não são escolha — são enfeite.

Cada rota precisa ser genuinamente diferente em **estratégia**, e por isso divergem em nome, cor e voz. Um jeito
confiável de garantir distância real é derivar cada rota de um arquétipo diferente (ver `references/estrategia.md`):
por exemplo Cuidador vs. Rebelde vs. Sábio — o mesmo produto vira três marcas irreconhecíveis entre si.

Apresente cada rota neste formato compacto, em texto no chat (rápido de ler, rápido de descartar):

```
ROTA A — "Nome"
Ideia central: [uma frase que explica a aposta]
Arquétipo: [nome] · Posicionamento: [premium/intermediário/popular]
Diz ao cliente: "[a frase que a marca sussurra na cabeça de quem compra]"
Visual: [2 cores em hex + a lógica] · [tipografia + por quê]
Voz: [3 adjetivos] — ex.: "[uma frase real de exemplo, do produto do usuário]"
Arrisca: [o custo honesto dessa escolha]
```

O campo **Arrisca** não é modéstia — é o que torna a escolha informada. Toda direção de marca troca alguma coisa por
outra (premium perde volume, divertido perde autoridade), e dizer isso na cara evita o arrependimento na semana 3.

Se for útil ver, monte um comparativo visual de uma página: três colunas com paleta, tipografia aplicada em um título
real e o nome. Publique como Artifact (carregue a skill `artifact-design` antes de escrever qualquer artifact).

**Checkpoint 2:** o usuário escolhe uma rota, ou pede uma mistura ("o nome da A com a cor da C"). Misturar é normal e
saudável — só verifique se a mistura continua coerente com um único arquétipo e diga se não continuar.

### Fase 3 — Construção da rota escolhida

Agora aprofunde. Trabalhe em paralelo e sem pedir aprovação a cada peça — o usuário já escolheu a direção.

| Camada | O que produzir | Referência |
|---|---|---|
| Naming | Nome final, checagem de disponibilidade, tagline, pronúncia/grafia | `references/naming.md` |
| Estratégia | Posicionamento, público, proposta de valor, pilares de mensagem | `references/estrategia.md` |
| Visual | Logo SVG + variações, paleta com papéis definidos, tipografia, grid | `references/identidade-visual.md` |
| Verbal | Tom de voz com pares certo/errado, glossário, mensagens-chave | `references/verbal.md` |
| Aplicações | Kit mínimo priorizado pelo canal principal | `references/aplicacoes.md` |

Quatro verificações obrigatórias antes de montar o manual, porque são os erros que só aparecem depois de
impresso — ou depois de um advogado ligar.

**1. Colisão de mercado, antes de apresentar qualquer nome.** Pesquise cada candidato na web com o setor
junto ("NOME software gestão", "NOME plataforma Brasil") e descarte antes de mostrar. Isso não é
formalidade: em português, quase toda palavra curta e bonita do território de instrumentos e navegação já
tem dono no mercado de TI. Numa rodada real caíram Prumo, Aprumo, Mirante, Compasso, Leme, Sextante,
Lastro, Nônio, Paralaxe e Azimute — e um deles vendia literalmente o mesmo produto. Reporte com o link, e
diga que registro é assunto de profissional de propriedade industrial.

**2. Contraste de toda a paleta**, inclusive a herdada:

```bash
python3 scripts/paleta_check.py "#752F8A" "#FFCE01" "#1A1A1A" "#FFFFFF"
```

Se a marca herda paleta de uma marca-mãe, teste os acentos **nos dois fundos**. Acento institucional
costuma ter sido desenhado para fundo escuro e reprovar sobre branco. Quando acontecer, derive um par
claro/escuro para cada acento e trate como regra fixa do manual — não como observação de acessibilidade.

**3. O símbolo aos 16px, renderizado de verdade — não imaginado.** Se vira mancha, falhou onde mais
aparece: favicon, avatar, canto de slide. Símbolo que precisa de elementos finos ganha duas densidades
oficiais (completo acima de 32px, reduzido abaixo), e a reduzida ainda tem que dizer alguma coisa sozinha,
não virar um retângulo neutro.

**4. Símbolo assimétrico exige regra de alinhamento óptico com valores fixos.** Calcule o centro óptico
pela massa visual, não pela caixa delimitadora, e escreva no manual como `transform="translate(x, y)"`.
Sem número, cada pessoa centraliza de um jeito e a marca fica torta em metade das aplicações.

### Fase 4 — Manual de marca

Monte o brand book a partir de `assets/brandbook-template.html`. É um HTML de arquivo único, autocontido, com
navegação lateral e as seções já estruturadas — preencha os placeholders `{{...}}`, não reescreva do zero.

Duas regras que separam um manual usável de um enfeite:

- **Nada de placeholder sobrevivente.** Todo exemplo é do produto real. Se sobrou "Lorem ipsum" ou "Nome do produto",
  o manual está incompleto.
- **Toda regra vem com o par certo/errado.** É o que permite alguém que não estava nessa conversa aplicar a marca sem
  perguntar nada.

Depois de preencher:

```bash
# valida que não sobrou placeholder e gera o PDF
python3 scripts/build_brandbook.py manual-marca.html --pdf manual-marca.pdf
```

Todo HTML que o usuário vai abrir fora do navegador de artifacts precisa de `<meta charset="utf-8">` na
primeira linha. Sem isso o arquivo abre com acentuação quebrada na máquina dele, e o manual inteiro perde
credibilidade na primeira frase.

Publique o HTML como Artifact (link privado que o usuário compartilha quando quiser) **e** entregue o PDF com
`SendUserFile`. Os dois formatos servem a coisas diferentes: o HTML é a referência viva que se atualiza, o PDF é o que
se manda para o gráfico, para o fornecedor de embalagem e para o freelancer.

### Fase 5 — Colocar para rodar

Um manual só prova valor quando vira algo publicado. Feche entregando 2 ou 3 peças reais e imediatas do canal
principal — o post de anúncio, a bio do Instagram, a etiqueta, a assinatura de e-mail — já com a marca aplicada. Veja
`references/aplicacoes.md` para o kit mínimo por tipo de negócio.

Gere também os arquivos finais, que é o que permite o time trabalhar sem pedir nada:

```bash
python3 scripts/gerar_arquivos.py --svg icone-app.svg --tamanhos 512 180 48 32 16 --ico --saida png/
```

**O ícone de aplicativo não é o símbolo em fundo transparente.** Símbolo escuro vazado some numa aba de
navegador com tema escuro. O ícone é ladrilho cheio: fundo sólido com a forma em cor clara. Entregue os
dois — transparente para documento, ladrilho para favicon e avatar.

Termine com uma lista curta e concreta do que ainda depende de terceiros (registro no INPI, compra da fonte comercial,
registro do domínio) — sem transformar isso em consultoria jurídica: aponte o caminho e diga que é preciso confirmar
com um profissional.

## Quando o pedido é parcial

Se o usuário pedir só um pedaço ("só me dá um nome", "só quero a paleta"), entregue **o pedaço, bem feito** — não
force o processo inteiro. Mas rode a Fase 1 numa versão mínima (2 perguntas), porque nome sem posicionamento é chute,
e paleta sem público é gosto pessoal. Ao final, ofereça uma vez o resto: "tenho o nome; quer que eu feche o manual
com visual e voz?". Uma oferta, sem insistir.

Se a marca **já existe** e o pedido é evolução ("moderniza", "profissionaliza"), o trabalho muda de natureza: o ativo
é o reconhecimento que a marca já tem. Preserve o que o público reconhece (geralmente cor e nome, nessa ordem) e
mexa no resto. Diga isso explicitamente no manual, na seção de rationale — é o que impede alguém de descartar o
patrimônio da marca sem perceber.

## Arquivos desta skill

- `references/briefing.md` — roteiro de entrevista, defaults e como lidar com respostas vagas
- `references/estrategia.md` — arquétipos, posicionamento, proposta de valor, pilares de mensagem
- `references/naming.md` — territórios de naming, testes de validação, checagem de disponibilidade
- `references/identidade-visual.md` — paleta com papéis, tipografia, construção do logo em SVG, grid
- `references/verbal.md` — tom de voz, pares certo/errado, glossário, mensagens-chave
- `references/aplicacoes.md` — kit mínimo de aplicações por tipo de negócio
- `assets/brandbook-template.html` — template do manual (HTML único, com placeholders)
- `scripts/paleta_check.py` — matriz de contraste WCAG da paleta
- `scripts/build_brandbook.py` — valida placeholders e exporta o HTML para PDF
- `scripts/gerar_arquivos.py` — PNGs em tamanho exato e favicon.ico a partir do SVG
