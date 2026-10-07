# Handoff · 6 motions para o 2º turno (2026)

## 1. Resumo e status

**Resumo:** seis motion graphics verticais (9:16, 1080×1920, até 60s), só tipografia e formas, para convencer quem se absteve (~33 milhões) e quem votou branco/nulo (~6 milhões) no 1º turno de 04/10/2026 a votar em Lula no 2º turno de 25/10/2026.

**Status (07/10/2026):**

| Item | Situação |
|---|---|
| Storyboard dos 6 vídeos | Aprovado: `storyboards/storyboard-2turno.html` |
| Paleta, fontes e regras | Definidas (seções 4 e 5) |
| Voz | Definida: Higgsfield `text2speech_v2`, variante `elevenlabs`, voz "Andre" (seção 7) |
| Vídeo 1 (piloto) | Renderizado na sessão de nuvem: `motion/v1/v1-final.mp4` (60s, 1080×1920, H.264 CRF 16, trilha e efeitos sintetizados, −14 LUFS). **Sem locução**, porque o CDN da Higgsfield estava bloqueado na nuvem (seção 7). Passou por 3 rodadas de folha de contato (`motion/v1/contact/`). Falta revalidar com a skill de motion. |
| Vídeos 2 a 6 | Não iniciados |
| Legendas dos posts | Rascunho pronto em `handoff/captions.md` |
| Skill de motion do usuário | Não estava disponível na sessão de nuvem. Precisa estar no desktop. |
| HyperFrames | CLI existe no npm (`hyperframes` v0.8.140, "create, preview, and render HTML video compositions"), **não testada** |
| Git | Branch `claude/storyboard-2turno` em `leoooiveira88/Container-Finance`, com `storyboards/`, `handoff/` e `motion/v1/` commitados. |

Arquivos de apoio:

- `storyboards/storyboard-2turno.html`: storyboard aprovado (fonte da verdade para beats, motion e locução)
- `handoff/assets/Programa-Governo-LULA-2026.pdf`: Programa de Governo (fonte da paleta e das citações, p. 73 e 75)
- `handoff/captions.md`: legendas prontas para os 6 posts
- `motion/v1/`: piloto do Vídeo 1

---

## 2. Decisões do usuário

1. **Ordem de postagem:** V1 (Dia 1) → V2 "Nulo não anula" → V3 "Quanto vale o seu domingo?" → V4 "Não precisa amar. Precisa escolher." → V5 "Cadeira vazia" → V6 "Dá pra votar, sim" (véspera, sábado 24/10). A numeração do storyboard já segue essa ordem.
2. **Fontes na tela.** Cada dado aparece com a fonte em texto pequeno no quadro, e a lista completa vai na legenda do post.
3. **Nenhuma imagem ou áudio de candidato.** Sem foto do Lula, sem rosto ou voz gerados por IA, sem imitação.
4. **Sem ataques e sem comparação com o adversário.** No V1 as barras dizem só "1º" e "2º", sem nomes.
5. **Paleta e identidade** tiradas do Programa de Governo (PDF).
6. **Voz sintética:** Higgsfield `text2speech_v2`, variante `elevenlabs`, voz pronta "Andre".
7. **Rodapé no quadro final:** "Conteúdo independente de apoiador" (no storyboard: "Conteúdo independente de apoiador · fontes na legenda").
8. Conteúdo de **apoiador, não oficial**, para as redes do próprio usuário.

---

## 3. Dados verificados (com fonte)

| Dado | Valor | Fonte | Usado em |
|---|---|---|---|
| Data do 1º turno | 04/10/2026 | TSE | V1, V2 |
| Data do 2º turno | 25/10/2026 (domingo) | TSE | todos |
| Abstenção no 1º turno | 33.469.244 (21,08% do eleitorado) | TSE, via Agência Brasil | V1 |
| 1º colocado | 56.104.503 votos (47,03%) | TSE, 100% das urnas, via Reuters (print do usuário) | V1 |
| 2º colocado | 53.879.538 votos (45,16%) | TSE, 100% das urnas, via Reuters (print do usuário) | V1 |
| Diferença entre 1º e 2º | 2.224.965 | cálculo: 56.104.503 − 53.879.538 | V1 |
| Abstenção ÷ diferença | 15,04× | cálculo: 33.469.244 ÷ 2.224.965 | V1 |
| Brancos e nulos | 1,84% brancos, 2,93% nulos, cerca de 6 milhões no total (**aproximado**) | TSE (percentuais), sobre cerca de 125 milhões de comparecimentos | V2 |
| Branco/nulo não anula eleição | "votos nulos e brancos não anulam a eleição" | TRE-MG, Código Eleitoral | V2 |
| Horário de votação | 8h às 17h (horário de Brasília). Manaus e Cuiabá: 7h às 16h (hora local) | TSE, calendário eleitoral 2026 | V1, V6 |
| Quem faltou no 1º turno | Pode votar no 2º normalmente. Justificativa do 1º até 03/12/2026 | TRE-SP, justificativa eleitoral | V6 |
| Empregos | 8,0 milhões de empregos entre 2023 e junho de 2026 (declaração do programa, atribuir como tal) | Programa de Governo, p. 73 | V4 |
| Salário mínimo | "aumento real para o piso de remuneração todos os anos" | Programa de Governo, p. 73 | V4 |
| Fim da 6x1 e 40h | "assegurar o fim da escala 6x1 e a redução da jornada de trabalho para 40 horas, sem redução salarial, nos termos aprovados na Câmara dos Deputados" | Programa de Governo, p. 75 | V3, V4 |
| Igualdade salarial | "fortalecendo a implementação da Lei de Igualdade Salarial" | Programa de Governo, p. 75 | V4 |
| PEC das 40h | Aprovada na Câmara em maio/2026. Está no Senado. | Câmara dos Deputados, Poder360/Estado de Minas | V3 |
| Apoio ao fim da 6x1 | 69% | Genial/Quaest, julho/2026, via Revista Fórum | V3 |
| Isenção do IR até R$ 5 mil | conforme storyboard | Agência Senado (nov/2025) | V4 |

