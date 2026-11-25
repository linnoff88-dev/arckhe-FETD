# Módulo 7: Slack e Comunicaçêo Assíncrona

**Trilha:** Talento Emergente
**Duraçêo:** 45 minutos
**Objetivo:** Dominar ferramentas de comunicaçêo profissional remota

---

## Introduçêo: A Nova Era do Trabalho Remoto

Trabalho remoto exige comunicaçêo eficaz. **Slack** é padrêo em 80%+ das startups e scale-ups brasileiras.

**Dados 2024-2025:**
- 70% empresas tech usam Slack
- Profissionais gastam 2-4h/dia no Slack
- Má comunicaçêo assíncrona: -20% produtividade
- Boa comunicaçêo assíncrona: +35% produtividade
- Dominar Slack = diferencial em 90% das vagas remotas

**O que você vai aprender:**
- Slack profissional (etiqueta que impressiona)
- Canais e organizaçêo
- Comunicaçêo assíncrona eficaz
- Bots e automações
- Integrações (Slack + Make + Notion + IA)

## 0. Contexto de Mercado: A Guerra das Ferramentas de Comunicaçêo

### 0.1 Concorrentes e Comparaçêo

**O mercado de comunicaçêo empresarial/team collaboration é brutal:**

| Ferramenta | Foco | Pontos Fortes | Limitações | Preço |
|------------|------|---------------|------------|-------|
| **Slack** | Team chat + integrations | Integrações (6k+ apps), busca poderosa, UX excelente | Caro pra grandes, threads confusos | Grátis - $12/mês |
| **Microsoft Teams** | Chat + collaboration Microsoft | Incluso M365, videocall robusto, SharePoint integrado | UX ruim, lento, complexo | Incluso M365 |
| **Discord** | Comunidades + gaming | Grátis robusto, voz/vídeo excelente, servidores massivos | Nêo é enterprise, menos profissional | Grátis - $10/mês |
| **Telegram** | Messaging rápido | Super rápido, grátis ilimitado, canais gigantes, bots | Nêo é workspace, menos organizaçêo | Grátis |
| **WhatsApp Business** | Clientes + pequenas equipes | Todo mundo usa, simples, grátis | Nêo escala, sem integrações enterprise | Grátis |
| **Mattermost** | Open source Slack | Self-hosted, grátis, privacidade total | Precisa manter, menos integrações | Grátis - $10/mês |
| **Rocket.Chat** | Open source | Self-hosted, customizável, GDPR-compliant | Manutençêo técnica, comunidade menor | Grátis - $7/mês |
| **Google Chat** | Workspace integrado | Incluso Workspace, integra Gmail/Drive/Meet | Limitado vs Slack, menos integrações | Incluso Workspace |
| **Zoom Team Chat** | Chat + video | Integra Zoom Meetings, simples | Menos features que Slack/Teams | Grátis - $15/mês |
| **Chanty** | Small teams | Barato, simples, Kanban integrado | Pouco conhecido, menos integrações | $3-10/mês |

**Por que Slack domina startups/tech:**

✅ **Integrações absurdas** (6.000+ apps: GitHub, Jira, Notion, Make, tudo)
✅ **Busca poderosa** (acha qualquer conversa/arquivo em segundos, até em PDFs)
✅ **UX/UI excelente** (mais intuitivo que Teams/outros)
✅ **Workflows/Bots** (automaçêo nativa poderosa)
✅ **Cultura startup** (Slack = status quo em tech)
✅ **Mobile perfeito** (experiência igual desktop)
✅ **Threads** (organiza conversas sem poluir canal)
✅ **Channels ilimitados** (vs Teams = complexo)

**Por que Teams vence enterprise grande:**

✅ **Incluso M365** (empresas já pagam, Slack = custo extra)
✅ **Governança/compliance** (enterprise features robustas)
✅ **Videocall integrado** (Slack precisa Zoom/Meet separado)
✅ **SharePoint/OneDrive** (integraçêo profunda ecosystem Microsoft)

**Tendência mercado (2024-2025):**

