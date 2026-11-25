# 🚀 Guia Rápido: Como Usar o Conversor Ultra Rico v2.0

## ⚡ Uso Rápido

### Converter uma trilha completa

```bash
python3 converter_md_para_html_rico_v2.py talento
```

### Converter apenas um módulo

```bash
python3 converter_md_para_html_rico_v2.py talento 1
```

### Converter todas as trilhas de uma vez

```bash
for trilha in operacional comunicador talento tecnico; do
  python3 converter_md_para_html_rico_v2.py $trilha
done
```

---

## 📁 Arquivos Importantes

| Arquivo | Descriçêo |
|---------|-----------|
| `converter_md_para_html_rico_v2.py` | Script principal do conversor |
| `LAYOUT_ULTRA_RICO_V2.md` | Documentaçêo completa do formato |
| `downloads/{trilha}/modulo-XX.md` | Arquivos Markdown fonte (INPUT) |
| `modulos/{trilha}/modulo-XX.html` | Arquivos HTML gerados (OUTPUT) |

---

## 🎨 Elementos Visuais Suportados

| Elemento | Como Criar no MD |
|----------|------------------|
| 🎯 Box Objetivo | Adicione `**Objetivo:** texto` no cabeçalho |
| ❌ Card Mito | Use `### ❌ Mito:` ou `### Mito` |
| ✅ Card Verdade | Use `### ✅ Verdade:` ou `### Verdade` |
| 💼 Card Exemplo | Use `### Exemplo:` ou `### Case:` |
| 💡 Card Importante | Use `### 💡 Importante:` |
| 📊 Card Dados | Use `### 📊 Dados:` |
| 📋 Tabela Premium | Use tabelas Markdown normais |
| 💻 Código Terminal | Use blocos com ``` |
| 🔄 Grid Antes/Agora | Crie lista com "Antes:" e "Agora:" |

---

## 🎯 Trilhas Disponíveis

- `operacional` - Operacional Produtivo (🔵 Azul)
- `comunicador` - Comunicador Estratégico (🟢 Verde)
- `talento` - Talento Emergente (🟡 Amarelo)
- `tecnico` - Técnico Comunicador (🟠 Laranja)

---

## ✅ Checklist Antes de Converter

- [ ] Arquivo `.md` existe em `downloads/{trilha}/`
- [ ] Arquivo tem estrutura correta (título, duraçêo, objetivo)
- [ ] Seções usam `##` e subseções `###`
- [ ] Tabelas têm linha separadora `|---|---|`
- [ ] Blocos de código usam ``` corretamente

---

## 🧪 Testando Localmente

```bash
# Iniciar servidor
python3 -m http.server 8080

# Acessar no navegador
http://localhost:8080/modulos/talento/modulo-01.html
```

---

## 🔧 Troubleshooting Rápido

**Erro: Arquivo nêo encontrado**
→ Verifique caminho: `downloads/{trilha}/modulo-XX.md`

**Card nêo ficou colorido**
→ Use emoji/keyword no título: ❌ ✅ 💼 💡 📊

**Tabela nêo renderiza**
→ Adicione linha separadora: `|---|---|`

**Código sem estilo terminal**
→ Use 3 backticks: ``` antes e depois

---

## 📚 Documentaçêo Completa

Para detalhes completos, consulte: **`LAYOUT_ULTRA_RICO_V2.md`**

---

**Última atualizaçêo:** 2025-01-19