### Pendências de verificação

- [ ] **Brancos e nulos exatos:** trocar "cerca de 6 milhões" pelo número final do TSE (contagem absoluta de brancos + nulos do 1º turno). Se o número exato não for encontrado, manter "cerca de 6 milhões" e os percentuais.
- [x] **Citação do V3 (p. 75):** corrigida no storyboard para o texto literal do PDF: "…o fim da escala 6x1 e a redução da jornada de trabalho para 40 horas, sem redução salarial".
- [ ] **Isenção do IR até R$ 5 mil (V4):** a fonte do storyboard é Agência Senado (nov/2025), mas ela não foi conferida nesta sessão. Abrir a matéria e confirmar antes do render.
- [ ] **Passe livre (V6):** varia por município. O vídeo só diz "confere se tem passe livre na sua cidade", sem afirmar que existe.
- [ ] **Link de cada fonte** para a legenda: Agência Brasil (abstenção), Reuters (resultado), TRE-MG, TRE-SP, TSE, Revista Fórum (Quaest), Poder360/Estado de Minas (PEC), Agência Senado (IR).

---

## 4. Identidade visual

**Paleta (do Programa de Governo):**

| Token | Hex | Uso |
|---|---|---|
| vermelho logo | `#E82028` | acento principal, bloco "15×", fundo de impacto |
| laranja | `#CF4A24` | colunas da semana 6x1, faixa de 4 cores |
| azul | `#546BE3` | fundos de bloco, pontos da abstenção, faixa de 4 cores |
| azul escuro | `#4955AF` | apoio (links e detalhes) |
| amarelo | `#F2C740` | fundos de bloco, destaques, faixa de 4 cores |
| verde | `#52943B` | checks, "40h", faixa de 4 cores |
| creme | `#F5F1E8` | fundo base |
| tinta (texto) | `#1B1B24` | texto sobre creme (definido no storyboard) |

**Tipografia:**

- O PDF usa Transducer Black/Bold nos títulos e Gotham/Sora no texto. Transducer e Gotham são pagas.
- **Título (display):** Archivo, `font-stretch:125%` (wdth 125), `font-weight:900`.
- **Texto e interface:** Sora.
- Regra: uma fonte de título, uma de texto.

**Assinatura visual:**

- Blocos de texto (slabs) **inclinados em −6°**, inspirados no lettering "LULA PRESIDENTE".
- **Faixa de 4 cores:** verde, laranja, azul, amarelo (nessa ordem), no fim de todo vídeo.
- **Quadro final (CTA) padrão:** frase-gancho do vídeo no topo → blocos "VOTE" / "LULA" / "13" batendo em sequência, um por beat → data "25 OUT · 2º TURNO" (no V6: "AMANHÃ · 25/10") → rodapé "Conteúdo independente de apoiador · fontes na legenda" → faixa de 4 cores varrendo da esquerda para a direita.
- O selo "VOTE LULA 13" é **inspirado** na identidade e **não copia** o logo oficial.
- Exceção do brief à regra de "uma cor de acento": a paleta tem 4 cores. O vermelho é o acento, e as outras entram como fundo de bloco.

---

## 5. Regras de motion (contrato)

Extraídas do print "Motion studio rules" do usuário. A borda direita da imagem estava cortada, então pode haver regras que não foram lidas. **Se a skill de motion do desktop tiver a versão completa, ela vale mais que esta lista.**

**Render**

- Todo filme é uma função pura do tempo: `window.seek(t)` pinta o quadro.
- Proibido no render: transições CSS, `setTimeout`, `requestAnimationFrame`, estado guardado entre quadros.
- Ruído só com semente (`mulberry32`).
- Render com `node render.mjs`. Saída H.264 `yuv420p`, CRF 16.

**Look**

- Padrões proibidos: título centralizado sobre gradiente, tudo surgindo em fade, rótulos de canto, moldura, brilho em elementos de interface, partículas genéricas.
- Uma fonte de título e uma de texto. Uma cor de acento, salvo exceção do brief (aqui: paleta de 4 cores com vermelho como acento).
- **A cada 2 a 4 segundos, algo novo acontece na tela.**