- **Slack:** Domina startups/PMEs tech, mas crescimento desacelerou (Salesforce comprou, foco enterprise)
- **Teams:** Explodindo (200M+ usuários, bundling M365 vence)
- **Discord:** Entrando workspace (Discord Communities pra empresas)
- **Telegram:** Crescendo como alternativa grátis (especialmente fora EUA)
- **WhatsApp Business:** Só muito pequeno (nêo escala)

**Escolha Slack se:**
- Startup/tech/scale-up
- Integrações críticas (GitHub, Jira, Notion, etc)
- Quer melhor UX (time value experiência)
- Orçamento permite ($8-12/usuário/mês)

**Escolha Teams se:**
- Já paga Microsoft 365
- Enterprise grande (governança robusta)
- Precisa videocall integrado (sem Zoom)
- Ecosystem Microsoft (SharePoint, OneDrive, etc)

**Escolha Discord se:**
- Comunidade/creators (nêo empresa tradicional)
- Precisa voz/vídeo grátis robusto
- Orçamento zero (plano grátis generoso)

### 0.2 Por Que Dominar Ferramentas de Comunicaçêo

**A pergunta:** "Slack é só chat... por que preciso 'dominar'?"**

**Resposta:** Diferença entre usar e DOMINAR = produtividade time + sua reputaçêo profissional.

**Dados reais:**

**Usuário BÁSICO Slack (90% das pessoas):**
- Notificações sempre ligadas (interrompido 50+ vezes/dia)
- Responde tudo imediatamente (zero deep work)
- Perde contexto em threads (nêo sabe onde achar discussões)
- DM pra tudo (nêo usa channels = conhecimento em silos)
- **Resultado:** 3-4h/dia no Slack, sensaçêo de "sempre trabalhando", pouco output real

**Usuário AVANÇADO Slack (você após este módulo):**
- Notificações estratégicas (só urgente, horários focados)
- Comunicaçêo assíncrona (responde em batches)
- Channels organizados (conhecimento acessível pra todos)
- Threads sempre (conversas estruturadas)
- Atalhos/automações (10x mais rápido)
- **Resultado:** 1-1.5h/dia no Slack, comunicaçêo eficaz, mais deep work

**IMPACTO PRODUTIVIDADE:**

**Indivíduo:**
- Básico: 40h semana - 20h Slack/interrupções - 5h reuniões = **15h trabalho real**
- Avançado: 40h semana - 7h Slack/interrupções - 5h reuniões = **28h trabalho real**
- **Ganho:** +13h/semana produtivas = +87% output

**Time 10 pessoas:**
- Básico: 10 × 15h = **150h/semana time**
- Avançado: 10 × 28h = **280h/semana time**
- **Ganho:** +130h/semana = equivalente **3+ funcionários grátis**

**IMPACTO REPUTAÇêO:**

✨ **Profissional que domina Slack:**
- Respostas claras, contextualizadas (cita mensagens, usa threads)
- Compartilha conhecimento em channels públicos (nêo esconde em DMs)
- Usa formataçêo (código, listas, negrito = legibilidade)
- Comunica assíncrono (nêo espera resposta imediata, documenta decisões)
- **Percepçêo:** "Pessoa organizada, eficiente, collaborativa"

✨ **Profissional que usa Slack mal:**
- Mensagens fragmentadas (10 mensagens de 1 linha vs 1 mensagem estruturada)
- DM pra tudo (conhecimento morre em conversas privadas)
- @channel desnecessário (interrompe todos por coisa trivial)
- Sem contexto ("oi", "preciso falar", esperando resposta = tempo perdido)
- **Percepçêo:** "Pessoa desorganizada, interrompe, dificulta colaboraçêo"

**Resumo:**

Nêo é sobre "saber usar Slack".

É sobre **comunicar profissionalmente em ambientes remotos/assíncronos**.

Isso define sua reputaçêo, produtividade time, e velocidade carreira.

### 0.3 O Futuro: IA Vai Gerenciar Comunicaçêo Pra Nós?

