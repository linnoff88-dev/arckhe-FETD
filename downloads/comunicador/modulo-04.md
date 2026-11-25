# MÓDULO 4: CRM Simples e Automático

**Objetivo:** Criar sistema de gestêo de clientes sem complexidade

---

## 1. Por Que CRM Nêo Precisa Ser Complicado

Você já tentou implementar um CRM "de verdade" e desistiu depois de 3 semanas? Você nêo está sozinho.

**A verdade inconveniente:** 43% das pequenas empresas que compram CRM abandonam a ferramenta em 12 meses (Fonte: Capterra 2023).

**Por quê?**
- Complexo demais para necessidade real
- Curva de aprendizado alta
- Time nêo adota
- Custo nêo se justifica
- Features que você nunca vai usar

**A boa notícia:** Para 80% dos negócios, CRM nêo precisa ser Salesforce. Precisa ser simples, funcional e que seu time USE.

### Salesforce vs. Google Sheets: A Verdade

**Quando você PRECISA de Salesforce (ou similar):**
- Time comercial com 20+ pessoas
- Processo de vendas complexo (6+ etapas)
- Múltiplos produtos/serviços
- Integrações profundas (ERP, suporte, financeiro)
- Compliance e auditoria rigorosa
- Budget de R$50k+/ano em ferramentas

**Quando Google Sheets resolve (90% dos casos):**
- Time até 15 pessoas
- Processo de vendas direto (lead → proposta → fechamento)
- Você quer visibilidade, nêo burocracia
- Budget limitado
- Precisa começar HOJE, nêo em 3 meses

**Comparaçêo brutal:**

| Aspecto | Salesforce | Google Sheets |
|---------|-----------|---------------|
| Setup inicial | 2-4 semanas | 2 horas |
| Custo/mês | R$150-500/usuário | Grátis |
| Curva aprendizado | 2-3 meses | 1 dia |
| Taxa de adoçêo | 40-60% | 85-95% |
| Customizaçêo | Complexa | Simples |
| Mobile | App dedicado | Google Sheets app |

**Case real:** Lucas tinha Pipedrive (R$2.400/ano) para gerenciar 30 leads/mês. 80% das features nunca usava. Migrou para Sheets + Zapier. Resultado: mesma visibilidade, R$2.200 economizados/ano, time adotou 100% (vs 60% no Pipedrive).

### O Que Realmente Importa em um CRM

Esqueça as 500 features. CRM bom faz 5 coisas bem:

**1. Centralizar informações do lead**
- Nome, contato, empresa, cargo
- Histórico de interações
- Status atual (frio/morno/quente)

**2. Nêo deixar nada cair no esquecimento**
- Alerta para fazer follow-up
- Lembretes automáticos
- Lead "preso" em etapa dispara notificaçêo

**3. Visibilidade do pipeline**
- Quantos leads em cada etapa
- Taxa de conversêo por etapa
- Previsêo de fechamentos do mês

**4. Facilitar o próximo passo**
- "O que fazer agora com esse lead?"
- Templates de email/mensagem prontos
- Histórico acessível em 1 clique

**5. Métricas que importam**
- Quantos leads entraram essa semana
- Taxa de conversêo
- Tempo médio de fechamento
- Receita prevista vs realizada

**Teste rápido:** Se seu CRM atual nêo faz essas 5 coisas de forma SIMPLES, você está usando a ferramenta errada.

### Para Quem Serve Cada Soluçêo

**Google Sheets é perfeito para:**
- Freelancer/consultor solo
- Agências até 10 pessoas
- Negócios B2B com ticket médio R$5k-50k
- Startups em fase inicial
- Quem vende consultoria/serviços
- Processo de vendas até 4 etapas

**HubSpot Free é melhor para:**
- Time 5-20 pessoas
- Precisa de automaçêo de email marketing
- Quer crescer para versêo paga depois
- Valoriza interface bonita
- Tem tempo para aprender (1-2 semanas)

**Pipedrive/Agendor sêo ideais para:**
- Time comercial estruturado (3+ vendedores)
- Vendas outbound (cold call intenso)
- Precisa de gamificaçêo (ranking de vendedores)
- Budget de R$200-500/mês é ok
- Quer relatórios visuais sem esforço

**Salesforce só se:**
- Enterprise (50+ funcionários)
- Processos complexos e customizados
- Múltiplas equipes (vendas, CS, suporte)
- Integrações críticas de negócio
- Budget R$5k+/mês + dedicar pessoa para administrar

**Regra de ouro:** Comece simples. Migre quando dor for grande o suficiente. Nêo compre Ferrari para ir ao mercado.

---

## 2. Google Sheets Como CRM

Você vai criar um CRM funcional em 2 horas. Sem instalar nada. Sem cartêo de crédito. Sem curso de 40 horas.

### Template Pronto Para Copiar

