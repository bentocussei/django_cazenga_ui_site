# Django + Tailwind CSS + Alpine.js Component Library

Uma biblioteca de componentes inspirada no shadcn/ui, construída com Django Templates, Tailwind CSS v4 e Alpine.js.

## 🚀 Características

- **23 Componentes** shadcn/ui convertidos para Django
- **Design System** completo com cores, tipografia e espaçamentos
- **Alpine.js** para interatividade reativa
- **Tailwind CSS v4** com hot reload
- **Acessibilidade** com ARIA labels e navegação por teclado
- **Temas** dark/light automático
- **Responsivo** mobile-first

## 📦 Componentes Disponíveis

### 🎯 **Componentes Essenciais (11)**
- **Button** - Botões com variantes, ícones e links
- **Input** - Campos de entrada com ícones e validação
- **Textarea** - Área de texto com redimensionamento
- **Select** - Dropdown com busca e seleção múltipla
- **Checkbox** - Caixas de seleção com estilos peer
- **Radio Group** - Grupos de radio buttons
- **Switch** - Toggle on/off com x-model
- **Label** - Rótulos com indicador obrigatório
- **Form** - Wrapper completo para formulários
- **Dialog** - Modal avançado com overlay
- **Table** - Tabelas com ordenação e seleção

### 🧩 **Componentes de Interface (7)**
- **Card** - Cartões flexíveis com header/footer
- **Alert** - Mensagens com variantes
- **Badge** - Etiquetas removíveis
- **Avatar** - Avatares com fallback
- **Progress** - Barras de progresso animadas
- **Separator** - Divisores horizontais/verticais
- **Tooltip** - Dicas com posicionamento

### 🗂️ **Componentes de Navegação (5)**
- **Tabs** - Navegação em abas com ícones
- **Accordion** - Conteúdo expansível
- **Breadcrumb** - Migalhas com ellipsis
- **Pagination** - Paginação completa
- **Dropdown** - Menus dropdown (legado)

## 🛠️ Instalação

```bash
# Clone o repositório
git clone <url-do-repo>
cd django-tailwind-alpine

# Instale as dependências Python
pip install django django-tailwind django-browser-reload

# Instale as dependências Node.js
cd theme/static_src
npm install

# Volte para o diretório raiz
cd ../..

# Execute as migrações
python manage.py migrate

# Inicie o servidor de desenvolvimento (em terminais separados)
python manage.py runserver
python manage.py tailwind dev
```

## 📚 Uso dos Componentes

### Button
```django
<!-- Básico -->
{% include "components/button.html" with text="Clique aqui" %}

<!-- Com variantes -->
{% include "components/button.html" with text="Deletar" variant="destructive" %}
{% include "components/button.html" with text="Cancelar" variant="outline" %}

<!-- Com ícones -->
{% include "components/button.html" with text="Download" icon='<svg>...</svg>' %}

<!-- Como link -->
{% include "components/button.html" with text="Google" href="https://google.com" target="_blank" %}
```

### Select
```django
<!-- Select básico -->
{% include "components/select.html" with name="country" options=countries placeholder="Selecione um país" %}

<!-- Com busca -->
{% include "components/select.html" with name="city" options=cities searchable=True %}

<!-- Exemplo de options -->
{% with countries='[{"value":"br","label":"Brasil"},{"value":"us","label":"EUA"}]' %}
    {% include "components/select.html" with name="country" options=countries %}
{% endwith %}
```

### Form
```django
{% include "components/form.html" with fields=form_fields action="/submit" %}

<!-- Exemplo de form_fields -->
{% with form_fields='[
    {"type":"text","name":"name","label":"Nome","required":true},
    {"type":"email","name":"email","label":"Email","required":true},
    {"type":"select","name":"country","options":[{"value":"br","label":"Brasil"}]},
    {"type":"textarea","name":"message","label":"Mensagem","rows":4}
]' %}
    {% include "components/form.html" with fields=form_fields %}
{% endwith %}
```

