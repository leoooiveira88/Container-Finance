# Componentes da Atalaia

Todos usam as variáveis de `assets/tokens.css`. Copie os tokens para o repositório antes de construir
qualquer tela.

## Cabeçalho da plataforma

Altura fixa de 56 px, fundo Noite, símbolo completo a 32 px. O contador de toques é o único elemento em
laranja — e em fundo escuro o acento é `#F2893D`, nunca `#B4560E`.

```html
<header class="at-top">
  <div class="at-marca">
    <svg width="32" height="32" viewBox="0 0 64 64" aria-label="Atalaia"><!-- símbolo completo, arcos #F2893D --></svg>
    <span class="at-nome">Atalaia</span>
  </div>
  <span class="at-badge"><span class="at-ponto"></span>3 toques</span>
</header>
```

```css
.at-top{display:flex;align-items:center;gap:12px;height:56px;padding:0 18px;background:var(--at-noite)}
.at-marca{display:flex;align-items:center;gap:10px}
.at-nome{font-family:var(--at-display);font-weight:700;font-size:19px;color:#fff;line-height:1}
.at-badge{margin-left:auto;display:flex;align-items:center;gap:7px;
  background:rgba(242,137,61,.16);color:var(--at-acento-em-escuro);
  font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  padding:5px 10px;border-radius:var(--at-raio-chip)}
.at-ponto{width:6px;height:6px;border-radius:50%;background:var(--at-acento-em-escuro)}
```

## Cartão de toque

O componente mais importante do produto: é onde o Princípio do Muro vira interface. Mesma anatomia nos
três estados — selo de severidade, o que aconteceu, o número em Plex Mono, a origem do dado e a saída
sugerida.

**A regra que não se negocia:** cartão sem saída sugerida só existe no estado resolvido. Em qualquer
outro, alerta sem saída é toque incompleto.

```html
<article class="at-toque">
  <div class="at-corpo">
    <span class="at-selo at-selo--atencao">Atenção</span>
    <div class="at-titulo">Alfa saiu do previsto</div>
    <div class="at-dado">Margem 18,2% → 14,1% · −4,1 p.p. em 21 dias</div>
    <div class="at-origem">Origem: Think Track + base de custo-hora · atualizado há 2 h · regra MG-04</div>
  </div>
  <button class="at-acao">Ver as saídas</button>
</article>
```

```css
.at-toque{background:var(--at-superficie);border:1px solid rgba(22,24,28,.14);
  border-left:3px solid var(--at-acento-em-claro);border-radius:var(--at-raio);
  padding:14px 16px;display:flex;gap:14px;align-items:flex-start}
.at-toque--critico{border-left-color:var(--at-critico)}
.at-toque--ok{border-left-color:var(--at-positivo-em-claro)}
.at-corpo{flex:1;min-width:0}
.at-titulo{font-weight:600;font-size:14.5px;color:var(--at-tinta);margin-bottom:3px}
.at-dado{font-family:var(--at-dado);font-size:13px;font-variant-numeric:tabular-nums;color:var(--at-tinta)}
.at-origem{font-size:11.5px;color:rgba(22,24,28,.55);margin-top:6px}
.at-acao{background:var(--at-acento-em-claro);color:#fff;border:0;border-radius:4px;
  padding:7px 12px;font-family:var(--at-texto);font-size:12px;font-weight:600;cursor:pointer;white-space:nowrap}
.at-acao:focus-visible{outline:2px solid var(--at-tinta);outline-offset:2px}
.at-selo{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  padding:3px 7px;border-radius:var(--at-raio-chip);display:inline-block;margin-bottom:6px}
.at-selo--atencao{background:#FBEDE2;color:var(--at-acento-em-claro)}
.at-selo--critico{background:#FAE7E6;color:var(--at-critico)}
.at-selo--ok{background:#EFF3DF;color:var(--at-positivo-em-claro)}
```

## Assinatura de e-mail

Em tabela, como todo cliente de e-mail exige. **O símbolo vai como PNG hospedado** — Gmail e Outlook
removem SVG inline. Acento na versão para fundo claro.

```html
<table cellpadding="0" cellspacing="0" border="0"
       style="font-family:Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#16181C;font-size:13px;line-height:1.45">
  <tr>
    <td style="padding-right:14px;vertical-align:top">
      <img src="https://SEU-ENDERECO/icone-48.png" width="40" height="40" alt="Atalaia"
           style="display:block;border-radius:9px">
    </td>
    <td style="border-left:2px solid #B4560E;padding-left:14px">
      <div style="font-family:Georgia,serif;font-size:18px;font-weight:700;color:#1B1E24">Atalaia</div>
      <div style="font-size:9px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;color:#5A6068;padding:3px 0 8px">
        Plataforma de inteligência operacional</div>
      <div><strong>NOME</strong> · Cargo</div>
      <div style="color:#5A6068">email@think.com.br · +55 11 90000-0000</div>
      <div style="padding-top:8px;font-family:Georgia,serif;font-style:italic;color:#B4560E">Ninguém decide no escuro.</div>
    </td>
  </tr>
</table>
```

## Ao criar componente novo

Antes de fechar, confira três coisas:

1. O acento usado bate com o fundo? (`#F2893D` no escuro, `#B4560E` no claro)
2. Todo número em coluna está em Plex Mono com `tabular-nums`?
3. Se é um alerta, tem saída sugerida? Se não tem, ou é estado resolvido ou está incompleto.
