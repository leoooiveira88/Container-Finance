# Aplicações

O manual prova valor quando vira coisa publicada. Feche sempre entregando peças reais — não mockups genéricos com
sombra bonita, mas material que o usuário publica amanhã.

## Priorize pelo canal principal

Faça **impecável** o que aparece primeiro no canal do briefing; o resto entra como esquema simples.

| Canal principal | Peças que precisam estar perfeitas |
|---|---|
| Instagram | avatar (símbolo a 40px), bio escrita, capa de destaque, 1 post de anúncio, 1 story |
| WhatsApp | foto de perfil, mensagem de apresentação, catálogo, imagem de lista de transmissão |
| PDV físico | fachada/placa, cardápio, etiqueta, uniforme/avental, adesivo |
| Embalagem | rótulo em uma cor, selo, lacre, cartão de agradecimento |
| Site / app | favicon, header, botão primário, tokens CSS |
| Marketplace | thumb do produto, banner da loja, título padronizado |

## Kit mínimo, sempre

Independentemente do canal, estas cinco peças cabem em qualquer negócio e são as mais pedidas depois:

1. **Avatar** (símbolo isolado, quadrado, legível a 40px)
2. **Assinatura de e-mail** (HTML simples, sem imagem externa)
3. **Cartão de visita ou etiqueta** (frente e verso, com margem de corte de 3mm se for para gráfica)
4. **Post de anúncio** 1080×1350
5. **Capa/banner** do canal principal

## Como produzir

- Peças estáticas (post, story, etiqueta, cartão): construa como HTML nas dimensões exatas e exporte com o
  `scripts/build_brandbook.py` (que aceita `--png` e um seletor de tamanho) ou renderize direto pelo Chromium
  disponível no ambiente. HTML é editável depois; imagem gerada não é.
- Tokens para código (quando houver site ou app): entregue um bloco `:root` com as variáveis de cor, fonte, raio e
  espaçamento. É o que garante que o produto digital não desvie da marca em três sprints.
- Templates editáveis: se a pessoa vai produzir sozinha toda semana, entregue um HTML com texto trocável e diga
  exatamente onde mexer. Um template que só você sabe editar não sobrevive.

## Encerramento

Liste em 5 linhas o que depende de terceiros, sem virar consultoria jurídica ou contábil:
- registro de marca (INPI, classe provável) — confirmar com profissional de propriedade industrial
- domínio e handles a reservar
- licença de fonte, se comercial
- fornecedor de impressão/embalagem e o formato que ele precisa receber
- o que o usuário deve refazer daqui a 6 meses com base no que aprender vendendo
