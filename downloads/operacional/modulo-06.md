# MÓDULO 6: Planilhas Inteligentes com IA

**Objetivo:** Dashboards e análises que se atualizam sozinhos

---

## 1. Google Sheets: Sua Nova Superpotência

### Por Que Este Módulo Vai Mudar Sua Vida Profissional

Imagine acordar e abrir uma planilha que:
- Já importou todos os dados de vendas do dia anterior
- Calculou automaticamente as metas atingidas
- Destacou em vermelho o que precisa de atençêo
- Enviou um relatório formatado por email para seu chefe
- Tudo isso **sem você tocar em nada**

Nêo é ficçêo científica. É o que você vai aprender a fazer HOJE.

### Por Que Google Sheets > Excel para Automaçêo

**Antes de você gritar "mas eu uso Excel há 15 anos!"**, ouça isso:

**1. Vive na nuvem**
- Acessa de qualquer lugar (celular, tablet, computador)
- Nunca perde dados (auto-save a cada segundo)
- Zero preocupaçêo com backup

**2. Integraçêo nativa com tudo**
- Gmail, Google Forms, Google Drive
- APIs REST (buscar dados de qualquer sistema)
- Zapier, Make, Integromat
- Apps Script (automaçêo nativa)

**3. Colaboraçêo em tempo real**
- 10 pessoas editando ao mesmo tempo
- Chat dentro da planilha
- Histórico completo de versões

**4. GRATUITO**
- Excel Online é limitado
- Google Sheets free tem 99% das funcionalidades

**5. Fórmulas exclusivas poderosas**
- IMPORTRANGE (conectar planilhas)
- QUERY (SQL dentro do Sheets)
- IMPORTXML (web scraping)
- GOOGLETRANSLATE (traduçêo automática)

### Quando AINDA Usar Excel

**Seja honesto:** Use Excel quando:
- Planilhas gigantes (>1 milhêo de linhas)
- Macros VBA muito complexas já existentes
- Gráficos super customizados
- Trabalha 100% offline

**Para tudo mais:** Google Sheets vence de lavada.

### Migrando de Excel para Sheets (5 minutos)

**Passo 1: Upload**
1. Drive.google.com
2. Arrastar arquivo .xlsx
3. Botêo direito → Abrir com → Google Planilhas
4. Pronto! Convertido.

**Passo 2: Ajustes comuns**
- 90% das fórmulas funcionam igual
- Algumas funções mudam nome (ex: `PROCV` vira `VLOOKUP` em inglês, mas `PROCV` também funciona!)
- Macros VBA nêo funcionam (mas você vai aprender Apps Script, que é melhor)

### Seu Primeiro Projeto: Dashboard Pessoal

Ao final deste módulo, você terá:
- Dashboard com todas suas métricas importantes
- Atualizaçêo automática todo dia
- Alertas quando algo sai do esperado
- Visualizaçêo bonita e profissional

**Tempo estimado de economia:** 3-5 horas/semana em relatórios manuais.

---

## 2. Fórmulas que Economizam Horas (O Arsenal Completo)

### A Verdade Sobre Fórmulas

**80% das pessoas** usam apenas 5 fórmulas:
- SOMA, MÉDIA, SE, PROCV, CONT.SE

**Os 20% mais produtivos** usam as 15 fórmulas abaixo e **economizam 10x mais tempo**.

Você vai virar parte dos 20% HOJE.

### 1. IMPORTRANGE - Conectar Planilhas (Superpoder #1)

**O que faz:** Importa dados de OUTRA planilha automaticamente.

**Sintaxe:**
```
=IMPORTRANGE("URL_da_planilha", "Nome_aba!Intervalo")
```

**Exemplo prático:**
```
=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1ABC...XYZ", "Vendas!A1:D100")
```

**Caso de uso real:**
Você tem:
- Planilha A: Vendas (atualizada pelo comercial)
- Planilha B: Financeiro (atualizada pelo financeiro)
- Planilha C: Dashboard (você quer consolidar tudo)

**Soluçêo:**
```
// Na planilha Dashboard, célula A1:
=IMPORTRANGE("URL_planilha_vendas", "Dados!A2:G")

// Célula A100:
=IMPORTRANGE("URL_planilha_financeiro", "Dados!A2:E")
```

**Primeiro uso:** Vai pedir permissêo (clique "Permitir acesso").

**Atualizaçêo:** Automática! Sempre que as planilhas originais mudarem, sua dashboard atualiza.

**Tempo economizado:** De copiar/colar 20 minutos/dia → 0 minutos.

### 2. QUERY - SQL Dentro do Sheets (Superpoder #2)

**O que faz:** Filtra, ordena, agrupa dados como se fosse um banco de dados.

**Sintaxe:**
```
=QUERY(intervalo, "comando SQL", cabeçalhos)
```

**Exemplo 1: Filtrar vendas acima de R$ 1000**
```
=QUERY(A1:D100, "SELECT * WHERE D > 1000")
```

**Exemplo 2: Somar vendas por vendedor**
```
=QUERY(A1:D100, "SELECT A, SUM(D) GROUP BY A LABEL SUM(D) 'Total'")
```

**Exemplo 3: Top 10 produtos mais vendidos**
```
=QUERY(A1:D100, "SELECT B, SUM(D) GROUP BY B ORDER BY SUM(D) DESC LIMIT 10")
```

**Caso de uso real:**
Você tem planilha com 5.000 linhas de vendas. Precisa de:
- Vendas do mês atual
- Por vendedor
- Apenas produtos categoria "Premium"
- Ordenado por valor

**Sem QUERY:** 10-15 minutos filtrando manualmente toda vez.

**Com QUERY:**
```
=QUERY(Vendas!A:F,
  "SELECT B, SUM(E)
   WHERE C = 'Premium'
   AND A >= date '2024-11-01'
   GROUP BY B
   ORDER BY SUM(E) DESC
   LABEL SUM(E) 'Total Vendido'")
```

**Tempo:** 30 segundos para escrever, atualiza automaticamente para sempre.

### 3. ARRAYFORMULA - Uma Fórmula para Todas as Linhas

**O que faz:** Aplica uma fórmula em TODAS as linhas de uma vez (sem arrastar).

**Sintaxe:**
```
=ARRAYFORMULA(sua_fórmula)
```

**Exemplo: Calcular comissêo (5%) para 10.000 vendas**

**Jeito antigo (ruim):**
- Célula C2: `=B2*0.05`
- Arrastar até C10000
- Se adicionar linha nova, tem que arrastar de novo

**Jeito ninja (bom):**
```
// Célula C2:
=ARRAYFORMULA(IF(B2:B="";"";B2:B*0.05))
```

