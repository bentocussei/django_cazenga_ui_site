# 🔧 Troubleshooting SPA - Guia de Resolução

## 🎯 Problema Relatado
Ao clicar nos itens do menu, toda a página ainda está recarregando ao invés de carregar apenas o conteúdo necessário.

## 🕵️ Passos para Debug

### 1. **Verificar Console do Navegador**

1. Execute o servidor: `python manage.py runserver`
2. Acesse: `http://localhost:8000/components/`
3. Abra o **Console do Navegador** (F12 → Console)
4. Procure por estas mensagens:

```
🚀 Página carregando...
🚀 SPA Simples carregando...
🟢 Alpine inicializado, ativando SPA...
✅ SPA Simples inicializado
```

**Se NÃO vir essas mensagens:**
- ❌ Arquivo `spa-simple.js` não está sendo carregado
- Verifique se existe: `theme/static/js/spa-simple.js`
- Rode: `python manage.py collectstatic`

### 2. **Testar Clique nos Links**

1. Clique em qualquer componente da sidebar
2. No console, deve aparecer:

```
🖱️ Clique interceptado no link: /components/button/
🔄 Navegando para: /components/button/
📡 Fazendo requisição AJAX: /components/button/?partial=true
📥 Dados recebidos: {content: "...", title: "..."}
🔄 Atualizando conteúdo principal...
✅ Navegação SPA concluída!
```

**Se vir navegação normal:**
- ❌ Links não têm `data-spa-link` ou SPA não está ativo

### 3. **Verificar Elementos no DOM**

No console, execute:

```javascript
// Verificar elemento principal
console.log('Main:', document.querySelector('#spa-main-content'));

// Verificar links SPA
console.log('Links SPA:', document.querySelectorAll('[data-spa-link]'));

// Verificar store Alpine
console.log('Store SPA:', Alpine.store('spaSimple'));
```

### 4. **Testar Requisição AJAX Manual**

No console, execute:

```javascript
fetch('/components/button/?partial=true', {
    headers: { 'X-Requested-With': 'XMLHttpRequest' }
})
.then(r => r.json())
.then(data => console.log('Resposta:', data))
.catch(e => console.error('Erro:', e));
```

**Deve retornar:**
```json
{
  "content": "<div>...</div>",
  "title": "Button - Componente UI",
  "path": "/components/button/"
}
```

## 🛠️ Soluções Possíveis

### **Problema 1: Arquivos Estáticos Não Carregam**

```bash
# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Verificar se arquivos existem
ls theme/static/js/
```

### **Problema 2: Alpine.js Não Carrega Store**

Adicione ao final do `<body>` em `components_base.html`:

```html
<script>
document.addEventListener('alpine:initialized', () => {
    console.log('🔍 Stores disponíveis:', Alpine.store());
    
    // Forçar inicialização se necessário
    if (!Alpine.store('spaSimple')) {
        console.log('⚠️ Store SPA não encontrado, recarregando...');
        location.reload();
    }
});
</script>
```

### **Problema 3: CSRF Token**

Se houver erro 403, adicione:

```html
<meta name="csrf-token" content="{{ csrf_token }}">
```

E no JavaScript:

```javascript
headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRFToken': document.querySelector('[name=csrf-token]').content
}
```

### **Problema 4: URL de Desenvolvimento**

No `settings.py`:

```python
# Para desenvolvimento
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'theme' / 'static',
]

# DEBUG deve estar True
DEBUG = True
```

## ⚡ Solução Rápida de Emergência

Se nada funcionar, use esta versão inline:

**Adicione no `<head>` do `components_base.html`:**

```html
<script>
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚨 SPA Inline ativado');
    
    document.addEventListener('click', (e) => {
        const link = e.target.closest('[data-spa-link]');
        if (!link) return;
        
        e.preventDefault();
        console.log('🔄 Navegando:', link.href);
        
        fetch(link.href + '?partial=true', {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(r => r.json())
        .then(data => {
            const main = document.querySelector('#spa-main-content');
            if (main) {
                main.innerHTML = data.content;
                history.pushState({}, data.title, link.href);
                console.log('✅ SPA Inline funcionando!');
            }
        })
        .catch(e => {
            console.error('❌ Erro:', e);
            window.location.href = link.href;
        });
    });
});
</script>
```

## 📋 Checklist Final

- [ ] Servidor Django rodando
- [ ] Arquivos estáticos coletados (`collectstatic`)
- [ ] Console sem erros JavaScript
- [ ] Links têm `data-spa-link`
- [ ] Elemento `#spa-main-content` existe
- [ ] Requisições AJAX retornam JSON
- [ ] Alpine.js carregado

## 🆘 Se Nada Funcionar

1. **Compartilhe o log do console** completo
2. **Verifique a aba Network** no DevTools para ver as requisições
3. **Teste em modo incógnito** para descartar cache
4. **Verifique se `DEBUG=True`** no settings.py

---

**🎯 O objetivo é transformar isto:**
```
Clique → Página recarrega completamente
```

**Em isto:**
```
Clique → Apenas conteúdo principal muda (como React!)
``` 