**Som**

- Trilha e efeitos sintetizados em código, a não ser que uma faixa seja fornecida.
- Batidas posicionadas sobre a grade de beats medida (`beats.json`).
- Loudness final: −14 LUFS.

**Loop de qualidade (antes do render final)**

1. Renderizar 1 quadro por beat e montar uma folha de contato. Olhar a folha.
2. Dar nota de 1 a 10 para: gancho nos 2 primeiros segundos, leitura no celular, qualidade do movimento, variedade, fidelidade à marca e sincronia com o som.
3. Corrigir os 3 piores pontos.
4. Repetir até **todas as notas serem 8 ou mais**. Só então fazer o render completo.

---

## 6. Os 6 roteiros

Copiados do storyboard aprovado. A coluna "Tela / motion" traz o texto que aparece no quadro (em **negrito**) e a instrução de movimento. A coluna "Fonte" traz o crédito que aparece na tela no beat.

Datas de postagem: o storyboard define a sequência (Dia 1 a Dia 5, e o V6 na véspera, 24/10). As datas exatas dos Dias 1 a 5 ficam a critério do usuário, antes de 24/10.

### Vídeo 1 · "Você era maior que a diferença"

- **Público:** quem não foi votar.
- **Objetivo:** comparar escalas, mostrando o tamanho da abstenção contra o tamanho da diferença. O número sozinho convence. O tom é de quem chama, não de quem dá bronca.
- **Postagem:** Dia 1.
- **Cor da etiqueta:** vermelho.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–2s | Fundo vermelho. **"33.469.244 pessoas não foram votar no domingo."** O número entra dígito a dígito, girando como caça-níquel com 40ms entre dígitos. Aterrissa no beat 1 com um "thump". | "Domingo, trinta e três milhões de brasileiros não foram votar." | TSE · 1º turno 04/10/2026 |
| 2–8s | Fundo creme. **"Diferença entre 1º e 2º colocados" · "1º · 56.104.503" · "2º · 53.879.538" · "2.224.965"**. Duas barras crescem da esquerda, sem nomes nem fotos (só "1º" e "2º"). Um traço vermelho marca a sobra entre elas e o número da diferença sobe de baixo. | "Sabe qual foi a diferença entre o primeiro e o segundo colocado? Dois milhões e duzentos mil votos." | TSE · 100% das urnas |
| 8–16s | Fundo creme. **"1 ponto = 100 mil pessoas" · "22 pontos vermelhos = diferença · 335 azuis = abstenção"**. Aparecem 22 pontos vermelhos (a diferença). Depois a grade explode em 335 pontos azuis (a abstenção), em ondas no ritmo da música. | "Agora olha quem ficou em casa: quinze vezes mais gente do que essa diferença." | (cálculo próprio) |
| 16–24s | Fundo amarelo. **"15×" · "maior que a diferença que decidiu o 1º turno."** Um bloco vermelho "15×" entra girando de −20° para −6°, com um pequeno tremor de câmera no impacto. A frase de apoio é escrita palavra a palavra. | "Quem não votou tinha força pra decidir essa eleição. E deixou outros decidirem." | 33.469.244 ÷ 2.224.965 = 15,04 |
| 24–36s | Fundo creme. **"Não precisa amar ninguém." · "Precisa não deixar escolherem por você."** Tipografia batida: cada palavra cai em um beat. A segunda frase troca para vermelho no último "você". | "Você não precisa amar candidato nenhum. Mas ficar em casa não é neutro: deixa outros escolherem seu salário, seu emprego, o futuro da sua família." | — |
| 36–50s | Fundo azul. **"25 OUT" · "domingo · 2º turno" · "8h às 17h (Brasília)"**. Uma folha de calendário vira (flip 3D) e revela "25 OUT". A linha de horário desliza para dentro. | "Dia vinte e cinco de outubro tem segundo turno. Dessa vez, a decisão pode ser sua." | TSE |
| 50–60s | Quadro final padrão com o gancho **"Vai votar."** Os blocos VOTE, LULA e 13 batem em sequência (3 beats), e a faixa de 4 cores varre da esquerda para a direita. As fontes ficam na legenda do post. | "Vai votar. Vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: TSE (via Agência Brasil e Reuters) e cálculo próprio.

### Vídeo 2 · "Nulo não anula"