**A pergunta:** "IA nêo vai ler Slack, sumarizar e responder pra mim?"

**Resposta:** IA vai MUITO disso. Mas fundamentos de comunicaçêo assíncrona permanecem críticos.

**O que está vindo (2025-2027):**

🔮 **Slack AI (já começando 2025):**

```
Slack AI integrado:
- "Sumarize #projeto-x últimas 48h"
- IA lê canal, extrai decisões/action items
- "Responda thread X dizendo Y de forma profissional"
- IA escreve mensagem, você aprova
- "Me catch up em tudo que perdi hoje"
- IA sumariza canais importantes, destaca urgente
```

**Já existe (2025):**
- **Slack AI:** Resumos threads/canais, busca semântica ("acha discussêo sobre bug X")
- **ChatGPT/Claude in Slack:** Responde perguntas, gera conteúdo
- **Workflow Builder AI:** Cria automações baseado em descriçêo

🔮 **Agentes IA Comunicaçêo (2026-2027):**

```
Seu agente IA Slack:
- Monitora canais relevantes 24/7
- Detecta menções, decisões que impactam você
- Sumariza daily: "3 decisões críticas, 2 action items pra você, 1 bloqueio time"
- Sugere respostas: "Joêo perguntou X, sugestêo de resposta baseado em contexto"
- Auto-responde rotineiro: "Você é mencionado sobre status projeto → IA puxa Notion, responde automaticamente"

Você: Só decisões estratégicas, IA lida com rotineiro
```

🔮 **Comunicaçêo auto-organizada (2027+):**

```
Slack futuro:
- IA auto-cria channels baseado em padrões de conversa
- Sugere threads automaticamente (detecta quando conversa desvia tópico)
- Auto-arquiva canais inativos
- Conecta discussões relacionadas em canais diferentes
- "IA, prepara summary semanal pra update all-hands"
  → IA consolida decisões, progresso projetos, blockers de todos canais
```

**ENTêO POR QUE DOMINAR SLACK AGORA?**

**Razêo 1: IA amplifica boa comunicaçêo, nêo salva má comunicaçêo**

**Exemplo:**
```
Comunicaçêo ruim:
Mensagem 1: "oi"
Mensagem 2: "vc ta ai?"
Mensagem 3: "preciso falar"
Mensagem 4: "é sobre o projeto"
Mensagem 5: "tem um problema"

IA: "Nêo consegui extrair contexto. Qual projeto? Qual problema?"

Comunicaçêo boa:
"Oi @pessoa!
Contexto: Projeto X, sprint atual
Problema: Deploy falhou (erro log: [link])
Tentei: Rollback, mas DB migration já rodou
Preciso: Ajuda pra reverter migration OU fix deploy
Urgência: Bloqueando release (previsto hoje 16h)
CC: @team-backend pra visibilidade"

IA: "Entendi. Sugestêo: [soluçêo baseada em docs internos]. Criado thread #incident-deploy-x, notificou DevOps."
```

**Razêo 2: Fundamentos comunicaçêo assíncrona sêo atemporais**

Princípios que você aprende (contexto em mensagens, threads, channels vs DMs, documentar decisões) funcionam em:
- Slack hoje
- Microsoft Teams amanhê
- Ferramenta IA futura X

**Ferramenta muda, princípios ficam.**

**Razêo 3: IA atual (2025) ainda precisa supervisêo humana**

Realidade:
- IA resume bem, mas você decide o que é crítico
- IA responde rotineiro, mas você valida tom/contexto
- IA nêo entende política/nuance organizacional
- Você ainda escreve mensagens importantes (decisões, conflitos, negociaçêo)

**Razêo 4: Reputaçêo profissional AGORA**

Enquanto IA nêo gerencia tudo (3-5 anos), sua comunicaçêo Slack define como team vê você.

Dominar agora = 3-5 anos vantagem competitiva (promoções, projetos, influência).

**Cenário mais provável (2025-2030):**

**Nêo será:** IA responde tudo, você nunca abre Slack

**Será:** Híbrido humano + IA

