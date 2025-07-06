### O que é o cazenga/ui?

**cazenga/ui** não é mais uma biblioteca de componentes tradicional para Django. Em vez de te prender a um pacote com estilos e lógicas que não podes controlar, cazenga/ui oferece uma abordagem radicalmente diferente: **dá-te a posse total do teu código.**

Funciona assim: em vez de importares uma "caixa preta", usas a nossa interface de linha de comando (`manage.py ui`) para adicionar componentes diretamente ao teu projeto. O código-fonte (HTML, classes Tailwind, lógica Alpine.js) é copiado para a tua pasta de templates. A partir desse momento, ele é teu. Podes modificá-lo, adaptá-lo e estilizá-lo como quiseres, sem restrições.

### Objetivo

O nosso objetivo é preencher a lacuna entre o desenvolvimento rápido de back-end do Django e as práticas de front-end modernas, oferecendo o melhor dos dois mundos:

1.  **Velocidade e Consistência:** Começa com uma base de componentes bem construídos, acessíveis e esteticamente agradáveis, permitindo-te criar interfaces complexas em minutos.
2.  **Controlo Total:** Porque o código é teu, nunca vais ter de "lutar contra o framework". Precisas de um botão ligeiramente diferente? Abre o ficheiro e edita. Sem `!important`, sem overrides complexos.
3.  **Leve e Performático:** Usa a stack `Django Templates + Tailwind CSS + Alpine.js`, evitando a necessidade de frameworks JavaScript pesados para a maioria dos projetos SaaS, sistemas de gestão e websites.

> **Pensa nisto como um conjunto de receitas, não um restaurante de fast-food. Nós damos-te os ingredientes e as instruções; tu cozinhas o prato perfeito para o teu projeto.**

### Características Principais

*   **Instalação via CLI:** Usa `python manage.py ui add <componente>` para adicionar apenas os componentes de que precisas.
*   **Construído com Tailwind CSS:** Todos os componentes são estilizados com classes de utilidade do Tailwind, tornando a personalização e o *theming* incrivelmente fáceis.
*   **Interatividade com Alpine.js:** Componentes complexos como Modais, Dropdowns e Tabs são alimentados pelo Alpine.js, o "Tailwind para JavaScript", mantendo a lógica diretamente no teu HTML.
*   **Acessibilidade em Primeiro Lugar:** Inspiramo-nos nas melhores práticas de acessibilidade (ARIA roles, navegação por teclado) para garantir que as tuas aplicações são utilizáveis por todos.
*   **Composição é a Chave:** Os componentes são desenhados para serem combinados. Um `Dialog` pode usar um `Card` no seu interior, que por sua vez contém `Button`s.

### Para Quem é o cazenga/ui?

Esta biblioteca é para o developer Django que:
*   Adora a simplicidade e o poder do render do lado do servidor.
*   Quer criar interfaces modernas e elegantes sem a complexidade de um SPA (Single-Page Application).
*   Valoriza a posse e o controlo sobre o seu código-fonte.
*   Já usa ou quer usar Tailwind CSS nos seus projetos.

Se estás cansado de lutar com Bootstrap ou de sentir que precisas de React para criar um simples dropdown, **cazenga/ui** é para ti.

---

### **Plano de Projeto: Criação da Biblioteca cazenga/ui**

**Objetivo:** Criar uma biblioteca de componentes UI para Django, instalável via `pip`, que utiliza um *management command* para copiar componentes para o projeto do utilizador.
**Stack Tecnológica:** Django, Tailwind CSS, Alpine.js.
**Nome do Pacote:** `django-cazenga-ui`
**Nome da App Django:** `cazenga_ui`

---

### **Fase 1: Configuração do Projeto da Biblioteca**

Nesta fase, vamos criar a estrutura do pacote Python que será publicado no PyPI.

**Passo 1: Criar a Estrutura de Ficheiros**
Cria uma pasta principal para o teu projeto e, dentro dela, a estrutura da app Django.

```
django-cazenga-ui/
├── .gitignore
├── cazenga_ui/
│   ├── __init__.py
│   ├── apps.py
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── ui.py
│   ├── templates_source/  # <-- Ficheiros de componentes fonte
│   │   └── ui/
│   │       └── (aqui viverão os teus componentes .html)
│   └── templatetags/      # <-- Para helpers personalizados se necessário
│       ├── __init__.py
│       └── cazenga_ui_tags.py
├── pyproject.toml
├── README.md
└── setup.cfg # Ficheiro opcional para configurações extra
```