- **Público:** quem votou branco ou nulo.
- **Objetivo:** desfazer um mito com respeito. O protesto é legítimo, mas na urna ele some. A virada do vídeo é "protesto que funciona é escolher".
- **Postagem:** Dia 2.
- **Cor da etiqueta:** azul.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–2s | Fundo azul. **"Votou nulo pra protestar?"** A pergunta aparece em três golpes, um por beat, com o cursor de digitação de uma urna (bip). | "Votou nulo ou branco pra protestar? Tenho uma notícia." | — |
| 2–8s | Fundo creme. **"NULO" · "não anula eleição."** O bloco "NULO" racha ao meio e as metades caem para fora do quadro com gravidade simulada (seed fixa). | "Branco e nulo não anulam eleição. Isso é mito." | TRE-MG · Código Eleitoral |
| 8–18s | Fundo creme. **"VOTOS VÁLIDOS" · "branco" · "nulo" · "→ fora da conta"**. Cédulas coloridas caem dentro da caixa "votos válidos". As cinzas (branco/nulo) quicam na borda e saem do quadro. | "Eles simplesmente não entram na conta. Quem decide o resultado são só os votos válidos." | — |
| 18–28s | Fundo amarelo. **"~6 mi" · "de votos brancos e nulos no 1º turno." · "1,84% brancos · 2,93% nulos"**. Um contador sobe de 0 a cerca de 6 milhões, com tique de relógio. Os percentuais entram como etiqueta. | "No primeiro turno, foram cerca de seis milhões de votos que não contaram pra ninguém." | TSE · apuração do 1º turno |
| 28–42s | Fundo creme. **"Protesto que ninguém conta…" · "ninguém escuta."** A primeira linha é escrita e o "…" pulsa. A segunda linha bate em vermelho, e a primeira fica cinza (perde contraste). | "Seu recado não chegou a lugar nenhum. Ninguém leu, ninguém contou." | — |
| 42–52s | Fundo vermelho. **"No 2º turno, protesto que funciona é escolher."** Wipe diagonal em vermelho, seguindo o ângulo de −6° da marca. A frase entra em 4 batidas. | "No segundo turno, o protesto que funciona é escolher quem protege seus direitos." | — |
| 52–60s | Quadro final padrão com o gancho **"Seu voto conta. Faz ele contar."** | "Dia vinte e cinco, vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: TRE-MG ("votos nulos e brancos não anulam a eleição") e TSE (percentuais). **Pendência:** número exato de brancos + nulos.

### Vídeo 3 · "Quanto vale o seu domingo?"

- **Público:** trabalhadores, principalmente na escala 6x1.
- **Objetivo:** a pauta mais concreta e popular. Só proposta positiva, sem comparar com ninguém.
- **Postagem:** Dia 3.
- **Cor da etiqueta:** laranja.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–2s | Fundo creme. Semana **S T Q Q S S** (laranja) **D** (amarelo). **"6 dias de trabalho. 1 de vida."** Seis colunas laranja batem uma por beat (ritmo de ponto batido) e a sétima acende em amarelo. | "Seis dias de trabalho. Um de vida." | — |
| 2–10s | Fundo laranja. **"44h" · "por semana. É o limite de hoje."** O número "44h" é desenhado como relógio de ponto, com o ponteiro girando e o som de tique sincronizado. | "Hoje a jornada pode chegar a quarenta e quatro horas por semana." | — |
| 10–20s | Fundo creme. **"44h" → "40h" · "Câmara aprovou em maio: 40h e 2 dias de descanso. Falta o Senado."** O "44" se transforma em "40" por interpolação dos contornos do número, e a cor vai de laranja para verde. | "Em maio, a Câmara aprovou reduzir pra quarenta horas, com dois dias de descanso. Agora falta o Senado." | Câmara dos Deputados · maio/2026 |
| 20–32s | Fundo azul. **"PROGRAMA DE GOVERNO LULA 2026" · citação literal "…o fim da escala 6x1 e a redução da jornada de trabalho para 40 horas, sem redução salarial"**. A citação entra linha a linha e "sem redução salarial" é sublinhado com um traço amarelo. **Ver a pendência da seção 3: usar o trecho literal do PDF.** | "O programa de Lula assume o compromisso: fim da seis por um e quarenta horas, sem reduzir salário." | Programa de Governo, p. 75 |
| 32–42s | Fundo amarelo. **"69%" · "dos brasileiros apoiam o fim da 6x1."** O 69% sobe como contador, ao lado de uma rosca de 7 em 10 bonequinhos. | "Sete em cada dez brasileiros querem isso." | Genial/Quaest · julho/2026 |
| 42–52s | Fundo creme. Semana **S T Q Q S** (laranja) **S D** (verde). **"Seu sábado de volta."** É a semana do primeiro quadro: a coluna de sábado vira verde de baixo para cima, como copo enchendo. | "Imagina ter o sábado pra sua família, seus amigos, pra você." | — |
| 52–60s | Quadro final padrão com o gancho **"Quer o sábado de volta?"** | "Dia vinte e cinco, vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: Programa de Governo Lula 2026 (p. 75), Poder360/Estado de Minas (PEC aprovada na Câmara em maio) e Genial/Quaest via Revista Fórum (69%).

### Vídeo 4 · "Não precisa amar. Precisa escolher."