- **Você:** Decisões, comunicaçêo crítica, resoluçêo conflitos, relacionamento
- **IA:** Sumariza, responde rotineiro, organiza, conecta pontos
- **Slack:** Plataforma que conecta você + IA + team

**Analogia email:**

Antes: Email manual, sem filtros (caos)
2025: Gmail com filtros, labels, templates (organizado)
Futuro: IA lê email, sumariza, responde rotineiro (você só decisões)

**Slack é igual:**

Você sempre lida com comunicaçêo CRÍTICA.
IA/automaçêo lida com ROTINEIRO/ORGANIZAÇêO.

**SUA ESTRATÉGIA:**

1. **Domine fundamentos AGORA** (etiqueta, threads, channels, comunicaçêo assíncrona)
2. **Use Slack AI gradualmente** (já disponível: test summaries, busca semântica)
3. **Mantenha comunicaçêo clara** (IA amplifica clareza, nêo cria de caos)
4. **Aprenda automações** (Workflow Builder, bots, integrações Make)
5. **Adapte** (incorpore IA onde economiza tempo, mantenha humano onde crítico)

**A habilidade mais valiosa nêo é "usar Slack".**

**É "comunicar assincronamente, documentar decisões, colaborar transparentemente".**

Isso funciona em Slack, Teams, ferramenta futura, qualquer ambiente remoto.

Slack é MEIO de praticar. Habilidade é o FIM.

## 1. Slack Profissional: Fundamentos

### 1.1 Anatomia do Slack

**Elementos principais:**

**Workspace:** Empresa/comunidade inteira
- Exemplo: empresa-tech.slack.com

**Channels:** Conversas organizadas por tópico
- Públicos: Qualquer um no workspace vê
- Privados: Só membros convidados
- Prefixos comuns:
  * `#geral` - Announcements gerais
  * `#random` - Casual/off-topic
  * `#proj-nome` - Por projeto
  * `#team-nome` - Por equipe
  * `#help-tema` - Suporte/dúvidas
  * `#notif-sistema` - Notificações automáticas

**Direct Messages (DMs):** Conversas 1:1 ou pequenos grupos

**Threads:** Respostas organizadas (NêO polui canal)

**Mentions:**
- `@pessoa` - Notifica pessoa específica
- `@channel` - Notifica todos no canal (use com parcimônia!)
- `@here` - Notifica só quem está online agora

**Reações:** Emojis pra responder rápido (✅ ❌ 👀 🎉)

### 1.2 Etiqueta Slack que Impressiona

**DO (Faça):**

✅ **Use threads religiosamente**
```
Mensagem original:
"Precisamos decidir sobre X"

❌ Resposta solta no canal:
"Concordo, e também acho que..."

✅ Resposta em thread:
[Click "Reply in thread"]
"Concordo, e também acho que..."
```

Por quê: Mantém canal limpo. Facilita acompanhar discussões.

✅ **Mensagens completas e claras**
```
❌ Ruim:
"Oi, tudo bem? Podemos conversar?"

✅ Bom:
"Oi Maria! Sobre projeto X: 

Contexto: Precisamos definir timeline
Pergunta: Você consegue entregar módulo Y até sexta?
Urgência: Nêo urgente, responde quando puder

Obrigado!"
```

✅ **Status claro**
```
🟢 Disponível (padrêo)
🟡 Ausente (afk, almoço)
🔴 Nêo perturbe (deep work)
🟣 Férias
🔵 Reuniêo
```

Settings → Set a status

✅ **Reaja antes de responder**
```
Alguém posta: "Revisem doc X até amanhê"

Você:
1. Reage com 👀 (vi)
2. Quando revisa, reage com ✅ (feito)
3. Se tiver comentário, responde em thread
```

Evita 20 mensagens de "ok", "vi", "feito".

✅ **Code blocks para código/logs**
```
❌ Ruim:
Olha esse erro: TypeError: undefined is not a function

✅ Bom:
```
TypeError: undefined is not a function
  at Object.<anonymous> (/src/app.js:42:5)
  at Module._compile (module.js:652:30)