**Passo 2: Configurar `pyproject.toml`**
Este é o coração da configuração do teu pacote.

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "django-cazenga-ui"
version = "0.0.1" # Começa com uma versão inicial
authors = [
    { name="O Teu Nome", email="o.teu@email.com" },
]
description = "Uma coleção de componentes UI para Django, lindamente desenhados e que podes copiar e colar no teu projeto. Inspirado em shadcn/ui."
readme = "README.md"
license = { file="LICENSE.txt" } # Adiciona um ficheiro de licença (MIT é uma boa escolha)
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3",
    "Framework :: Django",
    "Framework :: Django :: 4.2",
    "Framework :: Django :: 5.0",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
dependencies = [
    "Django>=4.2",
]

[project.urls]
Homepage = "https://github.com/teu-username/django-cazenga-ui"
Repository = "https://github.com/teu-username/django-cazenga-ui"
```

**Passo 3: Configurar a App Django (`cazenga_ui/apps.py`)**
Define a configuração da tua app.

```python
# cazenga_ui/apps.py
from django.apps import AppConfig

class CazengaUiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cazenga_ui'
    verbose_name = "Cazenga UI"
```

---

### **Fase 2: Desenvolvimento do Core - O Management Command**

Este é o mecanismo que copia os componentes para o projeto do utilizador.

**Passo 1: Escrever o Comando `ui.py`**
Este ficheiro terá a lógica para listar e adicionar componentes.

```python
# cazenga_ui/management/commands/ui.py
import os
import shutil
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Caminho para os templates fonte dentro do pacote
SOURCE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'templates_source', 'ui')

class Command(BaseCommand):
    help = 'Manage Cazenga UI components.'

    def add_arguments(self, parser):
        parser.add_argument('command', type=str, choices=['add', 'list'], help="Command to execute ('add' or 'list').")
        parser.add_argument('component_name', type=str, nargs='?', help="The name of the component to add (e.g., 'button').")

    def handle(self, *args, **options):
        command = options['command']

        if command == 'list':
            self.list_components()
        elif command == 'add':
            component_name = options['component_name']
            if not component_name:
                raise CommandError("You must provide a component name to add. Use 'list' to see available components.")
            self.add_component(component_name)

    def list_components(self):
        self.stdout.write(self.style.SUCCESS("Available components:"))
        try:
            components = [f.replace('.html', '') for f in os.listdir(SOURCE_DIR) if f.endswith('.html')]
            for component in sorted(components):
                self.stdout.write(f"- {component}")
        except FileNotFoundError:
            self.stdout.write(self.style.WARNING("No components found in the library source."))

    def add_component(self, component_name):
        source_file = os.path.join(SOURCE_DIR, f'{component_name}.html')
        
        if not os.path.exists(source_file):
            raise CommandError(f"Component '{component_name}' not found. Use 'list' to see available components.")

        # Caminho de destino personalizável via settings.py, com um padrão sensato
        destination_root = getattr(settings, 'CAZENGA_UI_DIR', os.path.join(settings.BASE_DIR, 'templates', 'components'))
        destination_dir = os.path.join(destination_root, 'ui')
        
        os.makedirs(destination_dir, exist_ok=True)
        destination_file = os.path.join(destination_dir, f'{component_name}.html')

        if os.path.exists(destination_file):
            overwrite = input(f"Component '{component_name}' already exists. Overwrite? [y/N]: ")
            if overwrite.lower() != 'y':
                self.stdout.write(self.style.NOTICE("Operation cancelled."))
                return

        self.stdout.write(f"Adding '{component_name}' component to your project...")
        try:
            shutil.copyfile(source_file, destination_file)
            self.stdout.write(self.style.SUCCESS(f"Successfully added '{component_name}.html' to '{destination_dir}'"))
            self.stdout.write(self.style.NOTICE(f"\nDon't forget to configure your tailwind.config.js to scan '{destination_root}/**/*.html' for classes!"))
        except Exception as e:
            raise CommandError(f"Failed to copy component: {e}")

