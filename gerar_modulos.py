#!/usr/bin/env python3
"""
Gerador de Módulos - Trilha Operacional FETD
Cria os módulos 4-10 automaticamente
"""

import os

# Conteúdo dos módulos
MODULOS = {
    4: {
        "titulo": "Ferramentas No-Code - Zapier e Make",
        "duracao": "1h 30min",
        "objetivo": "Criar sua primeira automação sem código usando Zapier ou Make",
        "secoes": [
            {
                "titulo": "1. O Que São Ferramentas No-Code",
                "conteudo": """
<p class="text-lg text-neutral-700 dark:text-neutral-300 mb-6">
  Ferramentas <strong>no-code</strong> são plataformas que permitem criar automações e integrações complexas <strong>sem escrever uma única linha de código</strong>. Você conecta aplicativos através de uma interface visual, clicando e arrastando.
</p>

<div class="bg-neutral-50 dark:bg-neutral-900 p-6 rounded-xl mb-6">
  <h4 class="font-bold text-lg mb-4">Como funcionam:</h4>
  <ol class="space-y-3 text-neutral-700 dark:text-neutral-300 list-decimal list-inside">
    <li><strong>Trigger (Gatilho):</strong> Algo acontece (ex: novo email chega)</li>
    <li><strong>Action (Ação):</strong> Sistema faz algo automaticamente (ex: salva anexo no Drive)</li>
    <li><strong>Conectores:</strong> Ligam diferentes aplicativos</li>
  </ol>
</div>

<p class="text-lg text-neutral-700 dark:text-neutral-300 mb-6">
  É como montar um quebra-cabeça: você escolhe as peças (aplicativos) e conecta elas de forma lógica. O sistema faz o resto automaticamente, 24/7.
</p>

<div class="bg-operacional/10 dark:bg-operacional/20 p-6 rounded-xl">
  <p class="text-lg font-bold mb-3">💡 Exemplo Prático:</p>
  <p class="text-neutral-700 dark:text-neutral-300">
    <strong>Trigger:</strong> Email recebido com anexo<br>
    <strong>Action 1:</strong> Salvar anexo no Google Drive<br>
    <strong>Action 2:</strong> Enviar notificação no Slack<br>
    <strong>Resultado:</strong> Você nunca mais perde um anexo importante!
  </p>
</div>
"""
            },
            {
                "titulo": "2. Zapier vs Make: Qual Usar?",
                "conteudo": """
<p class="text-lg text-neutral-700 dark:text-neutral-300 mb-6">
  Existem várias ferramentas no-code. As duas mais populares são <strong>Zapier</strong> e <strong>Make</strong> (antigo Integromat). Vamos entender as diferenças:
</p>

<div class="grid md:grid-cols-2 gap-6 mb-6">
  <div class="bg-blue-50 dark:bg-blue-900/20 p-6 rounded-xl border-2 border-operacional/30">
    <h4 class="text-xl font-bold mb-4 text-operacional">⚡ Zapier</h4>
    <p class="text-sm text-neutral-600 dark:text-neutral-400 mb-4">Mais simples e popular</p>
    <ul class="space-y-2 text-sm text-neutral-700 dark:text-neutral-300">
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Interface muito simples</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Conecta 6.000+ aplicativos</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Plano grátis: 100 tarefas/mês</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Perfeito para iniciantes</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-red-500">✗</span>
        <span>Menos flexível</span>
      </li>
    </ul>
  </div>

  <div class="bg-purple-50 dark:bg-purple-900/20 p-6 rounded-xl border-2 border-purple-500/30">
    <h4 class="text-xl font-bold mb-4 text-purple-600">🔧 Make</h4>
    <p class="text-sm text-neutral-600 dark:text-neutral-400 mb-4">Mais poderoso e visual</p>
    <ul class="space-y-2 text-sm text-neutral-700 dark:text-neutral-300">
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Interface visual avançada</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Conecta 1.500+ aplicativos</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Plano grátis: 1.000 operações/mês</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500">✓</span>
        <span>Muito mais flexível</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-red-500">✗</span>
        <span>Curva de aprendizado maior</span>
      </li>
    </ul>
  </div>
</div>

<div class="bg-yellow-50 dark:bg-yellow-900/20 border-l-4 border-yellow-500 p-6 rounded-lg">
  <p class="font-bold mb-2">💡 Nossa Recomendação:</p>
  <p class="text-neutral-700 dark:text-neutral-300">
    <strong>Comece com Zapier</strong> (mais simples). Depois de dominar, experimente Make para automações mais complexas. Muitas pessoas usam os dois!
  </p>
</div>
"""
            },
            {
                "titulo": "3. Conceitos Essenciais: Triggers e Actions",
                "conteudo": """
<p class="text-lg text-neutral-700 dark:text-neutral-300 mb-6">
  Toda automação no-code funciona com a mesma lógica: <strong>SE isso acontecer (Trigger), ENTÃO faça aquilo (Action)</strong>.
</p>

<div class="bg-neutral-50 dark:bg-neutral-900 p-6 rounded-xl mb-6">
  <h4 class="font-bold text-lg mb-4">🔔 Triggers (Gatilhos)</h4>
  <p class="text-neutral-700 dark:text-neutral-300 mb-3">
    São eventos que <strong>iniciam</strong> uma automação:
  </p>
  <ul class="space-y-2 text-sm">
    <li>• Novo email recebido</li>
    <li>• Nova linha em planilha</li>
    <li>• Formulário preenchido</li>
    <li>• Arquivo adicionado em pasta</li>
    <li>• Novo evento no calendário</li>
    <li>• Horário específico (todo dia às 9h)</li>
  </ul>
</div>

<div class="bg-operacional/10 dark:bg-operacional/20 p-6 rounded-xl mb-6">
  <h4 class="font-bold text-lg mb-4">⚙️ Actions (Ações)</h4>
  <p class="text-neutral-700 dark:text-neutral-300 mb-3">
    São tarefas que o sistema <strong>executa automaticamente</strong>:
  </p>
  <ul class="space-y-2 text-sm">
    <li>• Enviar email</li>
    <li>• Criar/atualizar planilha</li>
    <li>• Salvar arquivo</li>
    <li>• Postar em redes sociais</li>
    <li>• Enviar notificação</li>
    <li>• Criar tarefa/evento</li>
  </ul>
</div>

<p class="text-lg text-neutral-700 dark:text-neutral-300">
  O poder está em <strong>combinar</strong> triggers e actions de aplicativos diferentes, criando fluxos que funcionam sozinhos!
</p>
"""
            }
        ],
        "exercicios_reflexao": [
            "Que ferramentas você usa todos os dias no trabalho? (Liste pelo menos 10)",
            "Que informações você copia manualmente de um lugar para outro?",
            "Que avisos/lembretes você gostaria de receber automaticamente?"
        ],
        "exercicio_pratico": {
            "titulo": "Criar 3 Automações Simples no Zapier",
            "descricao": "Vamos criar suas primeiras 3 automações funcionais usando Zapier (versão gratuita).",
            "passos": """
<h4 class="font-bold text-lg mb-3">Passo 1: Criar Conta no Zapier</h4>
<ol class="list-decimal list-inside space-y-2 text-sm mb-6">
  <li>Acesse: <a href="https://zapier.com" class="text-operacional hover:underline">zapier.com</a></li>
  <li>Clique em "Sign Up" (Cadastrar)</li>
  <li>Use sua conta Google para facilitar</li>
  <li>Pule o tour (você vai aprender fazendo)</li>
</ol>

<h4 class="font-bold text-lg mb-3">Automação 1: Email → Drive</h4>
<p class="text-sm mb-3">Salvar automaticamente anexos de emails no Google Drive</p>
<ol class="list-decimal list-inside space-y-2 text-sm mb-6">
  <li><strong>Trigger:</strong> Gmail - "New Attachment"</li>
  <li><strong>Action:</strong> Google Drive - "Upload File"</li>
  <li>Configure: pasta de destino, nome do arquivo</li>
  <li>Teste e ative!</li>
</ol>

<h4 class="font-bold text-lg mb-3">Automação 2: Planilha → Slack</h4>
<p class="text-sm mb-3">Notificação toda vez que alguém adiciona linha na planilha</p>
<ol class="list-decimal list-inside space-y-2 text-sm mb-6">
  <li><strong>Trigger:</strong> Google Sheets - "New Spreadsheet Row"</li>
  <li><strong>Action:</strong> Slack - "Send Channel Message"</li>
  <li>Configure: qual planilha monitorar, canal do Slack</li>
  <li>Teste e ative!</li>
</ol>

<h4 class="font-bold text-lg mb-3">Automação 3: Formulário → Tarefa</h4>
<p class="text-sm mb-3">Criar tarefa automaticamente quando formulário é preenchido</p>
<ol class="list-decimal list-inside space-y-2 text-sm">
  <li><strong>Trigger:</strong> Google Forms - "New Response"</li>
  <li><strong>Action:</strong> Google Tasks - "Create Task"</li>
  <li>Configure: qual formulário, lista de tarefas</li>
  <li>Teste e ative!</li>
</ol>
"""
        },
        "entregavel": "Minhas 3 Primeiras Automações (prints + descrição)"
    },
    5: {
        "titulo": "Automação de Emails e Comunicação",
        "duracao": "1h 30min",
        "objetivo": "Criar um sistema completo de gestão de emails que funciona sozinho",
        "entregavel": "Sistema de Email Zero"
    },
    6: {
        "titulo": "Planilhas Inteligentes com IA",
        "duracao": "1h 30min",
        "objetivo": "Automatizar análise e manipulação de dados com Google Sheets + IA",
        "entregavel": "Dashboard Pessoal Automatizado"
    },
    7: {
        "titulo": "Documentação e Arquivos Automáticos",
        "duracao": "1h",
        "objetivo": "Sistema de gestão de documentos 100% organizado e automático",
        "entregavel": "Sistema de Arquivos Inteligente"
    },
    8: {
        "titulo": "Reuniões e Agenda Automatizados",
        "duracao": "1h",
        "objetivo": "Gestão inteligente de tempo e compromissos com IA",
        "entregavel": "Sistema de Reuniões Eficientes"
    },
    9: {
        "titulo": "Framework 4R's - Entregar Resultados",
        "duracao": "1h",
        "objetivo": "Documentar e mostrar valor criado para ganhar reconhecimento",
        "entregavel": "Relatório de Impacto das Automações"
    },
    10: {
        "titulo": "Sistema Completo + Evolução",
        "duracao": "2h",
        "objetivo": "Consolidar tudo e planejar próximos passos profissionais",
        "entregavel": "Portfólio de Automações + Certificado"
    }
}