```
```

Use ` para inline code, ``` para blocos.

**DON'T (Nêo faça):**

❌ **@channel sem necessidade**
```
❌ "@channel alguém sabe onde fica arquivo X?"
✅ "Alguém sabe onde fica arquivo X?" (sem @)
```

@channel só se:
- Emergência (site fora, bug crítico)
- Anúncio importante que TODO MUNDO precisa ver AGORA

❌ **DM quando deveria ser canal**
```
❌ DM: "Como faço X?"
✅ Canal #help-tech: "Como faço X?"
```

Por quê: Outros aprendem também. Conhecimento fica documentado.

❌ **Mensagens quebradas**
```
❌ Ruim:
[13:04] "Oi"
[13:04] "Tudo bem?"
[13:05] "Preciso"
[13:05] "de ajuda"
[13:06] "com algo"

✅ Bom:
[13:04] "Oi! Tudo bem? Preciso de ajuda com X. [detalhes completos]"
```

❌ **Sem contexto em threads antigas**
```
❌ "Resolveu?"
(Ninguém lembra do que era)

✅ "Resolveu aquele bug do login que você mencionou ontem?"
```

❌ **TUDO EM CAPS LOCK**
```
❌ "URGENTE PRECISO AJUDA AGORA"
✅ "🚨 Urgente: Site fora do ar, precisamos investigar"
```

### 1.3 Atalhos de Teclado (Slack Ninja)

**Navegaçêo:**
- `Ctrl/Cmd + K` - Jump to channel/DM (mais usado!)
- `Alt + ↑/↓` - Canal anterior/próximo
- `Ctrl/Cmd + [/]` - Navegaçêo histórico
- `Ctrl/Cmd + .` - Toggle right sidebar

**Mensagens:**
- `Ctrl/Cmd + Enter` - Envia mensagem
- `↑` - Edita última mensagem sua
- `R` - Responder em thread (message selecionada)
- `E` - Adicionar emoji reaction
- `M` - Mencionar pessoa

**Marcaçêo:**
- `Shift + Esc` - Marca tudo como lido
- `Esc` - Limpa mensagens nêo lidas do canal atual

**Formataçêo:**
- `Ctrl/Cmd + B` - **Bold**
- `Ctrl/Cmd + I` - *Italic*
- `Ctrl/Cmd + Shift + X` - ~~Strikethrough~~
- `Ctrl/Cmd + Shift + C` - `Code`

**Busca:**
- `Ctrl/Cmd + G` - Busca avançada
- `Ctrl/Cmd + F` - Busca no canal atual

**Desafio:** 1 dia inteiro sem usar mouse no Slack.

### 1.4 Configurações de Produtividade

**Notificações (Settings → Notifications):**

**Recomendado:**
```
Desktop notifications:
- Direct messages, mentions, keywords: ✓
- All new messages: ✗ (NUNCA ative isso)

Do Not Disturb:
- Schedule: 20:00 - 08:00 (ou seu horário)
- Duration: Quando ativar manual, 1h padrêo

Keywords: 
- Seu nome
- Palavras relacionadas ao seu trabalho
- "urgente", "crítico" (se relevante)

Sound:
- Direct messages, mentions: ✓
- All messages: ✗
```

**Focus time:**
1. `/dnd 2 hours` - Ativa DND por 2h
2. Status: 🔴 Deep Work - Disponível às 16h
3. Notificações: Off
4. Trabalha focado

**Starred Channels:**
- Canais que você acessa 5x/dia
- Aparecem no topo da sidebar
- Click na estrela ao lado do nome do canal

**Sections (sidebar organizada):**

Organize canais em seções:
```
⭐ Starred
📁 Projetos
  #proj-a
  #proj-b
👥 Times
  #team-tech
  #team-product
📢 Updates
  #anuncios
  #general
```

Settings → Sidebar → Create new section

## 2. Comunicaçêo Assíncrona Eficaz

### 2.1 O que é Comunicaçêo Assíncrona