### Table
```django
<!-- Tabela básica -->
{% include "components/table.html" with headers='["Nome","Email"]' data='[["João","joao@email.com"]]' %}

<!-- Com recursos avançados -->
{% include "components/table.html" with headers=headers data=data sortable=True selectable=True striped=True %}
```

### Dialog
```django
{% include "components/dialog.html" with 
    trigger='<button class="btn btn-primary">Abrir</button>'
    title="Confirmar"
    description="Tem certeza?"
    content="<p>Esta ação não pode ser desfeita.</p>"
    footer='<button @click="open=false">Cancelar</button>' %}
```

### Accordion
```django
{% include "components/accordion.html" with items=accordion_items type="single" %}

<!-- Exemplo de accordion_items -->
{% with accordion_items='[
    {"title":"Pergunta 1","content":"Resposta 1","open":true},
    {"title":"Pergunta 2","content":"Resposta 2"}
]' %}
    {% include "components/accordion.html" with items=accordion_items %}
{% endwith %}
```

### Pagination
```django
<!-- Com links -->
{% include "components/pagination.html" with current_page=5 total_pages=20 base_url="/produtos" %}

<!-- Com JavaScript -->
{% include "components/pagination.html" with current_page=3 total_pages=10 on_page_change="(page) => changePage(page)" %}
```

### Radio Group
```django
{% include "components/radio-group.html" with name="payment" options=payment_options value="card" %}

<!-- Exemplo de payment_options -->
{% with payment_options='[
    {"value":"card","label":"Cartão","description":"Pagar com cartão"},
    {"value":"pix","label":"PIX","description":"Instantâneo"}
]' %}
    {% include "components/radio-group.html" with name="payment" options=payment_options %}
{% endwith %}
```

## 🎨 Sistema de Cores

```css
/* Cores principais */
--primary: 222.2 84% 4.9%;
--primary-foreground: 210 40% 98%;

/* Cores de fundo */
--background: 0 0% 100%;
--foreground: 222.2 84% 4.9%;

/* Cores de borda */
--border: 214.3 31.8% 91.4%;
--input: 214.3 31.8% 91.4%;

/* Estados */
--destructive: 0 84.2% 60.2%;
--muted: 210 40% 96%;
--accent: 210 40% 96%;
```

## 🌙 Modo Escuro

Todos os componentes suportam modo escuro automaticamente:

```html
<!-- Toggle de tema -->
<button @click="toggleTheme()" class="btn btn-ghost">
    <span x-show="theme === 'dark'">☀️</span>
    <span x-show="theme === 'light'">🌙</span>
</button>
```

## 📱 Responsividade

Todos os componentes são responsivos por padrão:

```django
<!-- Grid responsivo -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {% for item in items %}
        {% include "components/card.html" with title=item.title content=item.content %}
    {% endfor %}
</div>
```

## ♿ Acessibilidade

- **ARIA labels** em todos os componentes interativos
- **Navegação por teclado** completa
- **Contraste** adequado em todos os temas
- **Screen readers** suportados
- **Focus management** em modais e dropdowns

## 🧪 Exemplos e Demo

Visite `/demo/` para ver todos os componentes em ação com exemplos interativos.

## 📁 Estrutura do Projeto

```
django-tailwind-alpine/
├── core/                    # App Django principal
├── theme/                   # App Tailwind
│   ├── templates/
│   │   ├── components/      # 23 componentes
│   │   ├── base.html        # Template base
│   │   └── demo.html        # Página de demonstração
│   └── static_src/
│       └── src/
│           ├── styles.css   # Estilos principais
│           └── components.css # Classes de componentes
└── django_tailwind_alpine/  # Configurações Django
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

MIT License - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- [shadcn/ui](https://ui.shadcn.com/) - Design system original
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS
- [Alpine.js](https://alpinejs.dev/) - Framework JavaScript
- [Django](https://djangoproject.com/) - Framework web Python 