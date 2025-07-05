# Django + Tailwind CSS + Alpine.js Component Library

Uma biblioteca de componentes reutilizáveis inspirada no [shadcn/ui](https://ui.shadcn.com/), construída com Django, Tailwind CSS v4 e Alpine.js.

## 🚀 Características

- 🎨 Sistema de cores e temas (claro/escuro) usando variáveis CSS
- 🧩 Componentes reutilizáveis prontos para uso
- ⚡ Hot reload em desenvolvimento com django-browser-reload
- 🎯 Totalmente tipado com Tailwind CSS v4
- 🔧 Fácil customização e extensão
- 📱 Componentes responsivos por padrão

## 📦 Componentes Disponíveis

- **Button** - Botões com 6 variantes (primary, secondary, destructive, outline, ghost, link)
- **Modal** - Modais responsivos com diferentes tamanhos
- **Dropdown** - Menus dropdown com alinhamento configurável
- **Card** - Cards estilizados com header, content e footer
- **Input/Textarea** - Campos de formulário estilizados
- **Label** - Labels para formulários

## 🛠️ Pré-requisitos

- Python 3.8+
- Node.js 14+ e npm
- pip (gerenciador de pacotes Python)

## 📋 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/django-tailwind-alpine.git
cd django-tailwind-alpine
```

### 2. Configure o ambiente virtual Python

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências Python

```bash
pip install django
pip install 'django-tailwind[reload]'
```

### 4. Configure o Django

```bash
# Execute as migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser
```

### 5. Instale as dependências do Tailwind CSS

```bash
python manage.py tailwind install
```

## 🚀 Como Usar

### Desenvolvimento

Para iniciar o ambiente de desenvolvimento com hot reload:

```bash
# Terminal 1 - Inicia o servidor Django e o compilador Tailwind
python manage.py tailwind dev

# Terminal 2 - Em uma nova janela/aba (opcional, se preferir separado)
python manage.py runserver
```

Acesse:
- `http://127.0.0.1:8000/` - Página inicial
- `http://127.0.0.1:8000/demo/` - Demonstração completa dos componentes

### Produção

Para compilar o CSS para produção:

```bash
python manage.py tailwind build
```

## 🎨 Usando os Componentes

### Button

```django
{% include "components/button.html" with text="Clique aqui" variant="primary" size="md" %}
```

Parâmetros:
- `text`: Texto do botão
- `variant`: primary, secondary, destructive, outline, ghost, link
- `size`: sm, md, lg
- `type`: button, submit, reset
- `x_click`: Evento Alpine.js para @click
- `disabled`: true/false
- `class`: Classes CSS adicionais

### Modal

```django
<!-- Botão para abrir o modal -->
<button @click="open_meuModal = true" class="btn btn-primary">
    Abrir Modal
</button>

<!-- Modal -->
{% include "components/modal.html" with modal_id="meuModal" title="Título do Modal" %}
```

Parâmetros:
- `modal_id`: ID único do modal (obrigatório)
- `title`: Título do modal
- `size`: sm, md, lg, xl
- `content`: Conteúdo HTML do modal

### Dropdown

```django
{% include "components/dropdown.html" with dropdown_id="menu1" label="Opções" align="right" %}
```

Parâmetros:
- `dropdown_id`: ID único do dropdown (obrigatório)
- `label`: Texto do botão do dropdown
- `align`: left, right
- `items`: Lista de itens (ou use block dropdown_items)

## 🌙 Tema Escuro

O sistema suporta tema escuro automaticamente. Para ativar/desativar:

```html
<button @click="darkMode = !darkMode">
    Toggle Dark Mode
</button>
```

## 🎨 Customização

### Cores

As cores estão definidas em `theme/static_src/src/styles.css` usando o formato OKLCH. Para customizar:

```css
:root {
  --primary: oklch(0.623 0.214 259.815);
  --secondary: oklch(0.967 0.001 286.375);
  /* ... outras cores ... */
}
```

### Novos Componentes

Para criar um novo componente:

1. Crie um arquivo em `theme/templates/components/seu_componente.html`
2. Use as classes CSS definidas em `theme/static_src/src/components.css`
3. Adicione interatividade com Alpine.js

Exemplo:

```django
{# theme/templates/components/alert.html #}
<div class="rounded-md p-4 bg-{{ variant|default:'info' }}-50 text-{{ variant|default:'info' }}-800">
    {{ message }}
</div>
```

## 📁 Estrutura do Projeto

```
django-tailwind-alpine/
├── core/                       # App principal Django
│   ├── views.py               # Views do projeto
│   └── ...
├── theme/                      # App do Tailwind CSS
│   ├── static_src/            # Arquivos fonte
│   │   ├── src/
│   │   │   ├── styles.css     # Estilos principais e variáveis
│   │   │   └── components.css # Classes dos componentes
│   │   └── package.json       # Dependências Node.js
│   ├── templates/             # Templates HTML
│   │   ├── components/        # Componentes reutilizáveis
│   │   └── base.html          # Template base
│   └── static/                # Arquivos compilados (gerado)
├── django_tailwind_alpine/     # Configurações Django
├── manage.py                   # CLI do Django
└── README.md                   # Este arquivo
```

## 🔧 Configurações Avançadas

### NPM no Windows

Se você encontrar problemas com o npm no Windows, adicione ao `settings.py`:

```python
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

### Configuração do @source (Tailwind v4)

O arquivo `theme/static_src/src/styles.css` contém:

```css
@source "../../../**/*.{html,py,js}";
```

Ajuste conforme necessário para sua estrutura de projeto.

## 📚 Recursos Adicionais

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Tailwind CSS](https://tailwindcss.com/docs)
- [Documentação do Alpine.js](https://alpinejs.dev/)
- [django-tailwind docs](https://django-tailwind.readthedocs.io/)

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [shadcn/ui](https://ui.shadcn.com/) - Inspiração para o design dos componentes
- [django-tailwind](https://github.com/timonweb/django-tailwind) - Integração Django + Tailwind CSS
- [Alpine.js](https://alpinejs.dev/) - Framework JavaScript reativo 