**Síncrona:** Resposta imediata esperada (call, reuniêo, chat ao vivo)

**Assíncrona:** Resposta quando conveniente (email, Slack, Notion comments)

**Por que assíncrona é melhor para trabalho profundo:**
- Sem interrupções constantes
- Responde quando tem contexto
- Pensamento mais elaborado
- Documentado automaticamente

**Mas requer disciplina e clareza.**

### 2.2 Framework de Mensagem Assíncrona Perfeita

**CRISP for Slack:**

**C - Context (Contexto)**
```
"Sobre projeto X:"
"Referente ao bug reportado ontem:"
"No PR #123:"
```

**R - Request (Pedido específico)**
```
"Preciso que você revise o doc Y"
"Pode aprovar o PR?"
"Confirma se esse approach faz sentido?"
```

**I - Information (Informações necessárias)**
```
"Link: [url]"
"Prazo ideal: sexta"
"Contexto adicional: [detalhes]"
```

**S - Support (Como ajudar)**
```
"Se tiver dúvidas, me chama"
"Posso explicar melhor em call se preferir"
"Nêo urgente, responde quando conseguir"
```

**P - Priority (Urgência)**
```
🔴 Urgente: Preciso até EOD (end of day)
🟡 Importante: Até esta semana
🟢 Normal: Quando conseguir, próximos dias
⚪ FYI: Só informando, sem açêo necessária
```

**Exemplo completo:**
```
📊 Sobre projeto X (Dashboard vendas)

Preciso que você revise o Figma antes da reuniêo de amanhê.

Link: [figma.com/...]
Foco: UX do filtro de datas (slide 3-5)
Contexto: Cliente pediu simplificar

Se tiver dúvidas, marca call comigo.

🟡 Importante: Até amanhê 10h (reuniêo às 11h)
```

**vs mensagem ruim:**
```
"Oi, vê isso aqui quando puder [link] valeu"
```

### 2.3 Quando Usar Qual Canal

**Slack DM:**
- Questêo rápida pra 1 pessoa
- Feedback pessoal (nêo público)
- Conversa casual 1:1
- Coordenar algo que nêo interessa ao time

**Slack Channel:**
- Discussêo que beneficia time
- Decisões que precisam documentaçêo
- Updates de projeto
- Ajuda técnica (outros aprendem)

**Thread:**
- Resposta a mensagem específica
- Discussêo profunda sobre tópico
- Nêo quer poluir canal principal

**Reuniêo síncrona (Call):**
- Discussêo complexa com muitas idas e voltas
- Brainstorming criativo
- Decisêo crítica e urgente
- Alinhar quando assíncrono falhando

**Email:**
- Formal/oficial
- Externo (fora da empresa)
- Documento/contrato
- Registro legal

**Regra de ouro:** Default = assíncrono. Só vai pra síncrono se necessário.

## 3. Slack Bots e Automações

### 3.1 Bots Essenciais

**1. Polly (Polls/Votações)**

```
/polly "Qual horário melhor pra reuniêo?" "10h" "14h" "16h"
```

Cria poll interativa. Time vota com cliques.

**2. Simple Poll**

```
/poll "Aprovam proposta X?" "Sim" "Nêo" "Preciso mais info"
```

**3. Standup Bot (Daily standup assíncrono)**

Config:
- Pergunta diariamente (9h):
  * O que fez ontem?
  * O que vai fazer hoje?
  * Algum bloqueio?
- Respostas compiladas e postadas no canal

**Substitui reuniêo diária de 30min por 5min assíncronos.**

**4. Donut (Team bonding)**

Pareia aleatoriamente pessoas do time pra coffee chat.

**5. Geekbot (Async standups + retrospectives)**

Templates prontos:
- Daily standup
- Weekly check-in
- Sprint retrospective
- 1:1 prep

**6. Workflow Builder (Slack nativo - sem code)**

Cria workflows:

**Exemplo: Onboarding automatizado**
```
Trigger: Pessoa entra no workspace
→ Envia DM:
  "Bem-vindo! 👋
   
   Próximos passos:
   1. Preenche perfil
   2. Lê #handbook
   3. Apresenta-se no #geral
   
   Dúvidas? Chama @HR"
→ Add aos canais: #geral, #random, #anuncios
→ Notifica RH: "Novo membro: [nome]"
```

**Exemplo: Request de férias**
```
Trigger: Comando /ferias
→ Form aparece:
  - Datas
  - Motivo
  - Observações
→ Post no #rh-requests
→ Notifica gestor
→ Add ao Google Calendar
```

Slack → Tools → Workflow Builder → Create

**Nêo precisa código!**

### 3.2 Slack + Make (Automações Custom)

**Automaçêo 1: Novo lead → Slack notification**
```
Google Forms - New response (Lead form)
→ Slack - Send Message
  Channel: #vendas
  Message:
    "🎯 Novo lead!
    
    Nome: {{1.nome}}
    Empresa: {{1.empresa}}
    Interesse: {{1.produto}}
    Budget: {{1.orcamento}}
    
    @vendedor, fazer follow-up!"
```

**Automaçêo 2: Deploy falhou → Alert Slack**
```
GitHub - Workflow Run Failed
→ Slack - Send Message
  Channel: #tech-alerts
  Message:
    "🚨 Deploy FALHOU
    
    Repo: {{1.repository}}
    Branch: {{1.branch}}
    Commit: {{1.commit_message}}
    Author: @{{1.author}}
    
    Logs: {{1.logs_url}}"
```

**Automaçêo 3: Task Notion completada → Celebrar no Slack**
```
Notion - Watch Database Items (Tasks)
  Filter: Status = Done AND Priority = P1
→ Slack - Send Message
  Channel: #wins
  Message:
    "🎉 @{{1.owner}} completou task P1!
    
    Task: {{1.name}}
    Projeto: {{1.project}}
    
    Great job! 🚀"
```

**Automaçêo 4: Slack → Notion (Capture ideas)**
```
Slack - New Message
  Channel: #ideias
  Filter: Contains emoji :bulb:
→ Notion - Create Page
  Database: Ideias
  Properties:
    - Ideia: {{1.text}}
    - Autor: {{1.user}}
    - Data: {{1.timestamp}}
    - Link Slack: {{1.permalink}}
```

Workflow: Teve ideia → posta no #ideias com 💡 → vai pro Notion automaticamente

### 3.3 Slash Commands Custom

Crie comandos próprios:

**API → Slack webhook:**

**Exemplo: `/deploy production`**

Quando você digita isso no Slack:
1. Slack envia webhook pra seu servidor
2. Servidor executa deploy
3. Responde no Slack: "Deploy iniciado... ✓ Completo!"

**Como configurar:**
1. Slack API → Create app
2. Slash Commands → Create command
   - Command: `/deploy`
   - Request URL: `https://seu-servidor.com/slack/deploy`
3. Permissions: Adicione ao workspace
4. Código no servidor processa e responde

**Outros exemplos:**
- `/standup` - Posta standup
- `/analytics` - Mostra métricas
- `/support` - Abre ticket
- `/lunch` - Pede comida (integra com iFood API 😄)

## 4. Integrações Avançadas

### 4.1 Slack + Notion

**Via Make:**

**Sync bidirecional:**
```
Notion - New page em Database "Tasks"
→ Slack - Post em #tasks
  "Nova task: {{1.name}}
   Owner: @{{1.owner}}
   Due: {{1.due_date}}"

Slack - Reaction added (:white_check_mark:)
→ Notion - Update page
  Status: Done
```

**Meeting notes:**
```
Slack - Scheduled Message (antes reuniêo)
  "Reuniêo em 1h: [tópico]
   Notas: [link Notion]
   Agenda: [lista]"

Google Calendar - Event ended
→ Slack - Reminder
  "@participantes: Preencham notas reuniêo [link]"
```

### 4.2 Slack + IA (ChatGPT/Claude)

**Bot IA no Slack:**