- **Público:** os desiludidos ("ninguém me representa").
- **Objetivo:** validar o sentimento e mudar a pergunta. Mostra uma lista de direitos com fonte, sem citar adversário.
- **Postagem:** Dia 4.
- **Cor da etiqueta:** verde.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–2s | Fundo creme. **"Acha que ninguém te representa?"** Texto preto em fundo creme, entrando por máscara de baixo para cima linha a linha, sem fade. | "Acha que ninguém te representa?" | — |
| 2–7s | Fundo creme. **"Justo."** O bloco "Justo." bate como carimbo e a frase de cima é empurrada para fora. | "Justo. Muita gente sente isso." | — |
| 7–14s | Fundo azul. **"Então troca a pergunta:" · "Quem protege o que é seu?"** Um wipe azul atravessa a tela e o "seu?" pulsa uma vez em amarelo. | "Então troca a pergunta: quem vai proteger o que é seu?" | — |
| 14–44s | Fundo creme. Checklist: **"✓ Salário mínimo com aumento real todo ano" · "✓ Isenção de IR para quem ganha até R$ 5 mil" · "✓ Fim da 6x1, 40h sem cortar salário" · "Igualdade salarial entre mulheres e homens" · "8 milhões de empregos (2023–jun/26)"**. Cinco itens, um a cada 6s. O check verde é desenhado como traço e o item fica em negrito. A fonte de cada item aparece no rodapé enquanto ele está ativo. | "Salário mínimo com aumento acima da inflação. Isenção de imposto de renda até cinco mil reais. Fim da escala seis por um. Salário igual pra mulher e homem. E, segundo o governo, oito milhões de empregos criados desde 2023." | Programa de Governo p. 73 e 75 · Agência Senado (IR) |
| 44–52s | Fundo verde. **"Não é sobre paixão." · "É sobre seus direitos."** A primeira frase fica estática e a segunda entra como bloco amarelo inclinado. | "Não é sobre paixão. É sobre os seus direitos." | — |
| 52–60s | Quadro final padrão com o gancho **"Escolhe o que te protege."** | "Dia vinte e cinco, vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: Programa de Governo Lula 2026 (p. 73: salário mínimo e 8,0 mi de empregos; p. 75: 6x1 e igualdade salarial) e Agência Senado (isenção do IR, nov/2025). O dado de 8 milhões de empregos é declaração do programa de governo e vai atribuído como tal ("segundo o governo").

### Vídeo 5 · "Cadeira vazia"

- **Público:** quem não foi votar (versão emocional).
- **Objetivo:** metáfora visual em ilustração plana e geométrica, vista de cima e sem pessoas desenhadas. Na mesa do Brasil, quem não senta come o que os outros escolhem.
- **Postagem:** Dia 5.
- **Cor da etiqueta:** amarelo.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–3s | Fundo creme. **"Tem uma cadeira vazia nessa mesa."** Mesa vista de cima. As cadeiras coloridas deslizam até o lugar, e a última fica tracejada e vazia. | "Tem uma cadeira vazia nessa mesa." | — |
| 3–12s | Fundo creme. **"Cada um escolhe o seu prato."** Cada cadeira ganha um prato. Pequenas setas saem das cadeiras ocupadas até os próprios pratos. | "Na mesa onde se decide o futuro do país, cada um escolhe o seu." | — |
| 12–24s | Fundo creme. Etiquetas **"seu salário" · "sua folga" · "o posto de saúde" · "a escola do seu filho"** · **"Quem não senta come o que os outros escolhem."** As etiquetas saem das outras cadeiras e voam para o prato vazio, uma por beat, com um "plim" de talher. | "Quem não senta, come o que os outros escolherem: seu salário, sua folga, o posto de saúde, a escola do seu filho." | — |
| 24–36s | Fundo vermelho. **"Não votar não é ficar de fora." · "É deixar escolherem por você."** Um corte seco para vermelho, a frase em 2 tempos. | "Não votar não é ficar de fora. É deixar escolherem por você." | — |
| 36–48s | Fundo creme. **"Ocupa o seu lugar."** A cadeira tracejada se preenche de amarelo, com um contorno preto que pulsa uma vez. A mesa toda fica completa. | "Você não precisa gostar de todo mundo na mesa. Só precisa ocupar o seu lugar." | — |
| 48–60s | Quadro final padrão com o gancho **"Senta na mesa."** | "Dia vinte e cinco, vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: sem dados numéricos. É um vídeo de argumento.

### Vídeo 6 · "Dá pra votar, sim"

- **Público:** todos. O vídeo tira as barreiras práticas.
- **Objetivo:** um checklist utilitário. É o vídeo mais compartilhável, porque serve para qualquer pessoa.
- **Postagem:** véspera, **sábado 24/10/2026**.
- **Cor da etiqueta:** verde.