```

---

### **Fase 3: Criação dos Componentes UI**

Esta é a parte criativa. Vais criar os ficheiros `.html` que serão a tua biblioteca. Começa pelos mais básicos.

**Roteiro de Componentes (ordem sugerida):**

#### Grupo 1: Os Fundamentais
1.  **`button.html`**: O componente mais essencial. Com `variant`, `size` e suporte para atributos extra.
2.  **`card.html`**: Um contentor com sub-partes (`CardHeader`, `CardContent`, `CardFooter`). Podes fazê-lo num só ficheiro ou usar `{% block %}` para composição.
3.  **`input.html`**: Inclui `<label>`, `<input>` e espaço para texto de ajuda/erro.
4.  **`alert.html`**: Para feedback. Com `variant` (info, success, warning, destructive) e um ícone.

*Exemplo de `cazenga_ui/templates_source/ui/button.html` (como visto anteriormente):*
```html
{#
  Component: Button
  Docs: Renders a button with variants and sizes.
  
  Usage: {% include 'components/ui/button.html' with ... %}
  
  Params:
    - text: (str) The button text.
    - variant: (str) 'default', 'destructive', 'outline', 'secondary', 'ghost', 'link'. Default: 'default'.
    - size: (str) 'default', 'sm', 'lg', 'icon'. Default: 'default'.
    - class: (str) Extra CSS classes.
    - attrs: (str) Extra HTML attributes (e.g., 'type="submit"').
#}
{% set base_classes = "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50" %}

{% set variants = {
  'default': 'bg-primary text-primary-foreground hover:bg-primary/90',
  'destructive': 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
  'outline': 'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
  'secondary': 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
  'ghost': 'hover:bg-accent hover:text-accent-foreground',
  'link': 'text-primary underline-offset-4 hover:underline'
} %}

{% set sizes = {
  'default': 'h-10 px-4 py-2',
  'sm': 'h-9 rounded-md px-3',
  'lg': 'h-11 rounded-md px-8',
  'icon': 'h-10 w-10'
} %}

<button
  class="{{ base_classes }} {{ variants[variant|default('default')] }} {{ sizes[size|default('default')] }} {{ class }}"
  {{ attrs|safe }}
>
  {{ text }}
</button>
```

#### Grupo 2: Componentes Interativos (com Alpine.js)
5.  **`dialog.html`** (Modal): Usa `x-data="{ open: false }"`.
6.  **`dropdown-menu.html`**: Usa `x-data="{ open: false }" @click.outside="open = false"`.
7.  **`accordion.html`**: Usa `x-data` para controlar o item ativo.
8.  **`tabs.html`**: Usa `x-data` para gerir o `activeTab`.

#### Grupo 3: Formulários Avançados
9.  `checkbox.html`
10. `radio-group.html`
11. `switch.html` (Toggle)
12. `textarea.html`
13. `select.html`

#### Grupo 4: Exibição de Dados e Feedback
14. `table.html`
15. `badge.html`
16. `avatar.html`
17. `skeleton.html`
18. `toast.html` (Este é complexo, envolve um "dispatcher" de eventos em Alpine.js).
19. `tooltip.html`

**Dica:** Cria uma documentação simples no topo de cada ficheiro de componente usando comentários `{# ... #}`, explicando como usar e quais os parâmetros disponíveis.

---

### **Fase 4: Teste Local**

Antes de publicar, tens de testar o teu pacote num projeto Django real.

**Passo 1: Criar um Projeto Django de Teste**
Fora da pasta `django-cazenga-ui`, cria um novo projeto:
```bash
django-admin startproject test_project
cd test_project
```

**Passo 2: Instalar a Tua Biblioteca em Modo Editável**
Isto permite-te fazer alterações na biblioteca e vê-las refletidas imediatamente no teu projeto de teste, sem reinstalar.

```bash
pip install -e /caminho/para/o/teu/projeto/django-cazenga-ui
```

**Passo 3: Configurar o Projeto de Teste**
1.  Adiciona `'cazenga_ui'` e `'tailwind'` a `INSTALLED_APPS`.
2.  Configura o `django-tailwind` e o `tailwind.config.js`.
3.  Cria uma view e um template de demonstração.

**Passo 4: Usar o Comando e Testar**
```bash
python manage.py ui list
# Deverá mostrar a lista dos teus componentes.

python manage.py ui add button
# Deverá copiar o button.html para a tua pasta de templates.
```

No teu template de teste, inclui o componente e verifica se ele renderiza corretamente.
```django
{# test_project/templates/demo.html #}
{% include 'components/ui/button.html' with text='Funciona!' %}
```

---

### **Fase 5: Documentação e Publicação**

**Passo 1: Escrever um `README.md` de Qualidade**
Este é o cartão de visita do teu projeto. Deve incluir:
*   O que é o `cazenga/ui`.
*   Como instalar (`pip install django-cazenga-ui`).
*   Como configurar (adicionar a `INSTALLED_APPS`, configurar o Tailwind).
*   Como usar (`python manage.py ui add ...`, exemplos de `include`).
*   Exemplo de `tailwind.config.js` para o utilizador final.

**Passo 2: Empacotar e Publicar**
1.  **Cria contas:** Precisas de uma conta no [PyPI](https://pypi.org/) e no [TestPyPI](https://test.pypi.org/) (para testar o processo de upload).
2.  **Instala as ferramentas:** `pip install build twine`.
3.  **Constrói o pacote:** `python -m build`.
4.  **Faz o upload para o TestPyPI primeiro:** `twine upload --repository testpypi dist/*`.
5.  **Testa a instalação a partir do TestPyPI:** `pip install --index-url https://test.pypi.org/simple/ django-cazenga-ui`.
6.  **Se tudo correr bem, faz o upload para o PyPI oficial:** `twine upload dist/*`.

Parabéns! A tua biblioteca `cazenga/ui` está agora disponível para o mundo.