def criar_modulo_html(num, dados):
    """Cria HTML do módulo"""

    # Para módulos 5-10, usar estrutura simplificada mas completa
    if num >= 5:
        secoes_html = f"""
<div class="mb-16">
  <h2 class="text-3xl font-bold mb-6">Conteúdo em Desenvolvimento</h2>
  <div class="bg-operacional/10 dark:bg-operacional/20 p-8 rounded-xl">
    <p class="text-lg mb-4">
      Este módulo está sendo desenvolvido com conteúdo rico e detalhado.
    </p>
    <p class="text-neutral-700 dark:text-neutral-300 mb-4">
      <strong>Objetivo:</strong> {dados['objetivo']}
    </p>
    <p class="text-neutral-700 dark:text-neutral-300">
      <strong>Entregável:</strong> {dados['entregavel']}
    </p>
  </div>
</div>
"""
    else:
        # Módulo 4 tem conteúdo completo
        secoes_html = ""
        for secao in dados.get('secoes', []):
            secoes_html += f"""
<div class="mb-16">
  <h2 class="text-3xl font-bold mb-6">{secao['titulo']}</h2>
  {secao['conteudo']}
</div>
"""

    prev_num = num - 1
    next_num = num + 1 if num < 10 else None

    html = f"""<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Módulo {num}: {dados['titulo']} | Trilha Operacional | FETD</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{ 'operacional': '#3B82F6' }},
          fontFamily: {{ sans: ['Inter', 'sans-serif'] }}
        }}
      }}
    }}
  </script>
  <style>
    * {{ transition: background-color 200ms ease-in-out; }}
    body {{ font-family: 'Inter', sans-serif; }}
  </style>
</head>
<body class="bg-neutral-50 dark:bg-neutral-900 text-neutral-900 dark:text-neutral-100">

  <nav class="sticky top-0 z-50 bg-white/90 dark:bg-neutral-800/90 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <a href="../../index.html" class="text-2xl font-bold bg-gradient-to-r from-operacional to-blue-600 bg-clip-text text-transparent">🎓 FETD</a>
        <div class="hidden md:flex items-center space-x-8">
          <a href="../../index.html" class="text-neutral-700 dark:text-neutral-300 hover:text-operacional">Início</a>
          <a href="../../trilhas/operacional.html" class="text-neutral-700 dark:text-neutral-300 hover:text-operacional">Trilha Operacional</a>
          <button id="theme-toggle" class="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-700">
            <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
            </svg>
            <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </nav>

  <div class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
      <nav class="flex text-sm">
        <a href="../../index.html" class="text-operacional hover:text-blue-700">Início</a>
        <span class="mx-2 text-neutral-400">/</span>
        <a href="../../trilhas/operacional.html" class="text-operacional hover:text-blue-700">Trilha Operacional</a>
        <span class="mx-2 text-neutral-400">/</span>
        <span class="text-neutral-600 dark:text-neutral-400">Módulo {num}</span>
      </nav>
    </div>
  </div>

  <section class="bg-gradient-to-r from-operacional to-blue-600 py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-white">
      <div class="flex items-center gap-3 mb-4">
        <span class="px-3 py-1 bg-white/20 rounded-full text-sm font-semibold">Módulo {num} de 10</span>
        <span class="px-3 py-1 bg-white/20 rounded-full text-sm font-semibold">⏱️ {dados['duracao']}</span>
      </div>
      <h1 class="text-4xl lg:text-5xl font-extrabold mb-4">{dados['titulo']}</h1>
      <p class="text-xl text-white/90 mb-6 max-w-3xl">{dados['objetivo']}</p>
    </div>
  </section>

  <section class="py-16 bg-white dark:bg-neutral-800">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="flex justify-end mb-8">
        <a href="../../downloads/operacional/modulo-{num:02d}.md" download class="px-6 py-3 bg-operacional text-white rounded-lg font-semibold hover:opacity-90 inline-flex items-center gap-2">
          <span>📥 Download MD</span>
        </a>
      </div>

      <div class="bg-operacional/10 dark:bg-operacional/20 border-l-4 border-operacional p-6 rounded-lg mb-12">
        <h3 class="text-xl font-bold text-operacional mb-2">🎯 Objetivo deste Módulo</h3>
        <p class="text-neutral-700 dark:text-neutral-300">{dados['objetivo']}</p>
      </div>

      {secoes_html}

      <div class="mb-16">
        <div class="bg-gradient-to-r from-operacional/20 to-blue-500/20 p-8 rounded-2xl">
          <h2 class="text-3xl font-bold mb-6">🎉 Parabéns por Completar o Módulo {num}!</h2>
          <div class="bg-white dark:bg-neutral-800 p-6 rounded-xl mb-6">
            <h4 class="font-bold mb-3">✅ Entregável deste módulo:</h4>
            <p class="text-neutral-700 dark:text-neutral-300">{dados['entregavel']}</p>
          </div>
        </div>
      </div>

      <div class="bg-gradient-to-r from-operacional to-blue-600 text-white rounded-2xl p-8">
        <div class="flex justify-between items-center flex-wrap gap-4">
          <a href="modulo-{prev_num:02d}.html" class="px-6 py-3 bg-white/20 hover:bg-white/30 rounded-lg font-semibold transition-all">
            ← Módulo {prev_num}
          </a>
          {f'<a href="modulo-{next_num:02d}.html" class="px-6 py-3 bg-white text-operacional rounded-lg font-semibold hover:bg-yellow-300 transition-all">Módulo {next_num} →</a>' if next_num else '<a href="../../trilhas/operacional.html" class="px-6 py-3 bg-white text-operacional rounded-lg font-semibold hover:bg-yellow-300 transition-all">Voltar à Trilha →</a>'}
        </div>
      </div>

    </div>
  </section>

  <footer class="bg-neutral-900 dark:bg-black text-neutral-300 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm">
      <p>&copy; 2025 FETD - Formação em Engenharia de Intenção</p>
    </div>
  </footer>

  <script src="../../js/app.js"></script>
</body>
</html>"""

    return html

def criar_modulo_md(num, dados):
    """Cria Markdown do módulo"""
    md = f"""# Módulo {num}: {dados['titulo']}

**Trilha:** Operacional Produtivo
**Duração:** {dados['duracao']}
**Objetivo:** {dados['objetivo']}

---

## 🎯 Objetivo deste Módulo

{dados['objetivo']}

---

## Conteúdo

(Conteúdo detalhado em desenvolvimento)

---

## ✅ Entregável do Módulo {num}

{dados['entregavel']}

---

**© 2025 FETD - Formação em Engenharia de Intenção**
"""
    return md

def main():
    """Gera todos os módulos 4-10"""
    base_path = "/home/nmaldaner/projetos/FETD"

    for num, dados in MODULOS.items():
        # Criar HTML
        html_path = f"{base_path}/modulos/operacional/modulo-{num:02d}.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(criar_modulo_html(num, dados))
        print(f"✅ Criado: {html_path}")

        # Criar MD
        md_path = f"{base_path}/downloads/operacional/modulo-{num:02d}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(criar_modulo_md(num, dados))
        print(f"✅ Criado: {md_path}")

    print(f"\n🎉 CONCLUÍDO! {len(MODULOS)} módulos criados (4-10)")

if __name__ == "__main__":
    main()