| Tempo | Tela / motion | Locução | Fonte |
|---|---|---|---|
| 0–2s | Fundo verde. **"Faltou no 1º turno?" · "Ainda dá."** A pergunta aparece e "Ainda dá." bate como carimbo amarelo. | "Faltou no primeiro turno? Ainda dá." | — |
| 2–12s | Fundo creme. **"1" · "Pode votar no 2º normalmente." · "Cada turno é uma eleição separada. Justifica o 1º depois, até 3/12."** O número grande desliza da esquerda, o título bate e o texto de apoio é escrito. | "Quem faltou no primeiro turno pode votar no segundo normalmente. A falta você justifica depois." | TRE-SP · Justificativa eleitoral |
| 12–22s | Fundo creme. **"2" · "Não sabe onde vota?" · "e-Título"**. Um celular em traço simples abre o app e mostra "local de votação". É só ícone desenhado, sem print da interface real. | "Não sabe onde vota? Abre o e-Título." | — |
| 22–32s | Fundo creme. **"3" · "Leva documento com foto."** Um cartão de documento gira em Y e entra em cena. | "Leva um documento com foto, ou o e-Título com foto." | — |
| 32–42s | Fundo azul. **"4" · "8h às 17h" · "horário de Brasília. Em Manaus e Cuiabá, das 7h às 16h."** Os ponteiros do relógio vão de 8h a 17h em 3 segundos. | "Das oito às dezessete, horário de Brasília. Quem tá em outro fuso, confere seu horário." | TSE · calendário eleitoral 2026 |
| 42–50s | Fundo creme. **"5" · "Confere se tem passe livre na sua cidade."** Um ônibus em traço atravessa a tela da esquerda para a direita. | "E confere se a sua cidade tem passe livre no dia da eleição." | — |
| 50–60s | Quadro final padrão com o gancho **"Amanhã é o dia."** e a data **"AMANHÃ · 25/10"**. | "Amanhã, vai votar. Vota Lula, treze." | rodapé de apoiador |

Fontes do vídeo: TRE-SP (justificativa e prazos) e TSE (horário unificado, 8h às 17h de Brasília). O passe livre varia por município e não é afirmado como certo.

---

## 7. Locução

**Voz e parâmetros**

- Ferramenta: Higgsfield `generate_audio`, modelo `text2speech_v2`, variante `elevenlabs`.
- Voz pronta: **"Andre"**, `voice_id` `f1e8226e-2248-4d5f-b43c-0a79e9949dbf`.
- Custo observado: cerca de 0,3 crédito por fala.
- Gerar **uma fala por arquivo** (uma linha por beat). Assim cada fala pode ser encaixada no `beats.json` e ajustada sem refazer o vídeo inteiro.
- Depois de gerar, medir a duração de cada fala. Se uma fala passar do tempo do beat, ajustar o beat (mantendo o total ≤ 60s), não acelerar a voz.
- Mix final em −14 LUFS, com a voz acima da trilha.
- Nunca usar voz clonada ou imitação de candidato.

**Falas prontas para TTS (números por extenso).** Nomes de arquivo sugeridos: `vN_bK.mp3`.

**Vídeo 1**

1. Domingo, trinta e três milhões de brasileiros não foram votar.
2. Sabe qual foi a diferença entre o primeiro e o segundo colocado? Dois milhões e duzentos mil votos.
3. Agora olha quem ficou em casa: quinze vezes mais gente do que essa diferença.
4. Quem não votou tinha força pra decidir essa eleição. E deixou outros decidirem.
5. Você não precisa amar candidato nenhum. Mas ficar em casa não é neutro: deixa outros escolherem seu salário, seu emprego, o futuro da sua família.
6. Dia vinte e cinco de outubro tem segundo turno. Dessa vez, a decisão pode ser sua.
7. Vai votar. Vota Lula, treze.

**Vídeo 2**

1. Votou nulo ou branco pra protestar? Tenho uma notícia.
2. Branco e nulo não anulam eleição. Isso é mito.
3. Eles simplesmente não entram na conta. Quem decide o resultado são só os votos válidos.
4. No primeiro turno, foram cerca de seis milhões de votos que não contaram pra ninguém.
5. Seu recado não chegou a lugar nenhum. Ninguém leu, ninguém contou.
6. No segundo turno, o protesto que funciona é escolher quem protege seus direitos.
7. Dia vinte e cinco, vota Lula, treze.

**Vídeo 3**

1. Seis dias de trabalho. Um de vida.
2. Hoje a jornada pode chegar a quarenta e quatro horas por semana.
3. Em maio, a Câmara aprovou reduzir pra quarenta horas, com dois dias de descanso. Agora falta o Senado.
4. O programa de Lula assume o compromisso: fim da seis por um e quarenta horas, sem reduzir salário.
5. Sete em cada dez brasileiros querem isso.
6. Imagina ter o sábado pra sua família, seus amigos, pra você.
7. Dia vinte e cinco, vota Lula, treze.

**Vídeo 4**

1. Acha que ninguém te representa?
2. Justo. Muita gente sente isso.
3. Então troca a pergunta: quem vai proteger o que é seu?
4. Salário mínimo com aumento acima da inflação. Isenção de imposto de renda até cinco mil reais. Fim da escala seis por um. Salário igual pra mulher e homem. E, segundo o governo, oito milhões de empregos criados desde dois mil e vinte e três.
5. Não é sobre paixão. É sobre os seus direitos.
6. Dia vinte e cinco, vota Lula, treze.

Observação: a fala 4 cobre 30s de checklist (5 itens de 6s). Pode ser gerada em 5 arquivos, um por item, para casar com cada check.

**Vídeo 5**

1. Tem uma cadeira vazia nessa mesa.
2. Na mesa onde se decide o futuro do país, cada um escolhe o seu.
3. Quem não senta, come o que os outros escolherem: seu salário, sua folga, o posto de saúde, a escola do seu filho.
4. Não votar não é ficar de fora. É deixar escolherem por você.
5. Você não precisa gostar de todo mundo na mesa. Só precisa ocupar o seu lugar.
6. Dia vinte e cinco, vota Lula, treze.