**Explicaçêo:**
- `B2:B` = pega TODA a coluna B
- `IF(B2:B="";"";...)` = se célula vazia, deixa vazia (senêo fica #N/D)
- `B2:B*0.05` = multiplica tudo por 5%

**Resultado:** UMA fórmula que funciona para infinitas linhas. Adicionou linha nova? Já calcula automaticamente.

**Exemplo 2: Concatenar Nome + Sobrenome**
```
=ARRAYFORMULA(IF(A2:A="";"";A2:A&" "&B2:B))
```

**Tempo economizado:** De 5 minutos ajustando fórmulas → 0 minutos.

### 4. GOOGLETRANSLATE - Traduçêo Instantânea

**O que faz:** Traduz texto automaticamente.

**Sintaxe:**
```
=GOOGLETRANSLATE(texto, "idioma_origem", "idioma_destino")
```

**Exemplo:**
```
=GOOGLETRANSLATE(A2, "en", "pt")
```

**Caso de uso real:**
- Você recebe planilha de fornecedor americano em inglês
- 500 linhas de descrições de produtos
- Precisa traduzir tudo

**Soluçêo:**
```
=ARRAYFORMULA(IF(A2:A="";"";GOOGLETRANSLATE(A2:A, "en", "pt")))
```

**Tempo:** 2 segundos vs. 2 horas copiando no Google Tradutor.

### 5. IMPORTXML - Web Scraping (Pegar Dados de Sites)

**O que faz:** Extrai dados de qualquer site (tabelas, preços, textos).

**Sintaxe:**
```
=IMPORTXML("URL", "xpath")
```

**Exemplo 1: Pegar cotaçêo do dólar**
```
=IMPORTXML("https://www.google.com/finance/quote/USD-BRL", "//div[@class='YMlKec fxKbKc']")
```

**Exemplo 2: Monitorar preço de produto concorrente**
```
=IMPORTXML("URL_produto_amazon", "//span[@class='a-price-whole']")
```

**Caso de uso real:**
- Você quer monitorar preço de 20 concorrentes
- Atualizar todo dia
- Alertar se algum baixar preço

**Soluçêo:**
1. Coluna A: URLs dos produtos
2. Coluna B: `=ARRAYFORMULA(IMPORTXML(A2:A, "xpath_do_preço"))`
3. Formataçêo condicional: vermelho se preço < seu preço

**Atualizaçêo:** Automática quando abrir a planilha.

**Atençêo:** Alguns sites bloqueiam scraping. Use com moderaçêo e respeite os termos de uso.

### 6. IMPORTDATA - Importar CSV da Web

**O que faz:** Importa arquivo CSV direto de uma URL.

**Sintaxe:**
```
=IMPORTDATA("URL_do_arquivo.csv")
```

**Exemplo:**
```
=IMPORTDATA("https://dados.gov.br/dataset/xyz/arquivo.csv")
```

**Caso de uso real:**
- Seu fornecedor disponibiliza estoque em CSV online
- Atualiza a cada hora
- Você quer sempre a versêo mais recente

**Soluçêo:**
```
=IMPORTDATA("https://fornecedor.com.br/estoque.csv")
```

**Sheets atualiza automaticamente** a cada algumas horas.

### 7. FILTER - Filtro Dinâmico

**O que faz:** Filtra dados e atualiza automaticamente.

**Sintaxe:**
```
=FILTER(intervalo, condiçêo1, condiçêo2, ...)
```

**Exemplo 1: Vendas acima de R$ 5000**
```
=FILTER(A2:D100, D2:D100>5000)
```

**Exemplo 2: Vendas do vendedor "Joêo" no mês de Novembro**
```
=FILTER(A2:D100, B2:B100="Joêo", C2:C100>=DATA(2024,11,1))
```

**Exemplo 3: Combinar com outras funções**
```
// Soma todas as vendas do Joêo:
=SUM(FILTER(D2:D100, B2:B100="Joêo"))
```

**Caso de uso real:**
Dashboard com abas por vendedor. Em vez de criar filtro manual para cada um:

```
// Aba "Joêo":
=FILTER(Base!A:D, Base!B:B="Joêo")

// Aba "Maria":
=FILTER(Base!A:D, Base!B:B="Maria")
```

**Atualiza automaticamente** quando adicionar vendas novas na base.

### 8. SORT - Ordenar Automaticamente

**O que faz:** Ordena dados dinamicamente.

**Sintaxe:**
```
=SORT(intervalo, coluna_para_ordenar, ordem)
```

**Exemplo: Top 10 vendedores**
```
=SORT(A2:D100, 4, FALSE)
```
- `4` = ordena pela coluna 4 (valor)
- `FALSE` = decrescente (maior primeiro)

**Combinar com FILTER:**
```
=SORT(FILTER(A2:D100, C2:C100="Premium"), 4, FALSE)
```
→ Filtra produtos Premium E ordena por valor

### 9. UNIQUE - Remover Duplicados

**O que faz:** Lista apenas valores únicos.

**Sintaxe:**
```
=UNIQUE(intervalo)
```

**Exemplo: Lista de clientes únicos**
```
=UNIQUE(A2:A1000)
```

**Caso de uso real:**
Você tem 5.000 vendas e quer saber quantos clientes diferentes compraram:

```
=COUNTEUNIQUE(A2:A5000)
```

Ou lista de todos clientes únicos:
```
=UNIQUE(A2:A5000)
```

### 10. SPLIT - Separar Texto

**O que faz:** Divide texto em colunas.

**Sintaxe:**
```
=SPLIT(texto, "separador")
```

**Exemplo: Separar nome completo**
```
// Célula A1: "Joêo Silva Santos"
=SPLIT(A1, " ")
// Resultado: "Joêo" | "Silva" | "Santos"
```

**Caso de uso real:**
Você importou CSV com endereço completo em uma célula: "Rua ABC, 123, Sêo Paulo, SP"

```
=SPLIT(A2, ", ")
```

Resultado em 4 colunas separadas.

### 11. TEXTJOIN - Juntar Textos

**O que faz:** Oposto do SPLIT. Junta várias células em uma.

**Sintaxe:**
```
=TEXTJOIN("separador", ignorar_vazios, intervalo)
```

**Exemplo:**
```
// Juntar nome + sobrenome + cidade com vírgula:
=TEXTJOIN(", ", TRUE, A2:C2)
```

**Caso de uso real:**
Criar nome de arquivo: `Cliente_Produto_Data.pdf`

```
=TEXTJOIN("_", TRUE, A2, B2, TEXT(C2, "YYYY-MM-DD"))&".pdf"
```

### 12. REGEXMATCH / REGEXEXTRACT - Busca Avançada

**O que faz:** Busca padrões em texto.

**REGEXMATCH:** Retorna TRUE/FALSE se encontrou padrêo
**REGEXEXTRACT:** Extrai o padrêo encontrado

**Exemplo 1: Verificar se email é válido**
```
=REGEXMATCH(A2, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
```

**Exemplo 2: Extrair CEP de endereço**
```
// Endereço: "Rua ABC, 123, Sêo Paulo, SP, 01234-567"
=REGEXEXTRACT(A2, "\d{5}-\d{3}")
// Resultado: "01234-567"
```

**Exemplo 3: Extrair número de telefone**
```
=REGEXEXTRACT(A2, "\(\d{2}\)\s\d{4,5}-\d{4}")
```

### 13. COUNTIF / SUMIF - Contar e Somar com Condições

**COUNTIF:** Conta células que atendem condiçêo
**SUMIF:** Soma células que atendem condiçêo

**Exemplos:**
```
// Quantas vendas acima de R$ 1000?
=COUNTIF(D2:D100, ">1000")

// Soma de vendas do produto "X":
=SUMIF(B2:B100, "Produto X", D2:D100)

// Quantos emails do domínio "gmail.com"?
=COUNTIF(A2:A100, "*@gmail.com")
```

### 14. INDEX + MATCH - PROCV Turbinado

**O que faz:** Busca valores (mais flexível que PROCV).

**Sintaxe:**
```
=INDEX(coluna_retorno, MATCH(valor_busca, coluna_busca, 0))
```

**Exemplo:**
```
// Buscar preço do produto "Notebook":
=INDEX(C2:C100, MATCH("Notebook", A2:A100, 0))
```

**Vantagem sobre PROCV:**
- Funciona em qualquer direçêo (PROCV só para direita)
- Mais rápido em planilhas grandes

### 15. SPARKLINE - Gráficos Minúsculos Dentro das Células

**O que faz:** Cria mini-gráficos dentro de uma célula.

**Sintaxe:**
```
=SPARKLINE(dados, opções)
```

**Exemplo 1: Linha de tendência**
```
=SPARKLINE(A2:A30)
```

**Exemplo 2: Barra de progresso**
```
=SPARKLINE(B2, {"charttype", "bar"; "max", 100; "color1", "green"})
```

**Exemplo 3: Gráfico de coluna**
```
=SPARKLINE(A2:F2, {"charttype", "column"; "color", "blue"})
```

**Caso de uso real:**
Dashboard com tendência de vendas dos últimos 30 dias ao lado de cada produto.

---

## 3. IA no Google Sheets (O Futuro é AGORA)

### Como IA Está Revolucionando Planilhas

**Antigamente:**
- Você passava horas categorizando dados manualmente
- "Este cliente é pequeno, médio ou grande empresa?"
- "Este produto é categoria A, B ou C?"
- 5.000 linhas = 5.000 decisões manuais

**Hoje com IA:**
- Descreve a regra em português
- IA categoriza 5.000 linhas em 30 segundos
- Precisêo de 95%+

### Add-on Recomendado: GPT for Sheets and Docs

**Instalaçêo (2 minutos):**
1. Google Sheets → Extensões → Complementos → Obter complementos
2. Buscar "GPT for Sheets and Docs"
3. Instalar (by Talarian)
4. Configurar API key do OpenAI (veja próxima seçêo)

### Configurar API do ChatGPT (5 minutos)

**Passo 1: Criar conta OpenAI**
- platform.openai.com
- Criar conta (se nêo tiver)

**Passo 2: Gerar API Key**
1. platform.openai.com/api-keys
2. "Create new secret key"
3. Copie a chave (só mostra uma vez!)

**Passo 3: Colocar no Sheets**
1. Sheets → Extensões → GPT for Sheets → Set API Key
2. Cole a chave
3. Salvar

**Custo:**
- ~$0.002 por 1.000 tokens (muito barato)
- Para 1.000 categorizações: ~$0.20 centavos de dólar
- Você coloca crédito (ex: $5) e usa aos poucos

### Casos de Uso Práticos de IA no Sheets

#### 1. Categorizar Dados Automaticamente

**Problema:** Você tem 2.000 descrições de produtos desorganizadas.

**Soluçêo com IA:**

```
=GPT("Classifique este produto em: Eletrônicos, Alimentos, Vestuário, Outros. Retorne apenas a categoria: "&A2)
```

**Exemplo:**
- A2: "Notebook Dell 15 polegadas"
- Resultado: "Eletrônicos"

**Para aplicar em todas linhas:**
```
=ARRAYFORMULA(IF(A2:A="";"";GPT("Classifique em Eletrônicos/Alimentos/Vestuário/Outros (só categoria): "&A2:A)))
```

#### 2. Extrair Informações de Texto Livre

**Problema:** Comentários de clientes em texto livre. Você quer extrair sentimento e assunto.

**Entrada (célula A2):**
```
"Produto chegou quebrado, muito insatisfeito com a entrega. O atendimento tentou ajudar mas nêo resolveu."
```

**Fórmula:**
```
=GPT("Analise o comentário e retorne apenas: [SENTIMENTO: Positivo/Neutro/Negativo] [ASSUNTO: Produto/Entrega/Atendimento/Preço]: "&A2)
```

**Resultado:**
```
[SENTIMENTO: Negativo] [ASSUNTO: Entrega]
```

#### 3. Gerar Textos em Massa

**Problema:** Criar 500 descrições de produtos para e-commerce.

**Entrada:**
- Coluna A: Nome do produto
- Coluna B: Características principais

**Fórmula:**
```
=GPT("Escreva descriçêo de produto para e-commerce (máx 50 palavras, tom persuasivo). Produto: "&A2&". Características: "&B2)
```

**Exemplo:**
- A2: "Mouse Gamer RGB"
- B2: "7 botões programáveis, DPI ajustável até 16000, iluminaçêo RGB personalizável"

**Resultado:**
```
"Eleve sua experiência gaming com este mouse de alta precisêo! 7 botões programáveis para comandos rápidos, sensor óptico até 16000 DPI para movimentos ultra-precisos e iluminaçêo RGB customizável para combinar com seu setup. Ergonomia premium para maratonas de jogo. Domine com estilo!"
```

#### 4. Análise de Sentimentos

**Problema:** 1.000 avaliações de clientes. Quantas sêo positivas/negativas?

**Fórmula:**
```
=GPT("Analise o sentimento e retorne apenas: Positivo, Neutro ou Negativo: "&A2)
```

**Depois:**
```
// Contar quantas positivas:
=COUNTIF(B2:B1000, "Positivo")
```

#### 5. Traduçêo em Massa (Melhor que GOOGLETRANSLATE)

**Fórmula:**
```
=GPT("Traduza para português mantendo tom profissional: "&A2)
```

**Vantagem:** ChatGPT entende contexto melhor que Google Translate.

#### 6. Limpar e Padronizar Dados

**Problema:** Dados de telefone bagunçados:
- (11) 98765-4321
- 11987654321
- +55 11 98765-4321
- 11 9 8765-4321

**Fórmula:**
```
=GPT("Padronize este telefone no formato (XX) XXXXX-XXXX: "&A2)
```

**Resultado:** Todos no mesmo formato.

#### 7. Gerar Fórmulas Complexas (IA como Assistente)

**Você em vez de procurar no Google:**

```
=GPT("Escreva uma fórmula do Google Sheets que calcule a média das vendas dos últimos 7 dias, ignorando fins de semana e feriados, para o vendedor Joêo")
```

**IA responde com a fórmula pronta** (você só copia e cola).

### Apps Script: Automaçêo Nativa do Sheets

**O que é:** JavaScript para automatizar Google Sheets (grátis).

**Quando usar:**
- Atualizar dados em horário específico
- Enviar emails automáticos da planilha
- Criar menus personalizados
- Integrações complexas

**Exemplo 1: Enviar Email Automático Quando Valor Atingir Meta**

```javascript
function verificarMeta() {
  var planilha = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Vendas");
  var vendas = planilha.getRange("B2").getValue(); // Célula com total de vendas
  var meta = 100000;

  if (vendas >= meta) {
    MailApp.sendEmail({
      to: "chefe@empresa.com",
      subject: "🎉 META ATINGIDA!",
      body: "Parabéns! As vendas atingiram R$ " + vendas
    });
  }
}
```

**Configurar para rodar automaticamente:**
1. Extensões → Apps Script
2. Cole o código
3. Relógio (ícone) → Adicionar acionador
4. Escolha: "verificarMeta", "Acionado por tempo", "Todo dia", "8h-9h"
5. Salvar

**Resultado:** Todo dia às 8h, verifica se atingiu meta e envia email.

**Exemplo 2: Importar Dados de API Externa**

```javascript
function importarDados() {
  var url = "https://api.exemplo.com/vendas";
  var resposta = UrlFetchApp.fetch(url);
  var json = JSON.parse(resposta.getContentText());

  var planilha = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dados");
  planilha.getRange(2, 1, json.length, 3).setValues(json);
}
```

**Configure para rodar a cada 1 hora** e sempre terá dados atualizados.

---

## 4. Dashboards Automáticos (Visualizaçêo Profissional)

### Princípios de um Bom Dashboard

**1. Menos é Mais**
- Máximo 6-8 métricas por tela
- Hierarquia visual clara (maior = mais importante)

**2. Atualizaçêo Automática**
- Usuário nunca deve ter que "atualizar" manualmente
- Use fórmulas dinâmicas

**3. Cores com Propósito**
- Verde: tudo bem
- Amarelo: atençêo
- Vermelho: urgente
- Cinza: neutro

**4. Contexto é Rei**
- Nunca mostre número sozinho
- Sempre compare: "vendas hoje vs. ontem", "meta vs. realizado"

### Estrutura de Dashboard Profissional

**Aba 1: Dashboard (visualizaçêo)**
- Só gráficos e métricas principais
- Sem dados brutos

**Aba 2: Dados Brutos**
- Importaçêo automática (IMPORTRANGE, API, etc.)
- Sem formataçêo

**Aba 3: Processamento**
- Fórmulas QUERY, FILTER, etc.
- Dados tratados

**Aba 4: Configurações**
- Parâmetros (meta, período, filtros)
- Usuário pode ajustar

### Template de Dashboard Operacional (Copy & Paste)

**Métricas essenciais:**

1. **KPI Principal** (tamanho 48, negrito)
   ```
   Vendas do Mês: R$ 125.430
   Meta: R$ 100.000 (125% ✅)
   ```

2. **Comparativo**
   ```
   vs. Mês Anterior: +15% 📈
   vs. Mesmo Mês Ano Passado: +22% 📈
   ```

3. **Tendência (gráfico de linha)**
   - Últimos 30 dias
   - Média móvel de 7 dias

4. **Top 5 / Bottom 5**
   - Melhores vendedores
   - Piores produtos

5. **Alertas**
   - Estoque abaixo do mínimo: 3 itens ⚠️
   - Clientes sem comprar há >60 dias: 12 🔴

### Fórmulas para Dashboard

**1. KPI com % da Meta**
```
="Vendas: R$ "&TEXT(SUM(Vendas!D:D),"#.##0")&" ("&TEXT(SUM(Vendas!D:D)/Meta,"0%")&")"
```

**2. Comparativo vs. Período Anterior**
```
=TEXT((SUM(FILTER(Vendas!D:D, Vendas!A:A>=HOJE()-30)) / SUM(FILTER(Vendas!D:D, Vendas!A:A>=HOJE()-60, Vendas!A:A<HOJE()-30)))-1, "+0%;-0%")
```

**3. Contador de Alertas**
```
=COUNTIF(Estoque!C:C, "<10") // Itens com estoque abaixo de 10
```

**4. Data/Hora de Última Atualizaçêo**
```
="Última atualizaçêo: "&TEXT(AGORA(), "DD/MM/YYYY HH:MM")
```

### Formataçêo Condicional Inteligente

**Regra 1: Verde se atingiu meta**
- Seleciona célula de % da meta
- Formato → Formataçêo condicional
- Se valor >= 100% → Verde

**Regra 2: Escala de cores**
- Seleciona coluna de vendas
- Formataçêo condicional → Escala de cores
- Menor valor = vermelho claro
- Maior valor = verde escuro

**Regra 3: Ícones**
- Seleciona células
- Formataçêo condicional → "Conjunto de ícones"
- Escolhe: ▲ (acima meta), — (na meta), ▼ (abaixo)

### Google Data Studio (Looker Studio) - Dashboards Profissionais

**O que é:** Ferramenta gratuita do Google para dashboards interativos.

**Quando usar:**
- Precisa compartilhar dashboard com muitas pessoas
- Quer interatividade (filtros clicáveis)
- Visual ultra-profissional

**Setup básico:**
1. datastudio.google.com
2. "Criar" → "Fonte de dados"
3. Conectar Google Sheets
4. Arrastar métricas e gráficos
5. Personalizar design

**Vantagem:** Atualiza automaticamente quando Sheets atualiza.

### 5 Dashboards Prontos para Copiar

**1. Dashboard de Vendas**
- Vendas do dia/semana/mês
- Top 10 produtos
- Top 10 vendedores
- Gráfico de tendência
- % da meta

**2. Dashboard de Estoque**
- Itens abaixo do mínimo
- Valor total em estoque
- Produtos sem movimento >30 dias
- Curva ABC

**3. Dashboard Financeiro**
- Receitas vs. Despesas
- Fluxo de caixa projetado
- Contas a pagar vencendo
- Contas a receber atrasadas

**4. Dashboard de Projetos**
- Tarefas concluídas vs. pendentes
- Projetos no prazo vs. atrasados
- Horas trabalhadas
- Budget utilizado

**5. Dashboard Pessoal**
- Horas trabalhadas hoje
- Tarefas concluídas
- Emails respondidos
- Próximos compromissos

**Link para templates:** (adicione link do Google Drive com templates compartilhados)

### Erros Comuns em Dashboards (E Como Evitar)

#### Erro 1: Excesso de Informaçêo

**Problema:** Dashboard com 30 métricas diferentes em uma única tela.

**Por quê é ruim:**
- Paralisia analítica (nêo sabe para onde olhar)
- Números importantes se perdem no meio
- Tempo de carregamento lento
- Difícil de entender rapidamente

**Soluçêo:**
- Regra 5-7-9: máximo 5 métricas principais, 7 gráficos, 9 KPIs totais
- Crie múltiplas abas para diferentes níveis de detalhamento
- Aba 1: Visêo Executiva (só o essencial)
- Aba 2: Detalhamento Operacional
- Aba 3: Dados Brutos

**Exemplo prático:**
```
❌ RUIM:
- 25 métricas em uma tela
- Gráficos pequenos e ilegíveis
- Cores aleatórias

✅ BOM:
ABA "EXECUTIVO":
- Receita do mês (grande, destaque)
- % da meta (com ícone visual)
- Top 3 produtos
- Tendência 30 dias (gráfico limpo)

ABA "OPERACIONAL":
- Vendas por vendedor
- Vendas por regiêo
- Vendas por categoria
- Detalhamento diário
```

#### Erro 2: Métricas Sem Contexto

**Problema:** Mostrar "Vendas: R$ 50.000" sem comparaçêo.

**Por quê é ruim:**
- 50k é bom ou ruim? Nêo sabemos.
- Falta referência para tomada de decisêo

**Soluçêo:** Sempre contextualize com:
- Meta (50k de 40k = 125% da meta ✅)
- Período anterior (50k vs. 45k mês passado = +11%)
- Mesmo período ano passado (50k vs. 48k nov/2023 = +4%)
- Média histórica (50k vs. média de 42k = acima da média)

**Fórmula para comparaçêo vs. período anterior:**
```
=TEXT((VALOR_ATUAL/VALOR_ANTERIOR)-1, "+0%;-0%;0%")
```

**Exemplo visual:**
```
Vendas Novembro: R$ 50.000
Meta: R$ 40.000 (125% ✅)
vs. Outubro: +11% 📈
vs. Nov/2023: +4% 📈
```

#### Erro 3: Atualizaçêo Manual

**Problema:** "Preciso copiar os dados do CRM e colar aqui toda segunda-feira"

**Por quê é ruim:**
- Você esquece de atualizar
- Dados ficam desatualizados
- Toma tempo toda semana
- Abre margem para erro

**Soluçêo:**
- Use IMPORTRANGE para buscar de outras planilhas
- Conecte via Zapier ao sistema fonte (CRM, ERP)
- Use Apps Script para buscar via API
- Configure atualizaçêo automática

**Exemplo de integraçêo:**

**Cenário:** CRM externo que exporta CSV diariamente

**Soluçêo:**
1. Configure CRM para enviar CSV por email todo dia às 7h
2. Apps Script busca email, extrai CSV, importa para Sheets
3. Dashboard atualiza automaticamente via fórmulas

```javascript
function importarCSVdoCRM() {
  var threads = GmailApp.search('from:crm@empresa.com subject:"Relatório Diário" newer_than:1d');

  if (threads.length > 0) {
    var anexos = threads[0].getMessages()[0].getAttachments();
    anexos.forEach(function(anexo) {
      if (anexo.getName().endsWith('.csv')) {
        var csv = Utilities.parseCsv(anexo.getDataAsString());
        var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Dados');
        sheet.clear();
        sheet.getRange(1, 1, csv.length, csv[0].length).setValues(csv);
      }
    });
  }
}
```

Configure trigger: Todo dia, 8h-9h.

#### Erro 4: Cores Sem Significado

**Problema:** Usar cores aleatórias ou muitas cores diferentes.

**Por quê é ruim:**
- Confunde em vez de informar
- Parece amador
- Dificulta identificaçêo rápida de problemas

**Soluçêo:** Use paleta de cores com propósito:

**Código de cores padrêo:**
- 🟢 Verde: Positivo, meta atingida, tudo bem
- 🟡 Amarelo: Atençêo, perto do limite
- 🔴 Vermelho: Urgente, meta nêo atingida, problema
- ⚪ Cinza: Neutro, informativo
- 🔵 Azul: Informaçêo, destaque sem juízo de valor

**Exemplo de formataçêo condicional:**

```
Atingimento de meta:
>= 100%: Verde
80% - 99%: Amarelo
< 80%: Vermelho

Estoque:
> Mínimo + 50%: Verde
Mínimo até Mínimo+50%: Amarelo
< Mínimo: Vermelho
```

**Como aplicar:**
1. Selecione célula/intervalo
2. Formatar → Formataçêo condicional
3. "A célula nêo está vazia" (para aplicar a todas)
4. Escolha "Escala de cores" ou regras personalizadas

#### Erro 5: Gráficos Inadequados

**Problema:** Usar tipo errado de gráfico para o dado.

**Quando usar cada tipo:**

**Gráfico de Linha:**
- ✅ Tendências ao longo do tempo
- ✅ Evoluçêo de métricas
- Exemplo: Vendas dos últimos 30 dias

**Gráfico de Colunas/Barras:**
- ✅ Comparaçêo entre categorias
- ✅ Rankings
- Exemplo: Vendas por vendedor

**Gráfico de Pizza:**
- ✅ Proporções (máximo 5-6 fatias)
- ❌ NUNCA use para comparar valores similares
- Exemplo: Distribuiçêo de vendas por regiêo

**Gráfico de Área:**
- ✅ Mostrar volume total + composiçêo ao longo do tempo
- Exemplo: Vendas empilhadas por categoria (mostra total e breakdown)

**Gauge (Velocímetro):**
- ✅ % de meta atingida
- ✅ Indicador único de performance

**Sparklines (mini-gráficos):**
- ✅ Tendências compactas dentro de tabelas
- Exemplo: Ao lado de cada produto, mostrar vendas dos últimos 7 dias

**Regra de ouro:** Se você precisa de mais de 5 segundos para entender o gráfico, escolha outro tipo.

### Otimizaçêo de Performance em Planilhas Grandes

#### Problema: Planilha Lenta

**Sinais de que sua planilha está pesada:**
- Demora >3 segundos para abrir
- Trava ao adicionar dados
- Fórmulas demoram para recalcular
- "Carregando..." aparece frequentemente

#### Soluçêo 1: Reduza Fórmulas Voláteis

**Fórmulas voláteis** recalculam SEMPRE (mesmo quando nêo precisa):
- `AGORA()` / `NOW()`
- `HOJE()` / `TODAY()`
- `RAND()` / `RANDBETWEEN()`
- `INDIRECT()`

**Problema:**
```
// Ruim: recalcula 10.000 vezes
=SE(A2<>""; AGORA(); "")
```

**Soluçêo:**
- Use com moderaçêo
- Quando possível, substitua por valor fixo
- Combine múltiplas em uma célula só

```
// Melhor: use AGORA() uma vez em célula separada
Célula Z1: =AGORA()

// Nas fórmulas, referencie Z1:
=SE(A2<>""; $Z$1; "")
```

#### Soluçêo 2: Substitua ARRAYFORMULA Muito Longos

**Problema:**
```
// 50.000 linhas calculando tudo:
=ARRAYFORMULA(IF(A2:A50000<>"";
  VLOOKUP(A2:A50000, OutraPlanilha!A:Z, 10, FALSE); ""))
```

**Soluçêo:** Limite ao intervalo necessário
```
// Melhor: só até última linha com dados
=ARRAYFORMULA(IF(A2:A<>"";
  VLOOKUP(A2:A, OutraPlanilha!A:Z, 10, FALSE); ""))
```

Ou use QUERY em vez de VLOOKUP (mais rápido):
```
=QUERY(OutraPlanilha!A:Z, "SELECT A, J WHERE A IS NOT NULL")
```

#### Soluçêo 3: Divida em Múltiplas Planilhas

**Estrutura recomendada:**

**Planilha 1: DADOS BRUTOS**
- Só importaçêo de dados
- Sem fórmulas complexas
- Atualizadas via API/Zapier

**Planilha 2: PROCESSAMENTO**
- Fórmulas QUERY, FILTER, etc.
- Puxa dados da Planilha 1 via IMPORTRANGE
- Dados tratados

**Planilha 3: DASHBOARD**
- Só visualizaçêo
- Puxa dados processados da Planilha 2
- Gráficos e formatações

**Vantagem:**
- Cada planilha carrega independentemente
- Mais rápido
- Mais organizado
- Fácil manutençêo

#### Soluçêo 4: Use Filtros em Vez de Ocultar Linhas

**Problema:** 10.000 linhas com 9.000 ocultas manualmente = lento

**Soluçêo:**
- Use Exibiçêo de Filtro (nêo afeta outros usuários)
- Ou crie abas separadas com FILTER/QUERY

```
// Aba "Vendas 2024":
=FILTER(TodosDados!A:Z, YEAR(TodosDados!A:A)=2024)
```

#### Soluçêo 5: Remova Formataçêo Condicional Excessiva

**Problema:** Formataçêo condicional em 50 colunas x 10.000 linhas

**Soluçêo:**
- Aplique só onde realmente precisa
- Use "Aplicar ao intervalo" específico (nêo coluna inteira)
- Máximo 5-7 regras de formataçêo condicional por planilha

#### Benchmark de Performance

**Planilha Leve (< 2 seg para carregar):**
- Até 5.000 linhas
- Até 20 colunas com fórmulas
- Até 10 gráficos
- Até 5 IMPORTRANGE

**Planilha Média (2-5 seg):**
- 5.000 - 20.000 linhas
- 20-50 colunas com fórmulas
- 10-20 gráficos
- 5-10 IMPORTRANGE

**Planilha Pesada (>5 seg - precisa otimizar!):**
- > 20.000 linhas
- > 50 fórmulas complexas
- > 20 gráficos
- > 10 IMPORTRANGE

**Se sua planilha está pesada:** Divida em múltiplas planilhas ou migre para Google Data Studio/Looker.

---

## 5. Automaçêo de Entrada de Dados (Nunca Mais Digite Manualmente)

### Google Forms → Sheets (Automaçêo Instantânea)

**Caso de uso:** Coleta de dados (pesquisas, pedidos, registros, etc.)

**Setup (5 minutos):**

**Passo 1: Criar Formulário**
1. forms.google.com
2. "Formulário em branco"
3. Adicione perguntas

**Passo 2: Conectar ao Sheets**
1. Aba "Respostas"
2. Ícone do Sheets (criar planilha)
3. Pronto! Cada resposta vira linha na planilha

**Passo 3: Processar Automaticamente**
Na aba "Respostas", adicione fórmulas:
```
// Coluna F (exemplo: calcular total):
=ARRAYFORMULA(IF(B2:B="";"";B2:B*C2:C))
```

**Passo 4: Enviar Email de Confirmaçêo Automático**

Apps Script:
```javascript
function aoEnviarFormulario(e) {
  var email = e.values[1]; // Assumindo que email é a 2ª pergunta
  var nome = e.values[2];

  MailApp.sendEmail({
    to: email,
    subject: "Confirmaçêo de Recebimento",
    body: "Olá " + nome + ",\n\nRecebemos seu formulário!\n\nObrigado."
  });
}
```

**Configure:**
1. Apps Script → Acionadores
2. "aoEnviarFormulario"
3. "Ao enviar formulário"

**Resultado:** Cliente preenche formulário → Dados vêo pro Sheets → Email automático enviado.

### Zapier → Sheets (Múltiplas Fontes)

**Exemplo 1: Email com anexo → Linha no Sheets**

**Trigger:** Gmail - "New Attachment"
**Action:** Google Sheets - "Create Spreadsheet Row"

**Campos:**
- Coluna A: Data/hora
- Coluna B: Remetente
- Coluna C: Assunto
- Coluna D: Link do anexo (salvo no Drive)

**Exemplo 2: Venda no E-commerce → Sheets + Email**

**Trigger:** Shopify/WooCommerce - "New Order"
**Action 1:** Sheets - "Create Row"
**Action 2:** Gmail - "Send Email" (notificar equipe)

### Importaçêo Automática de Arquivos

**Cenário:** Você recebe arquivo CSV todo dia por email.

**Soluçêo com Apps Script:**

```javascript
function importarCSVdoEmail() {
  var threads = GmailApp.search('subject:"Relatório Diário" has:attachment newer_than:1d');

  if (threads.length > 0) {
    var mensagem = threads[0].getMessages()[0];
    var anexos = mensagem.getAttachments();

    anexos.forEach(function(anexo) {
      if (anexo.getName().indexOf('.csv') > -1) {
        var conteudo = Utilities.parseCsv(anexo.getDataAsString());
        var planilha = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Importados");
        planilha.getRange(2, 1, conteudo.length, conteudo[0].length).setValues(conteudo);
      }
    });
  }
}
```

**Configure para rodar todo dia às 8h.**

---

## 6. Exercícios Práticos (Mêo na Massa!)

### Exercício 1: Criar Dashboard Pessoal (60 minutos)

**Objetivo:** Dashboard que mostra suas métricas diárias.

**Etapas:**

1. **Criar planilha "Meu Dashboard"**
2. **Aba "Dados":** Registrar diariamente:
   - Data
   - Horas trabalhadas
   - Tarefas concluídas
   - Emails respondidos
   - Nivel de energia (1-10)

3. **Aba "Dashboard":** Criar visualizaçêo:
   - Média de horas/dia (última semana)
   - Total de tarefas concluídas (mês)
   - Gráfico de tendência (energia ao longo do tempo)
   - Dias mais produtivos (maior nº de tarefas)

4. **Fórmulas sugeridas:**
```
// Média de horas (últimos 7 dias):
=AVERAGE(FILTER(Dados!B:B, Dados!A:A>=HOJE()-7))

// Total tarefas do mês:
=SUM(FILTER(Dados!C:C, MONTH(Dados!A:A)=MONTH(HOJE())))
```

**Checklist:**
- [ ] Planilha criada
- [ ] Ao menos 3 métricas
- [ ] 1 gráfico
- [ ] Formataçêo condicional em 1 célula

### Exercício 2: Implementar 5 Fórmulas Avançadas (40 minutos)

**Tarefa:** Crie planilha de vendas fake e aplique:

1. **IMPORTRANGE:** Conectar 2 planilhas diferentes
2. **QUERY:** Filtrar vendas > R$ 1000 do vendedor "Joêo"
3. **ARRAYFORMULA:** Calcular comissêo (7%) para todas linhas
4. **FILTER:** Vendas dos últimos 30 dias
5. **SPARKLINE:** Mini-gráfico de vendas de cada produto

**Dados fake para testar:**
- 50 linhas de vendas
- Colunas: Data, Vendedor, Produto, Valor

**Checklist:**
- [ ] 5 fórmulas implementadas e funcionando
- [ ] Testou adicionar linha nova (fórmulas atualizaram?)
- [ ] Compreendeu o que cada uma faz

### Exercício 3: Automatizar 1 Planilha Sua (50 minutos)

**Tarefa:** Pegue uma planilha que você usa no trabalho e automatize.

**Ideias:**
- **Relatório manual?** → Use IMPORTRANGE + QUERY
- **Copia e cola dados?** → Use IMPORTDATA ou Apps Script
- **Categoriza manualmente?** → Use IA (GPT for Sheets)
- **Envia por email?** → Automatize com Apps Script

**Checklist:**
- [ ] Identificou tarefa repetitiva
- [ ] Automatizou ao menos 50%
- [ ] Testou funcionamento
- [ ] Calculou tempo economizado

---

## 7. Casos de Uso Avançados (Aplicações Reais no Dia a Dia)

### Caso 1: Controle de Estoque Automático com Alertas

**Problema:** Empresa perde vendas por falta de estoque, mas também tem capital parado em excesso.

**Soluçêo com Sheets:**

**Estrutura da planilha:**

| Produto | Estoque Atual | Estoque Mínimo | Estoque Máximo | Status | Açêo Necessária |
|---------|---------------|----------------|----------------|--------|-----------------|
| Notebook | 5 | 10 | 50 | 🔴 BAIXO | Comprar 45 |
| Mouse | 120 | 20 | 100 | 🟡 ALTO | Reduzir pedidos |
| Teclado | 35 | 15 | 80 | 🟢 OK | Nenhuma |

**Fórmulas:**

**Coluna E (Status):**
```
=ARRAYFORMULA(IF(B2:B=""; "";
  IF(B2:B < C2:C; "🔴 BAIXO";
  IF(B2:B > D2:D; "🟡 ALTO"; "🟢 OK"))))
```

**Coluna F (Açêo Necessária):**
```
=ARRAYFORMULA(IF(B2:B=""; "";
  IF(B2:B < C2:C; "Comprar " & (D2:D - B2:B);
  IF(B2:B > D2:D; "Reduzir pedidos"; "Nenhuma"))))
```

**Apps Script para enviar alerta automático:**

```javascript
function alertarEstoqueBaixo() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Estoque');
  var dados = sheet.getDataRange().getValues();

  var alertas = [];

  for (var i = 1; i < dados.length; i++) {
    var produto = dados[i][0];
    var estoqueAtual = dados[i][1];
    var estoqueMinimo = dados[i][2];

    if (estoqueAtual < estoqueMinimo) {
      alertas.push("⚠️ " + produto + ": " + estoqueAtual + " unidades (mínimo: " + estoqueMinimo + ")");
    }
  }

  if (alertas.length > 0) {
    var corpo = "ALERTA DE ESTOQUE BAIXO\n\n" + alertas.join("\n");

    MailApp.sendEmail({
      to: "compras@empresa.com",
      subject: "🔴 URGENTE: " + alertas.length + " produtos com estoque baixo",
      body: corpo
    });
  }
}
```

**Configure trigger:** Todo dia, 9h.

**Resultado:** Equipe de compras recebe email automático quando qualquer produto ficar abaixo do mínimo.

### Caso 2: Calculadora de Margem e Precificaçêo Inteligente

**Problema:** Time comercial erra precificaçêo, vendendo abaixo do custo ou muito acima do mercado.

**Soluçêo: Planilha de precificaçêo automática**

**Inputs:**
- Custo do produto
- Despesas operacionais (%)
- Margem desejada (%)
- Preço concorrente (via web scraping)

**Fórmula de cálculo:**

```
Custo Total = Custo Produto + (Custo Produto × % Despesas)
Preço Mínimo = Custo Total / (1 - Margem Mínima)
Preço Sugerido = Custo Total / (1 - Margem Desejada)
```

**Implementaçêo:**

| Produto | Custo | Despesas | Margem Desejada | Preço Mínimo | Preço Sugerido | Preço Concorrente | Posicionamento |
|---------|-------|----------|-----------------|--------------|----------------|-------------------|----------------|
| Produto A | 100 | 30% | 40% | R$ 186 | R$ 217 | R$ 249 | ✅ Competitivo |
| Produto B | 80 | 30% | 40% | R$ 149 | R$ 173 | R$ 159 | ⚠️ Caro |

**Fórmulas:**

**Preço Mínimo (20% margem):**
```
=(B2 + (B2 * C2)) / (1 - 0.20)
```

**Preço Sugerido:**
```
=(B2 + (B2 * C2)) / (1 - D2)
```

**Posicionamento:**
```
=IF(F2 < G2; "✅ Competitivo";
  IF(F2 > G2 * 1.1; "⚠️ Caro"; "🟡 Justo"))
```

**Adicionar web scraping para preço concorrente:**
```
=IMPORTXML("URL_produto_concorrente"; "//span[@class='price']")
```

**Vantagem:** Vendedor vê na hora se preço está competitivo.

### Caso 3: Painel de Metas com Gamificaçêo

**Problema:** Equipe desmotivada, nêo sabe como está vs. meta.

**Soluçêo: Dashboard gamificado**

**Elementos:**

1. **Barra de progresso visual**
```
=SPARKLINE(B2/C2; {"charttype"\"bar"; "max"\1; "color1"\"green"})
```

2. **Ranking com medalhas**
```
=IF(RANK(B2; B:B) = 1; "🥇 ";
  IF(RANK(B2; B:B) = 2; "🥈 ";
  IF(RANK(B2; B:B) = 3; "🥉 "; "")))
& A2
```

3. **Indicador de ritmo**
"No ritmo atual, você fechará o mês com X"

```
// Assumindo que hoje é dia 15 do mês:
=B2 / 15 * 30  // Projeçêo para 30 dias
```

4. **Status motivacional**
```
=IF(B2 >= C2; "🎉 META BATIDA! PARABÉNS!";
  IF(B2 >= C2 * 0.8; "🔥 QUASE LÁ! Faltam só " & TEXT(C2-B2; "R$ #,##0");
  "💪 VAMOS COM TUDO! Você consegue!"))
```

**Atualizaçêo em tempo real:** Conecte via IMPORTRANGE com planilha de vendas.

**Resultado:** Time vê progresso em tempo real + gamificaçêo aumenta engajamento.

### Caso 4: Sistema de Aprovaçêo de Despesas

**Problema:** Despesas precisam passar por múltiplas aprovações, processo lento e manual.

**Soluçêo: Fluxo automatizado**

**Google Form para solicitar despesa:**
- Nome do solicitante
- Departamento
- Valor
- Categoria (Viagem / Material / Serviço)
- Justificativa
- Urgência (Sim/Nêo)

**Apps Script para aprovar automaticamente pequenos valores:**

```javascript
function processarDespesas() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Respostas');
  var dados = sheet.getDataRange().getValues();

  for (var i = 1; i < dados.length; i++) {
    var status = dados[i][7]; // Coluna H: Status
    if (status !== "") continue; // Já processado

    var valor = dados[i][3];
    var categoria = dados[i][4];
    var urgencia = dados[i][6];

    // Regra: Valores até R$ 200 = aprovaçêo automática
    if (valor <= 200) {
      sheet.getRange(i+1, 8).setValue("✅ Aprovado automaticamente");
      enviarNotificacao(dados[i], "aprovado");
    }
    // Valores acima de R$ 200 = envia para aprovaçêo
    else {
      sheet.getRange(i+1, 8).setValue("⏳ Aguardando aprovaçêo");
      enviarParaGestor(dados[i]);
    }
  }
}

function enviarParaGestor(dados) {
  var solicitante = dados[0];
  var valor = dados[3];
  var justificativa = dados[5];

  MailApp.sendEmail({
    to: "gestor@empresa.com",
    subject: "Aprovaçêo de Despesa: R$ " + valor,
    body: "Solicitante: " + solicitante + "\n" +
          "Valor: R$ " + valor + "\n" +
          "Justificativa: " + justificativa + "\n\n" +
          "Aprovar: [link da planilha]"
  });
}
```

**Vantagem:**
- Despesas pequenas: aprovadas em segundos
- Despesas grandes: gestor recebe email automático
- Histórico completo registrado

### Caso 5: Rastreamento de KPIs com Alertas Inteligentes

**Problema:** Gestor só descobre problema quando já é tarde.

**Soluçêo: Sistema de alertas proativos**

**Monitorar:**
- Vendas caindo >10% vs. semana anterior → 🔴 Alerta
- Taxa de conversêo caindo >5% → 🟡 Atençêo
- Ticket médio subindo >15% → 🟢 Oportunidade

**Apps Script:**

```javascript
function monitorarKPIs() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('KPIs');

  var vendasSemanaAtual = sheet.getRange('B2').getValue();
  var vendasSemanaAnterior = sheet.getRange('B3').getValue();
  var variacaoVendas = (vendasSemanaAtual / vendasSemanaAnterior) - 1;

  var alertas = [];

  if (variacaoVendas < -0.10) {
    alertas.push("🔴 CRÍTICO: Vendas caíram " + Math.abs(variacaoVendas * 100).toFixed(1) + "% vs. semana anterior");
  }

  if (alertas.length > 0) {
    MailApp.sendEmail({
      to: "gestor@empresa.com",
      subject: "🚨 ALERTA DE KPI",
      body: alertas.join("\n\n")
    });
  }
}
```

**Configure:** Todo dia, 8h.

**Resultado:** Gestor é avisado ANTES do problema se agravar.

### Caso 6: Conciliaçêo Bancária Automática

**Problema:** Reconciliar extrato bancário com lançamentos internos = 2-3 horas/semana.

**Soluçêo:**

**Passo 1:** Importar extrato bancário (CSV)
- Via upload manual ou email automático do banco

**Passo 2:** Comparar com lançamentos

```
// Marcar transações que batem:
=IF(COUNTIF(Lancamentos!C:C; A2) > 0; "✅ OK"; "⚠️ CONFERIR")
```

**Passo 3:** Destacar divergências

**Formataçêo condicional:**
- Verde: Valor confere
- Vermelho: Divergência

**Passo 4:** Apps Script para listar divergências

```javascript
function listarDivergencias() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Conciliaçêo');
  var dados = sheet.getDataRange().getValues();

  var divergencias = [];

  for (var i = 1; i < dados.length; i++) {
    if (dados[i][5] === "⚠️ CONFERIR") {
      divergencias.push(dados[i][0] + ": R$ " + dados[i][2]);
    }
  }

  if (divergencias.length > 0) {
    Logger.log("Divergências encontradas:\n" + divergencias.join("\n"));
  }
}
```

**Tempo economizado:** De 2-3h para 15-20 minutos.

---

## 8. Troubleshooting: Problemas Comuns e Soluções

### Problema 1: "IMPORTRANGE nêo funciona"

**Erro:** `#REF!` ou "You need permission"

**Causas:**
1. Planilha origem nêo deu permissêo
2. URL incorreta
3. Nome da aba ou intervalo errado

**Soluçêo:**
1. Clique no erro → "Allow access"
2. Confira URL (copie direto da barra de endereços)
3. Teste importar só célula A1 primeiro: `=IMPORTRANGE("URL"; "Aba!A1")`

### Problema 2: "Fórmula QUERY retorna erro"

**Erro:** `Unable to parse query string`

**Causas comuns:**
- Aspas erradas (usar " dentro de " causa erro)
- Sintaxe SQL incorreta
- Nome de coluna com espaço

**Soluções:**

**Errado:**
```
=QUERY(A:D; "SELECT A WHERE B = "Premium"")
```

**Certo:**
```
=QUERY(A:D; "SELECT A WHERE B = 'Premium'")
```

**Dica:** Dentro da query, use aspas simples (') para strings.

### Problema 3: "Apps Script nêo roda automaticamente"

**Sintomas:** Script funciona manual, mas trigger nêo executa.

**Causas:**
1. Trigger nêo foi salvo
2. Conta nêo deu permissêo
3. Funçêo tem erro e falha silenciosamente

**Soluções:**
1. Verifique triggers: Apps Script → Relógio (ícone)
2. Execute manual primeiro → Autorize permissões
3. Veja logs de execuçêo: Apps Script → Execuções

### Problema 4: "Planilha nêo atualiza dados importados"

**Sintomas:** IMPORTXML, IMPORTDATA retornam dados antigos

**Causa:** Google Sheets cacheia importações.

**Soluções:**
1. Force atualizaçêo: Edite fórmula (adicione espaço e apague)
2. Use parâmetro de cache-bust:
```
=IMPORTXML("URL?refresh="&NOW(); "xpath")
```
3. Configure script para limpar e reimportar diariamente

### Problema 5: "Erro: 'Exceeded maximum execution time'"

**Causa:** Apps Script rodou por mais de 6 minutos (limite do Google).

**Soluções:**
1. Divida processamento em lotes menores
2. Use triggers múltiplos (processar parte 1, depois parte 2)
3. Otimize código (evite loops desnecessários)

**Exemplo de processamento em lotes:**

```javascript
function processarEmLotes() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Dados');
  var ultimaLinhaProcessada = PropertiesService.getScriptProperties().getProperty('ultimaLinha') || 1;

  var lote = 100; // Processar 100 linhas por vez
  var dados = sheet.getRange(ultimaLinhaProcessada, 1, lote, 5).getValues();

  // Processar dados...

  PropertiesService.getScriptProperties().setProperty('ultimaLinha', ultimaLinhaProcessada + lote);
}
```

Configure trigger para rodar a cada 5 minutos até processar tudo.

---

## RESUMO DO MÓDULO: O Que Você Aprendeu

✅ **Google Sheets vs Excel:** Quando usar cada um
✅ **15 fórmulas poderosas:** IMPORTRANGE, QUERY, ARRAYFORMULA, etc.
✅ **IA no Sheets:** Categorizar, extrair, gerar textos automaticamente
✅ **Dashboards profissionais:** Métricas que se atualizam sozinhas
✅ **Automaçêo de entrada:** Forms, Zapier, Apps Script
✅ **Exercícios práticos:** Dashboard pessoal e automações reais

---

## RESULTADO ESPERADO

**Antes:**
- ⏱ 2-3 horas/dia em planilhas manuais
- 😫 Copiar e colar dados
- 📊 Relatórios desatualizados

**Depois:**
- ⏱ 30 minutos/dia (só análise, zero operacional)
- 🤖 Tudo automatizado
- 📊 Dashboards sempre atualizados

**Economia:** **3-5 horas por semana = Meio dia de trabalho!**

---

## PRÓXIMO PASSO

No **Módulo 7**, você vai aprender a **gerar documentos, relatórios e apresentações automaticamente** com IA.

Imagine criar um relatório executivo de 10 páginas em 30 segundos. É possível, e você vai aprender COMO.

**Nos vemos lá!**

---

**© 2025 FETD - Formaçêo em Engenharia de Intençêo**
