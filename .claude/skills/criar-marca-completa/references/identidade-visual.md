# Identidade visual

Regra que organiza tudo aqui: **cada elemento precisa de um papel declarado**. Paleta sem papéis vira decoração e cada
pessoa que aplica a marca escolhe diferente. É por isso que uma marca "some" depois de três meses.

## Paleta

Defina exatamente estes papéis. Mais que isso é enfeite; menos, e alguém vai improvisar.

| Papel | Quantidade | Função |
|---|---|---|
| Primária | 1 | identidade — a cor que a pessoa lembra |
| Primária escura | 1 | fundos densos, cabeçalhos, texto sobre claro |
| Primária clara | 1–2 | fundos suaves, estados hover, gráficos |
| Acento | 1 | **só** para ação: botão de compra, preço, CTA |
| Neutros | 3–4 | texto, borda, fundo de página, superfície |
| Semânticas | 3 | sucesso, alerta, erro — necessárias assim que houver app, painel ou formulário |

A cor de acento tem a regra mais importante e mais violada: se ela aparece em título, ícone decorativo e fundo, ela
deixa de significar "clique aqui" e o botão de compra perde força. Escreva isso no manual com um exemplo errado ao
lado.

**Proporção de uso** — dê a receita, não só os hex: aproximadamente 60% neutro, 30% primária, 10% acento. É o que
impede a marca de virar uma parede monocromática saturada.

**Contraste** é requisito, não preferência. Rode antes de fechar:

```bash
python3 scripts/paleta_check.py "#752F8A" "#FFCE01" "#1A1A1A" "#FFFFFF"
```

Alvos: 4.5:1 para texto corrido, 3:1 para texto grande (24px+) e para bordas/ícones funcionais. Se a primária não
atinge 4.5:1 com branco, ela **não serve para texto** — declare isso no manual em vez de esperar que alguém descubra.
Registre também qual par usar sobre fundo escuro; marca sem versão escura quebra no primeiro app ou story.

## Tipografia

Duas famílias resolvem quase tudo: uma de **display** (títulos, nome, números grandes) e uma de **texto** (corrido,
interface). Uma terceira só entra com justificativa funcional (mono para código/valores tabulares).

Critérios de escolha, nessa ordem:
1. **Licença** — priorize fontes de licença aberta (Google Fonts) salvo se o usuário puder comprar; fonte comercial
   usada sem licença é um problema real que aparece no primeiro material impresso.
2. **Suporte a português** — acentos e "ç" precisam existir e estar bem desenhados; muitas display bonitas falham aqui
   e o nome quebra.
3. **Pesos disponíveis** — mínimo 3 pesos na fonte de texto, senão a hierarquia depende de tamanho e vira ruim.
4. **Coerência com o posicionamento** — ver tabela no `briefing.md`.

Defina uma **escala** e registre no manual, com uso declarado por nível:

```
Display    48/1.05  peso 700  letter-spacing 0.02em  → nome, capas
H1         32/1.15  peso 700                          → título de página
H2         24/1.2   peso 600                          → seção
Corpo      16/1.55  peso 400                          → texto corrido
Apoio      13/1.4   peso 500                          → legenda, rótulo
Micro      11/1.3   peso 700  caixa alta 0.1em        → tag, overline
```

Escala fixa é o que faz materiais feitos por pessoas diferentes parecerem da mesma marca.

## Logo

Construa em SVG, à mão, no editor. Não gere imagem raster para logo: logo precisa escalar, mudar de cor e ser editado.

**O que entregar:**

| Variação | Uso |
|---|---|
| Principal (horizontal) | padrão, cabeçalhos, site |
| Vertical/empilhada | espaços quadrados, embalagem, carimbo |
| Símbolo isolado | avatar, favicon, etiqueta pequena, selo |
| Monocromática positiva | impressão em uma cor, gravação |
| Monocromática negativa | fundo escuro, fotografia |

**Como construir um símbolo que funciona:**
- Comece pela **ideia** (o que o símbolo representa) e desenhe com formas geométricas simples — círculo, retângulo,
  arco, linha de espessura constante. Um símbolo com muitos nós é impossível de bordar, gravar ou reduzir.
- Trabalhe sobre um `viewBox` quadrado (ex.: `0 0 64 64`) e mantenha uma margem óptica interna.
- Teste em 32px e em 16px: se virou mancha, retire detalhe até voltar a ler.
- Evite gradiente no logo principal. Gradiente não sobrevive a fax, carimbo, bordado, silk de uma cor e impressão
  barata — e é exatamente onde o logo de um negócio pequeno mais aparece.
- Evite texto dentro do símbolo, e evite o clichê literal da categoria (garfo e faca para comida, engrenagem para
  tecnologia, folha para sustentável). O clichê torna a marca substituível.

**Regras de uso** que precisam estar no manual, sempre com exemplo errado ao lado do certo:
- Área de proteção (defina em função de um elemento do próprio logo, ex.: "altura da letra inicial")
- Tamanho mínimo em px e em mm
- O que nunca fazer: distorcer, girar, recolorir fora da paleta, aplicar sombra, colocar sobre foto sem contraste,
  contornar

## Grid e formas

Fixe três decisões e a marca ganha consistência sem esforço:
- **Raio de borda** (0, 4, 8, 12 ou 999px) — expressa a personalidade tanto quanto a cor
- **Espaçamento base** (4 ou 8px) e a escala derivada
- **Sombra/elevação**: uma ou duas definições, não seis

## Fotografia e ilustração

Diga o que **sim** e o que **não**, com critério visual concreto: luz (natural quente vs. dura), enquadramento
(aberto vs. macro), presença de pessoas, tratamento de cor. Se o usuário for fotografar com celular — o caso mais
comum — dê 3 instruções práticas que ele consiga seguir sozinho amanhã.