**Vídeo 6**

1. Faltou no primeiro turno? Ainda dá.
2. Quem faltou no primeiro turno pode votar no segundo normalmente. A falta você justifica depois.
3. Não sabe onde vota? Abre o e-Título.
4. Leva um documento com foto, ou o e-Título com foto.
5. Das oito às dezessete, horário de Brasília. Quem tá em outro fuso, confere seu horário.
6. E confere se a sua cidade tem passe livre no dia da eleição.
7. Amanhã, vai votar. Vota Lula, treze.

---

## 8. Cuidados legais

Isto é uma orientação prática, não um parecer jurídico. Em caso de dúvida, consultar a legislação eleitoral vigente ou um advogado.

- **Nada de deepfake ou IA de candidato.** Não usar rosto, voz ou imagem de nenhum candidato, nem real nem gerada ou alterada por IA. A voz do narrador é sintética e neutra ("Andre"), sem imitar ninguém.
- **Sem conteúdo negativo e sem impulsionar crítica.** Os vídeos não atacam nem comparam com o adversário. Não pagar impulsionamento de conteúdo que critique ou ataque candidato. Antes de impulsionar qualquer vídeo, conferir as regras de impulsionamento da propaganda eleitoral.
- **Identificação como apoiador.** Todo quadro final tem o rodapé "Conteúdo independente de apoiador". Não usar o logo oficial (o selo "VOTE LULA 13" é só inspirado nele), nem se apresentar como perfil da campanha.
- **Fontes na legenda.** Todo dado tem fonte na tela e na legenda do post (`captions.md`). Dados aproximados aparecem como aproximados ("cerca de 6 milhões"). Declarações do programa de governo são atribuídas como tal ("segundo o governo", "Programa de Governo, p. 73").
- **Citações literais.** Texto entre aspas tem que ser idêntico ao do PDF (ver a pendência do V3).
- **Nada de prints de interfaces oficiais.** O e-Título no V6 é um ícone desenhado.
- **Passe livre:** não afirmar que existe. Só sugerir conferir.

---

## 9. Próximos passos no desktop

1. [ ] **Puxar o repositório:** `git fetch && git checkout claude/storyboard-2turno`. A pasta `handoff/` e o piloto `motion/v1/` só estarão lá se tiverem sido commitados e enviados. Se não estiverem, copiar manualmente.
2. [ ] **Instalar a skill de motion:** colocar o `SKILL.md` (e os arquivos da skill) em `.claude/skills/<nome-da-skill>/` no projeto ou em `~/.claude/skills/`. Abrir uma sessão nova e confirmar que ela aparece na lista de skills. Comparar as regras dela com a seção 5 deste README, já que o print estava cortado.
3. [ ] **Testar o HyperFrames:** `npx hyperframes@0.8.140 --help`. Criar uma composição de teste em 1080×1920, renderizar 2 segundos e conferir se respeita o contrato (`window.seek(t)`, sem rAF, H.264 yuv420p CRF 16). Decidir: HyperFrames ou o `render.mjs` próprio do piloto.
4. [ ] **Validar o piloto V1** (`motion/v1/`): gerar a folha de contato (1 quadro por beat), dar as 6 notas, corrigir os 3 piores pontos e repetir até tudo ser ≥ 8. Conferir os textos contra a seção 6. Só então fazer o render final e medir −14 LUFS.
5. [ ] **Resolver as pendências da seção 3:** brancos e nulos exatos no TSE, citação literal do V3, fonte do IR (Agência Senado).
6. [ ] **Produzir V2 a V6**, nesta ordem, reaproveitando do V1 o quadro final, a faixa de 4 cores, as fontes e o sistema de som. Para cada vídeo: gerar as falas (seção 7) → `beats.json` → composição → folha de contato → notas ≥ 8 → render.
7. [ ] **Legendas e caption do post:** revisar `handoff/captions.md`, colocar os links das fontes e conferir que cada legenda tem ≤ 600 caracteres.
8. [ ] **Agenda de postagem:** V1 a V5 em dias seguidos a partir da data escolhida, e o V6 no sábado 24/10/2026.

---

## 10. Prompt pronto para colar na nova sessão