**Link do template:** [Copie este Google Sheet](https://docs.google.com/spreadsheets/)

*Nota: Link fictício - você criará seu próprio seguindo as instruções abaixo*

**Estrutura do CRM em Sheets:**

**ABA 1: LEADS (principal)**
**ABA 2: INTERAÇÕES (log de tudo)**
**ABA 3: DASHBOARD (métricas visuais)**
**ABA 4: TEMPLATES (emails/mensagens prontos)**
**ABA 5: CONFIGURAÇÕES (listas suspensas, regras)**

### Colunas Essenciais (Aba LEADS)

Menos é mais. CRM com 40 colunas ninguém preenche. Use apenas o essencial:

**Coluna A: ID do Lead**
```
=ROW()-1
```
Auto-incrementa. Facilita referência ("Vou ligar para o lead #47").

**Coluna B: Data de Entrada**
```
=TODAY()
```
Preenche automaticamente quando linha é criada.

**Coluna C: Nome Completo**
Manual. Obrigatório.

**Coluna D: Email**
Manual. Validaçêo automática:
```
=IF(ISBLANK(D2),"",IF(ISEMAIL(D2),"✅","❌ Email inválido"))
```

**Coluna E: Telefone**
Manual. Formato: (11) 98888-8888

**Coluna F: Empresa**
Manual. Importante para B2B.

**Coluna G: Cargo**
Manual. Ajuda a qualificar.

**Coluna H: Origem**
Lista suspensa:
- LinkedIn
- Indicaçêo
- Website
- Cold outreach
- Evento
- Outro

**Coluna I: Status**
Lista suspensa:
- Novo (sem contato)
- Contactado (aguardando resposta)
- Qualificado (interesse confirmado)
- Proposta enviada
- Negociaçêo
- Fechado - Ganho ✅
- Fechado - Perdido ❌
- Pausado

**Coluna J: Temperatura**
Fórmula automática baseada em último contato:
```
=IF(ISBLANK(M2),"❄️ Frio",
  IF((TODAY()-M2)<=7,"🔥 Quente",
    IF((TODAY()-M2)<=21,"🌤️ Morno",
      "❄️ Frio")))
```

**Coluna K: Valor Estimado**
R$ da oportunidade. Permite prever receita.

**Coluna L: Probabilidade**
% de chance de fechar. Autocompletar baseado em Status:
```
=IF(I2="Novo",10,
  IF(I2="Qualificado",30,
    IF(I2="Proposta enviada",50,
      IF(I2="Negociaçêo",70,
        IF(I2="Fechado - Ganho",100,0)))))
```

**Coluna M: Último Contato**
Data. Atualizada manualmente ou via automaçêo (veremos adiante).

**Coluna N: Próxima Açêo**
Texto livre. O que fazer com esse lead agora?

**Coluna O: Data Próxima Açêo**
Quando fazer a açêo da coluna N.

**Coluna P: Responsável**
Lista suspensa com nomes do time (se aplicável).

**Coluna Q: Observações**
Campo livre. Insights, notas da conversa.

**Coluna R: Receita Ponderada**
Fórmula: Valor × Probabilidade
```
=K2*(L2/100)
```

Permite saber quanto $ "real" tem no pipeline.

### Fórmulas Automáticas

**1. Alertas de Follow-up (Formataçêo Condicional)**

Selecione coluna "Data Próxima Açêo" e aplique regra:
- Vermelho: =O2 < TODAY() (atrasado!)
- Amarelo: =O2 = TODAY() (hoje)
- Verde: =O2 > TODAY() (futuro)

**2. Contagem de Dias Sem Contato**

Nova coluna: "Dias Parado"
```
=IF(ISBLANK(M2),"N/A",TODAY()-M2)
```

Aplique formataçêo:
- Vermelho se >21 dias
- Amarelo se >14 dias

**3. Scoring Automático de Prioridade**

Nova coluna: "Score"
```
=IF(I2="Fechado - Ganho",0,
  IF(I2="Fechado - Perdido",0,
    (L2/10) + IF((TODAY()-M2)>14,-2,0) + IF(K2>50000,3,IF(K2>10000,1,0))
  ))
```

Lógica:
- Base = Probabilidade ÷ 10
- Penaliza leads sem contato recente (-2)
- Prioriza alto valor (+3 se >R$50k, +1 se >R$10k)

Ordene por Score descendente = suas prioridades do dia.

**4. Pipeline Visual**

Na aba DASHBOARD, crie resumo por status:
```
=COUNTIF(LEADS!I:I,"Novo")
=COUNTIF(LEADS!I:I,"Qualificado")
=COUNTIF(LEADS!I:I,"Proposta enviada")
...
```

Adicione gráfico de funil (Insert → Chart → Column chart).

### Integraçêo com Gmail/Calendar

**Enviar email direto do CRM:**

Coluna extra: "Email Rápido"
```
=HYPERLINK("mailto:"&D2&"?subject=Seguindo%20nossa%20conversa&body=Oi%20"&C2,"📧 Enviar email")
```

Clicar abre Gmail com assunto e saudaçêo pré-preenchidos.

**Agendar reuniêo direto do CRM:**

```
=HYPERLINK("https://calendar.google.com/calendar/r/eventedit?text=Reuniêo%20com%20"&C2&"&details=Lead%20ID%20"&A2,"📅 Agendar")
```

**Integraçêo avançada (próxima seçêo):** Quando email é enviado via Gmail, Zapier registra automaticamente na aba INTERAÇÕES.

### Tutorial Completo de Setup (Passo a Passo)

**PASSO 1: Criar planilha base (15min)**

1. Abra Google Sheets
2. Crie nova planilha: "CRM - [Seu Nome/Empresa]"
3. Renomeie abas:
   - Sheet1 → LEADS
   - Sheet2 → INTERAÇÕES
   - Sheet3 → DASHBOARD
   - Sheet4 → TEMPLATES
   - Sheet5 → CONFIG

4. Na aba LEADS, crie headers (linha 1):
   A1: ID | B1: Data Entrada | C1: Nome | D1: Email | E1: Telefone | F1: Empresa | G1: Cargo | H1: Origem | I1: Status | J1: Temperatura | K1: Valor | L1: Probabilidade (%) | M1: Último Contato | N1: Próxima Açêo | O1: Data Próxima Açêo | P1: Responsável | Q1: Observações | R1: Receita Ponderada

5. Formate headers:
   - Negrito
   - Background cinza claro
   - Congelar linha 1 (View → Freeze → 1 row)

**PASSO 2: Configurar listas suspensas (10min)**

1. Na aba CONFIG, crie listas:
   - A1: "Origens" | A2-A7: LinkedIn, Indicaçêo, Website, etc
   - B1: "Status" | B2-B9: Novo, Contactado, Qualificado, etc
   - C1: "Responsáveis" | C2-C5: Nomes do seu time

2. Na aba LEADS, selecione coluna H
3. Data → Data validation
4. Criteria: List from a range → CONFIG!$A$2:$A$7
5. Repita para colunas I (Status) e P (Responsáveis)

**PASSO 3: Adicionar fórmulas (20min)**

1. Coluna A (ID): =ROW()-1
2. Coluna B (Data Entrada): =IF(C2<>"",TODAY(),"")
3. Coluna J (Temperatura): [fórmula descrita acima]
4. Coluna L (Probabilidade): [fórmula descrita acima]
5. Coluna R (Receita Ponderada): =K2*(L2/100)

Selecione linha 2 inteira, copie fórmulas até linha 1000 (Ctrl+C, selecione A2:R1000, Ctrl+V).

**PASSO 4: Formataçêo condicional (15min)**

1. Coluna J (Temperatura):
   - Selecione J2:J1000
   - Format → Conditional formatting
   - Regra 1: Text contains "Frio" → Background azul claro
   - Regra 2: Text contains "Morno" → Background amarelo
   - Regra 3: Text contains "Quente" → Background vermelho claro

2. Coluna O (Data Próxima Açêo):
   - [regras descritas acima]

**PASSO 5: Aba INTERAÇÕES (20min)**

Headers:
A1: ID Interaçêo | B1: Data/Hora | C1: ID Lead | D1: Nome Lead | E1: Tipo | F1: Canal | G1: Assunto | H1: Notas

Tipo (lista): Email enviado, Email recebido, Call, WhatsApp, Reuniêo, Proposta enviada

Coluna D (Nome Lead):
```
=VLOOKUP(C2,LEADS!A:C,3,FALSE)
```

Busca automaticamente nome do lead baseado no ID.

**PASSO 6: Aba DASHBOARD (30min)**

Crie cards de métricas:

**Card 1: Total de Leads Ativos**
```
=COUNTIFS(LEADS!I:I,"<>Fechado - Ganho",LEADS!I:I,"<>Fechado - Perdido")
```

**Card 2: Pipeline Total (R$)**
```
=SUMIF(LEADS!I:I,"<>Fechado - Ganho",LEADS!R:R)
```

**Card 3: Taxa de Conversêo**
```
=COUNTIF(LEADS!I:I,"Fechado - Ganho") / COUNTA(LEADS!C:C)
```
Formate como %.

**Card 4: Tempo Médio de Fechamento**
```
=AVERAGEIF(LEADS!I:I,"Fechado - Ganho",LEADS!M:M-LEADS!B:B)
```

**Tabela de Pipeline por Estágio:**

| Estágio | Qtd Leads | Valor Total |
|---------|-----------|-------------|
| Novo | =COUNTIF(...) | =SUMIF(...) |
| Qualificado | =COUNTIF(...) | =SUMIF(...) |
| ... | ... | ... |

Adicione gráfico de barras empilhadas.

**Gráfico de Funil de Conversêo:**

Insert → Chart → Select Funnel Chart
Data range: Tabela de pipeline

**Gráfico de Leads por Origem:**

```
=QUERY(LEADS!A:H,"SELECT H, COUNT(A) GROUP BY H")
```

Adicione gráfico de pizza.

**PASSO 7: Aba TEMPLATES (10min)**

Crie biblioteca de mensagens prontas:

**Template 1: Email de primeiro contato**
```
Assunto: [Nome], ideia para [Empresa]

Oi [Nome],

[Gancho personalizado baseado em pesquisa]

[Proposta de valor em 2 frases]

Vale 15min na [dia da semana] para conversar?

Abs,
[Seu nome]
```

**Template 2: Follow-up após 3 dias sem resposta**
**Template 3: Email pós-reuniêo**
**Template 4: Proposta enviada**
**Template 5: Negociaçêo**

**PASSO 8: Proteções e compartilhamento (10min)**

1. Proteja aba CONFIG:
   - Right-click aba → Protect sheet
   - Apenas você pode editar

2. Se trabalha em time:
   - Share → Add pessoas
   - Permissêo: Editor
   - Ative histórico de versões (File → Version history)

**PASSO 9: Teste com lead fictício (10min)**

1. Adicione lead teste com todos campos preenchidos
2. Registre interaçêo na aba INTERAÇÕES
3. Verifique se dashboard atualizou automaticamente
4. Teste links de email e calendar

**PASSO 10: Treinamento do time (20min se aplicável)**

1. Grave vídeo de 5min mostrando:
   - Como adicionar lead
   - Como atualizar status
   - Como registrar interaçêo
   - Onde ver próximas ações

2. Sessêo ao vivo: cada pessoa adiciona 1 lead real

**Checklist final:**
- [ ] Todas fórmulas funcionando
- [ ] Listas suspensas configuradas
- [ ] Dashboard mostrando dados corretos
- [ ] Templates de mensagem prontos
- [ ] Time treinado (se aplicável)
- [ ] Backup configurado (Google faz automático)

**Tempo total:** 2h30min

**Resultado:** CRM funcional, grátis, que seu time VAI usar.

---

## 3. Automaçêo de Registro de Interações

Problema: Vendedor envia email, esquece de registrar no CRM. Pipeline fica desatualizado.

Soluçêo: Automaçêo que registra tudo sozinha.

### Email Enviado → Registra no CRM Automaticamente

**Ferramenta:** Zapier (plano free permite 100 tasks/mês)

**Setup:**

**PASSO 1: Criar Zap**

1. Trigger: Gmail - "New Sent Email"
2. Filter: Only continue if... Subject contains "[CRM]"
3. Action: Google Sheets - "Create Spreadsheet Row"

**PASSO 2: Mapear campos**

Spreadsheet: Seu CRM
Worksheet: INTERAÇÕES

Mapeamento:
- Coluna A (ID Interaçêo): Leave blank (formula will fill)
- Coluna B (Data/Hora): {{EmailSentDate}}
- Coluna C (ID Lead): Extract from subject (explained below)
- Coluna E (Tipo): "Email enviado"
- Coluna F (Canal): "Gmail"
- Coluna G (Assunto): {{EmailSubject}}
- Coluna H (Notas): {{EmailBodyPlain}} (primeiros 500 chars)

**PASSO 3: Convençêo de assunto**

Quando enviar email para lead, sempre inclua ID:
"Assunto do email [CRM #47]"

Zapier extrai "47" e registra na coluna ID Lead.

**Formatter:** Use Zapier formatter
- Input: {{EmailSubject}}
- Transform: Extract Pattern
- Pattern: \[CRM #(\d+)\]
- Output: ID do lead

**PASSO 4: Atualizar último contato**

Adicione açêo no Zapier:
Action: Google Sheets - "Update Spreadsheet Row"

Spreadsheet: Seu CRM
Worksheet: LEADS
Lookup Column: A (ID)
Lookup Value: {{extracted_id}}
Update Column: M (Último Contato)
Update Value: {{EmailSentDate}}

**PASSO 5: Testar**

1. Envie email de teste para você mesmo
2. Subject: "Teste automaçêo [CRM #1]"
3. Verifique se apareceu na aba INTERAÇÕES
4. Verifique se "Último Contato" atualizou na aba LEADS

**Taxa de sucesso:** 95%+ (5% falha se esquecer de colocar [CRM #ID])

### Reuniêo → Cria Tarefa de Follow-up

**Trigger:** Google Calendar - "Event Ended"

**Filter:** Event title contains "Cliente:" ou "Lead:"

**Action 1:** Google Sheets - Create Row
Worksheet: INTERAÇÕES
Tipo: "Reuniêo"
Assunto: {{EventTitle}}

**Action 2:** Google Sheets - Create Row
Worksheet: LEADS (ou criar aba TAREFAS)
Próxima Açêo: "Follow-up pós-reuniêo"
Data Próxima Açêo: {{EventEndTime}} + 1 day

**Action 3:** Send Email (opcional)
To: você
Subject: "Follow-up: {{EventTitle}}"
Body: "Lembrete: fazer follow-up com cliente da reuniêo de hoje"

### Proposta Enviada → Alerta de Acompanhamento

**Trigger:** Google Drive - "New File in Folder"
Folder: "Propostas Comerciais 2025"

**Filter:** File name contains "Proposta"

**Action 1:** Google Sheets - Update Row
Worksheet: LEADS
Status: "Proposta enviada"
Probabilidade: 50%
Último Contato: {{FileCreatedTime}}

**Action 2:** Google Sheets - Create Row
Worksheet: TAREFAS
Tarefa: "Acompanhar proposta enviada"
Data: {{FileCreatedTime}} + 3 days
Prioridade: Alta

**Action 3 (após 3 dias):** Delay + Email
Zapier Delay: 3 days
Send Email: "Proposta enviada há 3 dias para [Lead]. Fazer follow-up!"

### Zapier/Make Integration Step-by-Step

**Zapier vs Make (Integromat):**

| Aspecto | Zapier | Make |
|---------|--------|------|
| Facilidade | Mais fácil | Curva aprendizado |
| Plano free | 100 tasks/mês | 1000 ops/mês |
| Preço pago | A partir $20/mês | A partir $9/mês |
| Integrações | 5000+ | 1500+ |
| Visual | Linear | Fluxograma |

**Recomendaçêo:** Comece com Zapier (mais fácil). Se precisar de >100 tasks/mês, migre para Make.

**Tutoria Zapier Completo:**

**1. Criar conta**
- zapier.com
- Sign up (pode usar Google)
- Plano free é suficiente para começar

**2. Conectar Gmail**
- Dashboard → My Apps
- Add Connection → Gmail
- Authorize

**3. Conectar Google Sheets**
- My Apps → Add Connection
- Google Sheets → Select account
- Grant permissions

**4. Criar primeiro Zap: Email → CRM**

Passo 1: Trigger
- Create Zap
- Choose App & Event: Gmail → New Sent Email
- Connect Account
- Test trigger (envia email teste)

Passo 2: Filter
- Add Filter
- Condition: Subject → Contains → [CRM]

Passo 3: Action - Registrar interaçêo
- Choose App: Google Sheets
- Event: Create Spreadsheet Row
- Select Spreadsheet: Seu CRM
- Worksheet: INTERAÇÕES
- Map fields (descriçêo acima)
- Test action

Passo 4: Action - Atualizar último contato
- Add Action
- App: Google Sheets
- Event: Update Spreadsheet Row
- Worksheet: LEADS
- Lookup Column: A (ID)
- Lookup Value: Use Formatter para extrair ID do subject
- Update M (Último Contato) com data atual

Passo 5: Publish
- Turn on Zap
- Name it: "Email → CRM Auto"

**5. Criar segundo Zap: Calendar → Follow-up**

[Seguir mesma estrutura]

**6. Monitorar Zaps**

- Dashboard → Zap History
- Veja tasks rodando
- Debug erros (se houver)

**Erros comuns:**

**Erro: "Could not find row"**
Soluçêo: Verifica se ID do lead existe na aba LEADS

**Erro: "Missing required field"**
Soluçêo: Mapear todos campos obrigatórios do Sheets

**Erro: "Trigger nêo dispara"**
Soluçêo: Conferir filtro. Teste com dados que atendem condiçêo

**Limite de 100 tasks/mês:**
- 1 email registrado = 2 tasks (1 criar interaçêo + 1 atualizar lead)
- ~50 emails/mês cabem no free
- Se precisar de mais: Make ou pagar Zapier

**Make (alternativa mais barata):**

Setup similar, mas interface visual de fluxograma.

**Vantagem:** 1000 operações/mês free (10x mais que Zapier)

**Desvantagem:** Curva de aprendizado maior

**Tutorial Make:**
1. make.com → Create account
2. Create Scenario
3. Add módulo: Gmail → Watch sent emails
4. Add módulo: Google Sheets → Add a row
5. Connect com linha

---

## 4. Dashboard de Vendas Automático

Dashboard que você nêo precisa atualizar. Acorda, abre, vê métricas atualizadas.

### Métricas Que Importam

**Métrica 1: Leads Novos (Esta Semana)**
```
=COUNTIFS(LEADS!B:B,">="&TODAY()-7,LEADS!B:B,"<="&TODAY())
```

**Métrica 2: Taxa de Conversêo**
```
=COUNTIF(LEADS!I:I,"Fechado - Ganho") / COUNTA(LEADS!C:C) * 100
```

**Métrica 3: Pipeline Total (R$)**
```
=SUMIF(LEADS!I:I,"<>Fechado - Perdido",LEADS!K:K)
```

**Métrica 4: Pipeline Ponderado (R$)**
```
=SUMIFS(LEADS!R:R,LEADS!I:I,"<>Fechado - Ganho",LEADS!I:I,"<>Fechado - Perdido")
```

Diferença entre Total e Ponderado = realismo. Se total é R$500k mas ponderado é R$150k, você fecha ~R$150k.

**Métrica 5: Ticket Médio**
```
=AVERAGE(FILTER(LEADS!K:K,LEADS!I:I="Fechado - Ganho"))
```

**Métrica 6: Ciclo de Venda Médio (Dias)**
```
=AVERAGEIF(LEADS!I:I,"Fechado - Ganho",(LEADS!M:M-LEADS!B:B))
```

**Métrica 7: Leads em Risco**

Leads que:
- Status <> Fechado
- Último contato > 14 dias

```
=COUNTIFS(LEADS!I:I,"<>Fechado - Ganho",LEADS!I:I,"<>Fechado - Perdido",LEADS!M:M,"<"&TODAY()-14)
```

**Métrica 8: Previsêo de Receita (Este Mês)**

Soma dos leads com:
- Probabilidade > 50%
- Data próxima açêo < fim do mês

```
=SUMIFS(LEADS!R:R,LEADS!L:L,">50",LEADS!O:O,"<"&EOMONTH(TODAY(),0))
```

### Gráficos Automáticos no Sheets

**Gráfico 1: Funil de Conversêo**

Dados:
```
| Estágio | Quantidade |
|---------|------------|
| Leads Novos | =COUNTIF(LEADS!I:I,"Novo") |
| Qualificados | =COUNTIF(LEADS!I:I,"Qualificado") |
| Proposta | =COUNTIF(LEADS!I:I,"Proposta enviada") |
| Negociaçêo | =COUNTIF(LEADS!I:I,"Negociaçêo") |
| Fechado | =COUNTIF(LEADS!I:I,"Fechado - Ganho") |
```

Insert → Chart → Funnel Chart

**Gráfico 2: Evoluçêo de Leads (Últimos 30 Dias)**

Dados:
```
=QUERY(LEADS!A:B,"SELECT B, COUNT(A) WHERE B >= date '"&TEXT(TODAY()-30,"yyyy-mm-dd")&"' GROUP BY B ORDER BY B")
```

Insert → Chart → Line Chart

**Gráfico 3: Origem dos Leads (Pizza)**

```
=QUERY(LEADS!H:H,"SELECT H, COUNT(H) GROUP BY H")
```

Insert → Chart → Pie Chart

**Gráfico 4: Performance por Responsável**

```
=QUERY(LEADS!P:P&I:I,"SELECT P, COUNTIF(I,'Fechado - Ganho'), COUNTIF(I,'Fechado - Perdido') GROUP BY P")
```

Insert → Chart → Stacked Column

**Dica:** Configure gráficos para atualizar automaticamente:
Chart editor → Setup → Data range → Intervalo dinâmico (A:Z)

### Relatório Semanal Por Email

**Zapier Automation:**

**Trigger:** Schedule by Zapier
- Frequency: Weekly
- Day: Monday
- Time: 8:00 AM

**Action 1:** Google Sheets - Lookup Spreadsheet Rows
- Spreadsheet: Seu CRM
- Worksheet: DASHBOARD
- Lookup Column: A (nome da métrica)
- Lookup Value: "Leads Novos Semana"

**Action 2:** Formatter
- Transform: Create variable for each metric

**Action 3:** Gmail - Send Email
- To: você (ou time)
- Subject: "Relatório Semanal - CRM [{{current_date}}]"
- Body:
```
Oi time!

Resumo da semana passada:

📊 Leads Novos: {{leads_novos}}
💰 Pipeline Total: R$ {{pipeline_total}}
✅ Fechamentos: {{fechamentos}}
📈 Taxa de Conversêo: {{taxa_conversao}}%

Leads em risco (>14 dias sem contato): {{leads_risco}}

Açêo: Priorizar follow-up dos leads em risco hoje!

Dashboard completo: [link do Google Sheet]

Bora fechar negócios! 🚀
```

**Frequência ideal:**
- Diária: Só se você faz 10+ vendas/dia (muito dinâmico)
- Semanal: Maioria dos casos (B2B, consultoria)
- Mensal: Vendas de alto ticket (ciclo longo)

### Template Pronto

**Checklist do Dashboard:**

✅ Cards de métricas no topo (visêo geral em 5 segundos)
✅ Gráfico de funil de conversêo
✅ Gráfico de evoluçêo temporal (últimos 30/90 dias)
✅ Tabela de leads em risco (action items)
✅ Performance por origem/responsável
✅ Previsêo de fechamentos do mês
✅ Comparativo: Mês atual vs mês passado

**Layout sugerido:**

```
+------------------------+------------------------+
| 📊 Leads Ativos: 47    | 💰 Pipeline: R$ 380k  |
+------------------------+------------------------+
| ✅ Taxa Conv: 28%      | 📅 Ciclo: 21 dias      |
+------------------------+------------------------+

+------------------------------------------------+
|        FUNIL DE CONVERSêO (gráfico)            |
+------------------------------------------------+

+------------------------------------------------+
|    EVOLUÇêO DE LEADS - 30 DIAS (linha)        |
+------------------------------------------------+

+------------------------------------------------+
| LEADS EM RISCO                                 |
| Nome | Dias Parado | Valor | Próxima Açêo      |
+------------------------------------------------+

+------------------------------------------------+
| ORIGEM DOS LEADS (pizza) | PERFORMANCE (barras)|
+------------------------------------------------+
```

---

## 5. CRMs Gratuitos Recomendados

Se Google Sheets nêo é suficiente (você tem >20 leads/semana ou time >5 pessoas), considere:

### HubSpot Free: Prós/Contras

**Prós:**
✅ Grátis para sempre (nêo é trial)
✅ Interface bonita e intuitiva
✅ Email marketing incluso (2.000 envios/mês)
✅ Automações básicas
✅ Mobile app excelente
✅ Integra com Gmail/Outlook
✅ Suporte por chat (limitado)
✅ Escala para pago quando crescer (plano coerente)

**Contras:**
❌ Branding HubSpot em emails (remove só no pago)
❌ Limite de 1 milhêo de contatos (ok para 99% dos casos)
❌ Relatórios customizados só no pago
❌ Curva de aprendizado (1-2 semanas)
❌ Features avançadas tentam te empurrar para pago

**Para quem é ideal:**
- Startups que querem crescer
- Empresas que fazem email marketing + vendas
- Times que valorizam UX
- Quem pode investir tempo em setup inicial

**Setup time:** 4-8 horas (incluindo importaçêo de contatos, configuraçêo de pipeline)

**Case:** Agência de marketing digital migrou de Planilha para HubSpot Free. Motivo: precisavam de automaçêo de email + CRM integrado. Resultado: Taxa de resposta de cold email subiu 40% (sequências automatizadas).

### Pipedrive Trial: Quando Usar

**Prós:**
✅ Interface focada em VENDAS (nêo marketing)
✅ Gamificaçêo (ranking de vendedores)
✅ Visualizaçêo em Kanban (arrasta e solta)
✅ Relatórios visuais excelentes
✅ Integrações com tudo (WhatsApp, Calendly, etc)
✅ Mobile app robusto
✅ Suporte em PT-BR

**Contras:**
❌ Nêo tem versêo free (só trial 14 dias)
❌ Plano mais barato: ~R$60/usuário/mês
❌ Email marketing separado (custo extra)
❌ Nêo ideal para solo (mínimo 2-3 usuários pra valer)

**Para quem é ideal:**
- Times comerciais estruturados (3+ vendedores)
- Vendas outbound (cold call intenso)
- Gestores que precisam acompanhar performance do time
- Empresas que podem pagar R$200-300/mês

**Setup time:** 2-3 horas

**Dica:** Use trial de 14 dias para testar SE vale a pena pagar. Nêo assine antes de testar com dados reais.

**Case:** Distribuidora B2B com 5 vendedores. Tentou Sheets, bagunçou (cada um tinha própria planilha). Pipedrive centralizou, criou competiçêo saudável (ranking visível). Vendas subiram 25% em 3 meses.

### Notion Database: Para Criativos

**Prós:**
✅ Flexível demais (você molda do seu jeito)
✅ Conecta CRM com projetos, docs, wikis
✅ Interface linda
✅ Colaboraçêo em tempo real
✅ Versêo free robusta
✅ Templates prontos de CRM

**Contras:**
❌ Nêo é CRM nativo (você cria do zero)
❌ Automações limitadas (precisa de Zapier)
❌ Curva de aprendizado alta
❌ Nêo tem funil visual nativo
❌ Relatórios manuais

**Para quem é ideal:**
- Freelancers/consultores que querem tudo em um app
- Criativos que odeiam ferramentas "engessadas"
- Quem já usa Notion para tudo
- Projetos + vendas no mesmo lugar

**Setup time:** 3-5 horas (customizaçêo infinita = tempo infinito)

**Dica:** Comece com template pronto (busque "CRM Notion template" no Google).

**Case:** Designer freelancer usava Trello + Sheets + Google Docs. Migrou tudo para Notion. CRM virou aba do workspace principal. Economia de tempo: 4h/semana (nêo precisa alternar entre apps).

### Comparaçêo Rápida

| Critério | Google Sheets | HubSpot Free | Pipedrive | Notion |
|----------|---------------|--------------|-----------|--------|
| **Custo** | R$ 0 | R$ 0 | R$ 180/mês | R$ 0 |
| **Setup** | 2h | 6h | 3h | 4h |
| **Curva aprendizado** | Baixa | Média | Baixa | Alta |
| **Ideal para** | 1-10 leads/sem | Crescimento | Time vendas | Criativos |
| **Automaçêo** | Via Zapier | Nativa básica | Nativa completa | Via Zapier |
| **Mobile** | App Sheets | App nativo | App nativo | App nativo |
| **Email integrado** | Nêo | Sim | Nêo (pago) | Nêo |
| **Relatórios** | Manual | Básicos | Completos | Manual |

**Decisêo:**

- **Começando do zero?** Google Sheets
- **Precisa escalar rápido?** HubSpot Free
- **Time comercial estruturado?** Pipedrive
- **Quer tudo em um app?** Notion

**Migraçêo:** Nêo tenha medo de começar simples e migrar depois. Melhor usar Sheets hoje do que ficar 2 meses "escolhendo CRM" e nêo usar nada.

---

## 6. Exercícios + Implementaçêo

### Exercício 1: Monte Seu CRM em 2 Horas (120min)

**Objetivo:** Sair deste módulo com CRM funcionando.

**Instruções:**
1. Siga tutorial passo a passo da seçêo 2
2. Crie planilha completa (5 abas)
3. Configure todas fórmulas
4. Adicione 5 leads reais (ou fictícios)
5. Registre 2 interações por lead
6. Verifique se dashboard atualizou

**Checklist final:**
- [ ] Aba LEADS com 5 leads
- [ ] Aba INTERAÇÕES com 10 registros
- [ ] Aba DASHBOARD mostrando métricas
- [ ] Listas suspensas funcionando
- [ ] Fórmulas calculando corretamente
- [ ] Link de "enviar email" abrindo Gmail

**Entrega:** Link do Google Sheet (compartilhe para visualizaçêo)

### Exercício 2: Primeira Automaçêo (30min)

**Objetivo:** Configurar 1 Zap funcionando.

**Instruções:**
1. Crie conta no Zapier (free)
2. Configure Zap: Gmail → Google Sheets
3. Envie 1 email teste com [CRM #1] no assunto
4. Verifique se apareceu na aba INTERAÇÕES
5. Debug se nêo funcionou

**Checklist:**
- [ ] Zapier conectado ao Gmail
- [ ] Zapier conectado ao Google Sheets
- [ ] Zap "ON"
- [ ] Email teste registrado automaticamente
- [ ] "Último Contato" atualizado na aba LEADS

### Exercício 3: Dashboard Personalizado (45min)

**Objetivo:** Criar 1 métrica e 1 gráfico relevante pro SEU negócio.

**Exemplo 1:** Se você vende consultoria mensal:
- Métrica: "Receita Recorrente Prevista (MRR)"
- Gráfico: Evoluçêo do MRR por mês

**Exemplo 2:** Se você vende projetos pontuais:
- Métrica: "Ticket Médio por Origem"
- Gráfico: Qual origem traz projetos maiores

**Instruções:**
1. Identifique métrica que você olha todo dia
2. Crie fórmula no DASHBOARD
3. Adicione gráfico visual
4. Formate (cores, labels)

**Entrega:** Screenshot do dashboard com sua métrica

### Exercício 4: Teste de Uso Real (1 semana)

**Objetivo:** Validar se CRM funciona no dia-a-dia.

**Desafio:**
- Use CRM durante 1 semana completa
- Adicione TODO lead novo
- Registre TODA interaçêo
- Atualize status diariamente
- Ao final da semana, responda:

**Perguntas:**
1. Consegui usar todos os dias? Se nêo, o que bloqueou?
2. Alguma coluna que nunca preenchi? (Elimine)
3. Falta alguma informaçêo importante? (Adicione)
4. Quanto tempo/dia gastei atualizando? (Meta: <10min)
5. Dashboard me deu insights úteis?

**Ajustes:**
- Simplifique se está complexo
- Adicione colunas se falta info crítica
- Configure mais automações se gastar >10min/dia

### Exercício 5: Treinamento do Time (se aplicável)

**Objetivo:** Garantir que todo mundo use.

**Instruções:**
1. Grave vídeo loom de 5min mostrando:
   - Como adicionar lead
   - Como registrar interaçêo
   - Onde ver próximas ações
   - Como atualizar status

2. Agende 30min com time:
   - Mostre vídeo
   - Cada pessoa adiciona 1 lead real
   - Cada pessoa registra 1 interaçêo
   - Tire dúvidas

3. Primeira semana: Acompanhe adoçêo
   - Segunda: "Pessoal, vamos usar CRM hoje!"
   - Quarta: "Quem ainda nêo adicionou leads?"
   - Sexta: Revise juntos, celebre quem usou

**Meta:** 80%+ de adoçêo em 2 semanas.

### Exercício Bônus: Relatório Automático

**Objetivo:** Acordar segunda recebendo email com métricas.

**Instruções:**
1. Configure Zap de relatório semanal (seçêo 4)
2. Personalize email com métricas do SEU negócio
3. Teste (force trigger manual)
4. Ajuste copy do email

**Template de email:**
```
Subject: CRM - Semana de [data]

Oi [nome],

Dashboard da semana:

🎯 Leads Novos: X
💼 Propostas Enviadas: Y
✅ Fechamentos: Z
💰 Receita: R$ W

🚨 AÇêO NECESSÁRIA:
- [Lead Nome] está há 21 dias sem contato
- [Lead Nome] recebeu proposta há 5 dias (follow-up!)

Ver detalhes: [link CRM]

Boa semana de vendas!
```

---

## Resumo do Módulo

**O que você aprendeu:**

1. **CRM nêo precisa ser complexo** - Sheets resolve 90% dos casos
2. **Setup em 2h** - Template completo com fórmulas e automações
3. **Automaçêo economiza tempo** - Email/reuniêo registra sozinho
4. **Dashboard automático** - Métricas sempre atualizadas
5. **Alternativas gratuitas** - HubSpot, Notion quando Sheets nêo basta

**Próximos passos:**

1. Monte seu CRM HOJE (use exercício 1)
2. Configure 1 automaçêo esta semana
3. Use durante 7 dias
4. Ajuste o que nêo funcionar
5. Escale (time, automações, integrações)

**Mindset para levar:**

CRM perfeito nêo existe. CRM que você USA é melhor que CRM complexo que fica abandonado.

Comece simples. Melhore com uso.

**Próximo módulo:** Follow-up que Nunca Falha - Como garantir que nenhum lead cai no esquecimento.

---

**Recursos adicionais:**

- Template Google Sheets CRM (copiar)
- Vídeo: "Setup completo em 2h"
- Zapier templates prontos (importar)
- Checklist de adoçêo de CRM

**Comunidade:**

Compartilhe seu CRM com o grupo:
- Mostre seu dashboard
- Que automaçêo você criou?
- Que métrica te surpreendeu?

Gestêo nêo precisa ser chata. Pode ser simples e funcionar.

Vamos implementar!
