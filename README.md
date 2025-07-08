# Django Cazenga UI - Website de Demonstração

Website de demonstração da **[Django Cazenga UI](https://github.com/seu-usuario/django-cazenga-ui)** - uma biblioteca de componentes inspirada no shadcn/ui, construída com Django Templates, Tailwind CSS v4 e Alpine.js.

> 📚 **Este é um projeto de demonstração**. Para usar a biblioteca em seus projetos, visite: **[django-cazenga-ui](https://github.com/seu-usuario/django-cazenga-ui)**

## 🚀 Características da Biblioteca

- **53 Componentes** inspirados no shadcn/ui para Django
- **6 Temas de cores** (azul, laranja, verde, roxo, vermelho, amarelo)
- **333 Ícones SVG** do Radix Icons
- **Sistema SPA** completo com Alpine.js
- **Django-tailwind** integração opcional
- **CLI poderoso** para gestão de componentes
- **Acessibilidade** com ARIA labels completos
- **Responsivo** mobile-first

## 🎯 Este Projeto de Demonstração

- **Interface visual** para explorar componentes
- **Exemplos práticos** de uso
- **Playground interativo** 
- **Documentação visual** dos componentes

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

### 📦 Para usar a biblioteca em seus projetos:

```bash
# Instale a biblioteca Django Cazenga UI
pip install django-cazenga-ui[tailwind]

# Siga a documentação oficial:
# https://github.com/seu-usuario/django-cazenga-ui
```

### 🖥️ Para executar este projeto de demonstração localmente:

```bash
# Clone este repositório (projeto demo)
git clone <url-do-repo>
cd cazenga-ui-website

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

### 🌐 Acesse a demonstração:
- **Desenvolvimento**: `http://localhost:8000`
- **Online**: [Site da demonstração](https://seu-site-demo.com)

## 📚 Exemplos de Componentes (neste projeto demo)

> 💡 **Para usar em seus projetos**, instale a biblioteca `django-cazenga-ui` e siga a [documentação oficial](https://github.com/seu-usuario/django-cazenga-ui).

### Exemplos de uso neste projeto de demonstração:

### Button
```django
<!-- Básico -->
{% include "components/ui/button.html" with text="Clique aqui" %}

<!-- Com variantes -->
{% include "components/ui/button.html" with text="Deletar" variant="destructive" %}
{% include "components/ui/button.html" with text="Cancelar" variant="outline" %}

<!-- Com ícones -->
{% include "components/ui/button.html" with text="Download" icon='<svg>...</svg>' %}

<!-- Como link -->
{% include "components/ui/button.html" with text="Google" href="https://google.com" target="_blank" %}
```

### Select
```django
<!-- Select básico -->
{% include "components/ui/select.html" with name="country" options=countries placeholder="Selecione um país" %}

<!-- Com busca -->
{% include "components/ui/select.html" with name="city" options=cities searchable=True %}

<!-- Exemplo de options -->
{% with countries='[{"value":"br","label":"Brasil"},{"value":"us","label":"EUA"}]' %}
    {% include "components/ui/select.html" with name="country" options=countries %}
{% endwith %}
```

### Form
```django
{% include "components/ui/form.html" with fields=form_fields action="/submit" %}

<!-- Exemplo de form_fields -->
{% with form_fields='[
    {"type":"text","name":"name","label":"Nome","required":true},
    {"type":"email","name":"email","label":"Email","required":true},
    {"type":"select","name":"country","options":[{"value":"br","label":"Brasil"}]},
    {"type":"textarea","name":"message","label":"Mensagem","rows":4}
]' %}
    {% include "components/ui/form.html" with fields=form_fields %}
{% endwith %}
```

### Table
```django
<!-- Tabela básica -->
{% include "components/ui/table.html" with headers='["Nome","Email"]' data='[["João","joao@email.com"]]' %}

<!-- Com recursos avançados -->
{% include "components/ui/table.html" with headers=headers data=data sortable=True selectable=True striped=True %}
```

### Dialog
```django
{% include "components/ui/dialog.html" with 
    trigger='<button class="btn btn-primary">Abrir</button>'
    title="Confirmar"
    description="Tem certeza?"
    content="<p>Esta ação não pode ser desfeita.</p>"
    footer='<button @click="open=false">Cancelar</button>' %}
```

### Accordion
```django
{% include "components/ui/accordion.html" with items=accordion_items type="single" %}

<!-- Exemplo de accordion_items -->
{% with accordion_items='[
    {"title":"Pergunta 1","content":"Resposta 1","open":true},
    {"title":"Pergunta 2","content":"Resposta 2"}
]' %}
    {% include "components/ui/accordion.html" with items=accordion_items %}
{% endwith %}
```

### Pagination
```django
<!-- Com links -->
{% include "components/ui/pagination.html" with current_page=5 total_pages=20 base_url="/produtos" %}

<!-- Com JavaScript -->
{% include "components/ui/pagination.html" with current_page=3 total_pages=10 on_page_change="(page) => changePage(page)" %}
```

### Radio Group
```django
{% include "components/ui/radio-group.html" with name="payment" options=payment_options value="card" %}

<!-- Exemplo de payment_options -->
{% with payment_options='[
    {"value":"card","label":"Cartão","description":"Pagar com cartão"},
    {"value":"pix","label":"PIX","description":"Instantâneo"}
]' %}
    {% include "components/ui/radio-group.html" with name="payment" options=payment_options %}
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
        {% include "components/ui/card.html" with title=item.title content=item.content %}
    {% endfor %}
</div>
```

## ♿ Acessibilidade

- **ARIA labels** em todos os componentes interativos
- **Navegação por teclado** completa
- **Contraste** adequado em todos os temas
- **Screen readers** suportados
- **Focus management** em modais e dropdowns

## 🚀 Como usar a biblioteca Django Cazenga UI

### Instalação rápida:

```bash
# 1. Instalar
pip install django-cazenga-ui[tailwind]

# 2. Auto-configurar
cazenga-setup --auto-configure

# 3. Inicializar (processo interativo)
python manage.py cazenga init --with-tailwind --theme roxo

# 4. Adicionar componentes
python manage.py ui add button
python manage.py ui add card
python manage.py ui icons --install
```

### Documentação completa:
- **README oficial**: [django-cazenga-ui](https://github.com/seu-usuario/django-cazenga-ui)
- **Tutorial completo**: [TUTORIAL.md](https://github.com/seu-usuario/django-cazenga-ui/blob/main/TUTORIAL.md)

## 🧪 Exemplos e Demo

**Neste projeto de demonstração**:
- Visite `/demo/` para ver todos os componentes em ação
- Explore exemplos interativos  
- Teste diferentes variações e temas
- Veja código-fonte dos componentes

## 📁 Estrutura deste Projeto Demo

```
cazenga-ui-website/          # 🌐 Projeto de demonstração
├── core/                        # App Django principal
├── theme/                       # App Tailwind (criada pelo django-tailwind)
│   ├── templates/
│   │   ├── components/ui/       # Componentes copiados da biblioteca
│   │   ├── base.html           # Template base
│   │   └── demo.html           # Página de demonstração
│   └── static_src/
│       └── src/
│           ├── styles.css      # Tema aplicado
│           └── components.css  # Classes da biblioteca
└── django_cazenga_ui_site/     # Configurações Django

django-cazenga-ui/               # 📦 Biblioteca (repositório separado)
├── cazenga_ui/                  # Código da biblioteca
│   ├── management/commands/     # Comandos CLI (cazenga, ui)
│   ├── templates_source/        # 53 componentes fonte
│   ├── static_source/           # Temas, CSS, JavaScript
│   └── templatetags/            # Tags (ícones)
├── README.md                    # Documentação da biblioteca
└── TUTORIAL.md                  # Tutorial completo
```

### 🔗 Relação entre os projetos:

- **django-cazenga-ui** = Biblioteca pip com 53 componentes
- **cazenga-ui-website** = Website demo que usa a biblioteca

## 🤝 Contribuindo

### Para a biblioteca Django Cazenga UI:
- Contribua no repositório principal: **[django-cazenga-ui](https://github.com/seu-usuario/django-cazenga-ui)**

### Para este projeto de demonstração:
1. Fork este projeto
2. Crie uma branch para melhorias da demonstração
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

### Tipos de contribuição:
- 🐛 **Bug fixes** na demonstração  
- ✨ **Novos exemplos** de uso
- 📖 **Melhorias na documentação**
- 🎨 **Interface** e experiência do usuário

## 📄 Licença

MIT License - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- **[Django Cazenga UI](https://github.com/seu-usuario/django-cazenga-ui)** - Biblioteca de componentes demonstrada
- [shadcn/ui](https://ui.shadcn.com/) - Design system original inspirador
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS
- [Alpine.js](https://alpinejs.dev/) - Framework JavaScript reativo
- [Django](https://djangoproject.com/) - Framework web Python
- [Radix Icons](https://www.radix-ui.com/icons) - Conjunto de 333 ícones SVG

---

## 🔗 Links Úteis

### 📦 Biblioteca Django Cazenga UI:
- **[Repositório](https://github.com/seu-usuario/django-cazenga-ui)** - Código fonte da biblioteca
- **[PyPI](https://pypi.org/project/django-cazenga-ui/)** - Instalação via pip
- **[Tutorial](https://github.com/seu-usuario/django-cazenga-ui/blob/main/TUTORIAL.md)** - Documentação completa
- **[Changelog](https://github.com/seu-usuario/django-cazenga-ui/blob/main/CHANGELOG.md)** - Histórico de versões

### 🌐 Este Projeto Demo:
- **[Site Demo](https://seu-site-demo.com)** - Demonstração online
- **[Repositório](https://github.com/seu-usuario/cazenga-ui-website)** - Código do website

**Django Cazenga UI** - Componentes shadcn/ui para Django. Controle total, desenvolvimento rápido. 🚀 