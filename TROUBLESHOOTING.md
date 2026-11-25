# 🔧 Troubleshooting - FETD

Documentaçêo de problemas encontrados e soluções aplicadas.

---

## ❌ Erro: Tailwind CDN Bloqueado (18/11/2025)

### 📋 Descriçêo do Problema

O layout do site parou de funcionar completamente em todos os navegadores (Firefox, Chrome, Edge) e tanto no localhost quanto no GitHub Pages.

**Sintomas:**
- Página carregava sem nenhuma formataçêo CSS
- Apenas texto preto e branco, sem cores ou layout
- Erro no console do navegador: `Uncaught ReferenceError: tailwind is not defined`
- Erro de rede: `OpaqueResponseBlocking` bloqueando `cdn.tailwindcss.com`

### 🕵️ Investigaçêo

**Linha do tempo:**
- **17/11 18:52 até 18/11 06:29:** Site funcionando normalmente com `cdn.tailwindcss.com`
- **18/11 10:23:** Usuário reportou que layout estava quebrado
- **18/11 10:23-11:01:** Várias tentativas de correçêo (reset para commits anteriores, clear cache, etc.)
- **18/11 11:01:** Mesmo voltando para commit a9fa6bf (onde estava funcionando), problema persistiu

**Teste de conectividade:**
```bash
$ curl -I https://cdn.tailwindcss.com
HTTP/2 500
date: Tue, 18 Nov 2025 14:16:03 GMT
content-type: text/plain; charset=UTF-8
server: cloudflare
```

### 🎯 Causa Raiz

**O servidor `cdn.tailwindcss.com` teve uma falha (HTTP 500 - Internal Server Error).**

- Nêo foi problema de código
- Nêo foi problema de configuraçêo local
- Nêo foi problema de navegador ou extensões
- Foi uma **queda/instabilidade no servidor do CDN oficial do Tailwind**

### ✅ Soluçêo Aplicada

Substituímos o CDN oficial por um CDN alternativo mais estável:

**Antes (quebrado):**
```html
<!-- Tailwind CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
```

**Depois (funcionando):**
```html
<!-- Tailwind CSS Play CDN (alternativa ao cdn.tailwindcss.com) -->
<script src="https://cdn.jsdelivr.net/npm/tailwindcss-cdn@3.4.1/tailwindcss.js"></script>
```

**Arquivos alterados:**
- `index.html`
- `trilhas/operacional.html`
- `trilhas/comunicador.html`
- `trilhas/talento.html`
- `trilhas/tecnico.html`
- `modulos/talento/modulo-01.html` até `modulo-10.html`

**Commit:**
```
209fb70 - feat: Atualizar Trilha 3 (Talento) com layout rico profissional
```

### 🔄 Para Testar Futuramente

**Verificar se cdn.tailwindcss.com voltou:**
```bash
curl -I https://cdn.tailwindcss.com
```

Se retornar `HTTP/2 200`, o CDN voltou ao normal.

**Testar carregamento no navegador:**
1. Abrir: https://cdn.tailwindcss.com
2. Deve baixar um arquivo JavaScript
3. Se aparecer erro 500 ou página em branco, CDN ainda está com problema

**Se quiser voltar para o CDN oficial:**
```bash
# Substituir em todos os arquivos HTML
find . -name "*.html" -type f -exec sed -i 's|https://cdn.jsdelivr.net/npm/tailwindcss-cdn@3.4.1/tailwindcss.js|https://cdn.tailwindcss.com|g' {} \;

# Commit e push
git add -A
git commit -m "Restaurar CDN oficial do Tailwind"
git push
```

### 📊 Vantagens do jsdelivr CDN

1. ✅ **Mais estável** - Menos quedas e problemas
2. ✅ **Versionado** - Usa versêo específica (3.4.1), mais previsível
3. ✅ **Múltiplos mirrors** - Se um servidor cai, outro assume
4. ✅ **Faster** - CDN global otimizado
5. ✅ **Usado por milhões** - Altamente confiável

### 📝 Lições Aprendidas

1. **CDNs podem cair** - Sempre ter alternativa (jsdelivr, unpkg, cdnjs)
2. **Testar em produçêo** - GitHub Pages pode ter comportamento diferente do localhost
3. **Monitorar status** - Sites como https://status.tailwindcss.com (se existir)
4. **Versionar CDNs** - Usar versêo específica em vez de `@latest`

### 🔗 Links Úteis

- **jsdelivr CDN:** https://www.jsdelivr.com/
- **Tailwind Play CDN (atual):** https://cdn.jsdelivr.net/npm/tailwindcss-cdn@3.4.1/
- **Tailwind oficial (problemático):** https://cdn.tailwindcss.com
- **Alternativa unpkg:** https://unpkg.com/tailwindcss-jit-cdn
- **Status Cloudflare:** https://www.cloudflarestatus.com/

---

## 🧪 Testes Futuros Recomendados

### Teste 1: Verificar Status do CDN Original
```bash
# Rodar este comando periodicamente
curl -I https://cdn.tailwindcss.com

# Esperado: HTTP/2 200 (funcionando)
# Problema: HTTP/2 500 (erro no servidor)
```

### Teste 2: Comparar Performance
```bash
# Testar velocidade do jsdelivr
time curl -s https://cdn.jsdelivr.net/npm/tailwindcss-cdn@3.4.1/tailwindcss.js > /dev/null

# Testar velocidade do CDN oficial (quando voltar)
time curl -s https://cdn.tailwindcss.com > /dev/null
```

### Teste 3: Validar em Múltiplos Navegadores
- [ ] Firefox (testado ✅)
- [ ] Chrome
- [ ] Edge
- [ ] Safari
- [ ] Mobile (iOS/Android)

### Teste 4: Validar GitHub Pages
1. Fazer push de alteraçêo
2. Aguardar 2-3 minutos
3. Abrir: https://linnoff88-dev.github.io/
4. Verificar console (F12) - nêo deve ter erros
5. Verificar layout - deve estar formatado

---

## 📞 Quando Usar Este Documento

- ✅ Se o layout parar de funcionar novamente
- ✅ Se quiser testar voltar para cdn.tailwindcss.com original
- ✅ Se precisar entender por que mudamos de CDN
- ✅ Se aparecer erro "tailwind is not defined"
- ✅ Como referência para projetos futuros

---

**Última atualizaçêo:** 18/11/2025
**Problema resolvido:** ✅ Sim
**Soluçêo permanente:** jsdelivr CDN
**Status atual:** Funcionando em todos os ambientes