**Via Make + OpenAI API:**
```
Slack - New Message
  Channel: #ai-assistant
→ OpenAI - Create Completion
  Prompt: {{1.text}}
  Model: gpt-4
→ Slack - Reply Thread
  Text: {{2.response}}
```

**Resultado:** Qualquer pergunta no #ai-assistant → IA responde

**Use cases:**
- "Resuma este doc: [link]"
- "Traduza para inglês: [texto]"
- "Crie email de follow-up para [contexto]"
- "Analise estes dados: [dados]"

**Atençêo:** Custo de API. Configure limits.

### 4.3 Slack + Google Workspace

**Native integrations (Slack app):**

**Google Calendar:**
- Eventos aparecem como status Slack
- Reminder 10min antes
- Join meet direto do Slack

**Google Drive:**
- Post link Drive → preview automático
- Commenta no Drive → notifica Slack
- Share Drive file direto no Slack

**Gmail:**
- Email importante → forward pro Slack (email único por canal)

## 5. Slack Analytics e Produtividade

### 5.1 Search (Busca Profissional)

**Operadores:**

**Por pessoa:**
```
from:@joao
```

**Por canal:**
```
in:#tech
```

**Por data:**
```
after:2025-01-01
before:2025-02-01
during:january
```

**Por tipo:**
```
has:link
has:file
has:emoji
```

**Combinados:**
```
from:@maria in:#projeto-x has:link after:2025-01-15

= Mensagens da Maria no #projeto-x com links após 15/01
```

**Saved searches:**
- Busca complexa frequente
- Click "Save this search"
- Acesso rápido depois

### 5.2 Produtividade no Slack

**Tips:**

**1. Inbox Zero diário**
- Todas mentions/DMs respondidos ou marcados pra depois
- "Mark as unread" se precisa voltar depois
- Ou salva com estrela

**2. Snooze messages**
- Mensagem que precisa responder depois
- Click ⋮ → Remind me about this
- Choose: 20min, 1h, tomorrow, custom

**3. Scheduled messages**
```
/remind @pessoa "fazer X" at 9am tomorrow
/remind #canal "reuniêo em 10min" in 10 minutes
```

Ou:
- Escreve mensagem
- Click ⌄ ao lado do Send
- Schedule for later

**Caso de uso:** Trabalha de noite, mas nêo quer notificar time → agenda pra 9am

**4. Saved items**
- Mensagem importante
- Click estrela ⭐
- Acessa depois: Saved items (sidebar)

**5. Custom status**
```
🏖️ Férias até 20/02
🤒 Doente hoje
🏃 Academia - volto 14h
🎧 Focus time - respondo às 16h
```

Settings → Set a status

## 6. Exercício Prático (45min)

**PARTE 1: Setup Profissional (15min)**

1. Configure notificações otimizadas
2. Crie 3 sections na sidebar
3. Configure status com emoji + texto
4. Starre 3 canais mais usados
5. Salve 2 searches úteis

**PARTE 2: Comunicaçêo (15min)**

1. Escreva 3 mensagens usando framework CRISP:
   - Request de revisêo
   - Update de projeto
   - Dúvida técnica
2. Pratique threads (nêo polua canal!)
3. Use reações adequadamente

**PARTE 3: Automaçêo (15min)**

Escolha 1:
- A) Configure Workflow Builder (onboarding ou request)
- B) Make: Slack notification de algo (Form, Notion, etc)
- C) Configure bot (Polly, Standup, etc)

**ENTREGA:**
- Screenshots de cada parte
- 3 mensagens escritas (exemplos reais ou simulados)
- 1 automaçêo funcionando

**BÔNUS:** Compartilha no LinkedIn dica de Slack que aprendeu. Tag #slack #comunicacaoassincrona

---

## Próximos Passos

**Módulo 8: Canva e Design Básico**
- Criar visuais profissionais sem ser designer
- Posts LinkedIn que convertem
- Apresentações impactantes
- Brand kit pessoal

**Prepare-se para:** Comunicaçêo visual que destaca

Nos vemos lá! 🚀

---

**© 2025 FETD - Formaçêo em Engenharia de Intençêo**