```
Estou continuando um projeto de 6 motion graphics verticais (9:16, 1080x1920, até 60s) para o 2º turno de 25/10/2026. É conteúdo de apoiador, não oficial, para minhas redes.

Leia primeiro, nesta ordem:
1. handoff/README.md (decisões, dados com fonte, identidade, regras de motion, os 6 roteiros beat a beat, falas da locução, cuidados legais e próximos passos)
2. storyboards/storyboard-2turno.html (storyboard aprovado, que é a fonte da verdade)
3. handoff/assets/Programa-Governo-LULA-2026.pdf, páginas 73 a 75 (citações)
4. motion/v1/ (piloto do Vídeo 1, ainda não validado)

Regras que não mudam:
- Nenhuma imagem, foto, rosto ou voz de candidato, nem real nem gerada por IA. Só tipografia e formas.
- Sem ataque e sem comparação com o adversário.
- Fonte de cada dado na tela e na legenda. Não invente números, datas nem fontes: use só o que está no README. O que estiver como pendência, me pergunte ou verifique.
- Paleta: #E82028, #CF4A24, #546BE3, #4955AF, #F2C740, #52943B, fundo #F5F1E8. Títulos em Archivo (wdth 125, peso 900), texto em Sora, blocos inclinados -6°, faixa de 4 cores no fim, rodapé "Conteúdo independente de apoiador".
- Voz: Higgsfield text2speech_v2, variante elevenlabs, voz "Andre" (voice_id f1e8226e-2248-4d5f-b43c-0a79e9949dbf), uma fala por arquivo.
- Siga a minha skill de motion (contrato de render puro em função do tempo, folha de contato com notas ≥ 8 antes do render final, -14 LUFS). Se ela divergir do README, a skill vale mais.

Tarefa de hoje, seguindo a seção 9 do README:
1. Confirme que a minha skill de motion está carregada e teste o HyperFrames (npx hyperframes@0.8.140).
2. Valide o piloto V1 com a folha de contato e me mostre as notas antes de renderizar.
3. Depois siga para V2, V3, V4, V5 e V6, um de cada vez, me mostrando a folha de contato de cada um.
Não faça commit nem push sem eu pedir.
```


---

## Anexo A · Locução do Vídeo 1 já gerada na Higgsfield

As 7 falas do V1 foram geradas com a voz "Andre" (`text2speech_v2` / `elevenlabs`, 0,3 crédito cada) e estão na biblioteca Higgsfield do usuário. A sessão de nuvem não conseguiu baixar os arquivos porque o CDN estava bloqueado pela rede. No desktop, baixe as falas e mixe usando os `vo_slots` de `motion/v1/beats.json`. Abaixe a trilha uns 8 dB durante a voz (ducking) e normalize o mix final em −14 LUFS.

| Fala | Slot (s) | Job ID Higgsfield |
|---|---|---|
| vo1 "Domingo, trinta e três milhões…" | 0,0–3,3 | 4590259a-aeeb-4fd8-a9fa-7aba088dbb15 |
| vo2 "Sabe qual foi a diferença…" | 3,4–9,3 | 1deb8cd3-f1f7-4316-abbc-4f6ee4e603a3 |
| vo3 "Agora olha quem ficou em casa…" | 9,4–16,8 | c9d04fd6-495a-4895-9dc9-84668172dc39 |
| vo4 "Quem não votou tinha força…" | 16,9–23,8 | e7cd6c86-2f96-4e97-a616-c3877d1c0acc |
| vo5 "Você não precisa amar…" | 24,0–35,8 | 8d6e0826-b75d-404e-9ec9-a652e81c9e98 |
| vo6 "Dia vinte e cinco de outubro…" | 36,0–47,8 | b852194d-59f8-4e9b-ad09-021d816fcc8a |
| vo7 "Vai votar. Vota Lula, treze." | 48,2–53,0 | 7aebb1f0-b6c6-40bf-b2ca-6bb3e00f5667 |

Comando de mix sugerido, depois de salvar as falas como `motion/v1/vo/vo1.mp3` a `vo7.mp3`. Os atrasos do `adelay` são o início de cada slot em ms:

```bash
cd motion/v1
ffmpeg -i v1-final.mp4 -i vo/vo1.mp3 -i vo/vo2.mp3 -i vo/vo3.mp3 -i vo/vo4.mp3 -i vo/vo5.mp3 -i vo/vo6.mp3 -i vo/vo7.mp3 -filter_complex "\
[1]adelay=0|0[a1];[2]adelay=3400|3400[a2];[3]adelay=9400|9400[a3];[4]adelay=16900|16900[a4];\
[5]adelay=24000|24000[a5];[6]adelay=36000|36000[a6];[7]adelay=48200|48200[a7];\
[a1][a2][a3][a4][a5][a6][a7]amix=inputs=7:normalize=0[vo];\
[0:a][vo]sidechaincompress=threshold=0.05:ratio=6:release=300[duck];\
[duck][vo]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[mix]" \
-map 0:v -map "[mix]" -c:v copy -c:a aac -b:a 192k v1-com-voz.mp4
```

Confira se cada fala cabe no slot. Se uma fala ficar mais longa, ajuste a velocidade da voz (`speech_rate`) ou estique o beat no `index.html`. Todos os tempos do vídeo derivam de `b(n)`.

## Anexo B · Arquivos do piloto (`motion/v1/`)

- `index.html`: a composição. `window.seek(t)` é função pura do tempo, com grade de beats `b(n)=0,3+0,5n` (120 BPM) e ruído com semente (mulberry32).
- `render.cjs`: `node render.cjs video` gera o `silent.mp4`. `node render.cjs contact '[t1,t2,…]'` gera os quadros da folha de contato.
- `score.py`: sintetiza trilha e efeitos sobre a grade de beats e grava o `beats.json`.
- `fonts/`: Archivo e Sora em cópia local, para o render não depender da rede.
