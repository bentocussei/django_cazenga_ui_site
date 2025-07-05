from django.shortcuts import render, get_object_or_404
from django.http import Http404
import json
import os
from django.conf import settings

# Lista de componentes disponíveis
COMPONENTS_LIST = [
    {'name': 'Accordion', 'slug': 'accordion'},
    {'name': 'Alert', 'slug': 'alert'},
    {'name': 'Avatar', 'slug': 'avatar'},
    {'name': 'Badge', 'slug': 'badge'},
    {'name': 'Button', 'slug': 'button'},
    {'name': 'Card', 'slug': 'card'},
    {'name': 'Checkbox', 'slug': 'checkbox'},
    {'name': 'Input', 'slug': 'input'},
    {'name': 'Label', 'slug': 'label'},
    {'name': 'Layout', 'slug': 'layout'},
    {'name': 'Progress', 'slug': 'progress'},
    {'name': 'Select', 'slug': 'select'},
    {'name': 'Separator', 'slug': 'separator'},
    {'name': 'Skeleton', 'slug': 'skeleton'},
    {'name': 'Switch', 'slug': 'switch'},
    {'name': 'Table', 'slug': 'table'},
    {'name': 'Tabs', 'slug': 'tabs'},
    {'name': 'Textarea', 'slug': 'textarea'},
    {'name': 'Tooltip', 'slug': 'tooltip'},
]

# Dados das tabelas de parâmetros
BUTTON_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do botão'],
        ['<code>variant</code>', 'string', 'default', 'Variante do botão: default, secondary, destructive, outline, ghost, link'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do botão: sm, md, lg'],
        ['<code>type</code>', 'string', 'button', 'Tipo do botão: button, submit, reset'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o botão está desabilitado'],
        ['<code>x_click</code>', 'string', '-', 'Evento Alpine.js para clique'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

CARD_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do card'],
        ['<code>description</code>', 'string', '-', 'Descrição do card'],
        ['<code>content</code>', 'string/HTML', '-', 'Conteúdo principal do card (aceita HTML)'],
        ['<code>footer</code>', 'string/HTML', '-', 'Conteúdo do footer (aceita HTML)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

INPUT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>type</code>', 'string', 'text', 'Tipo do input: text, email, password, number, etc.'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>placeholder</code>', 'string', '-', 'Texto de placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor inicial'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>readonly</code>', 'boolean', 'false', 'Se o campo é somente leitura'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>min</code>', 'number', '-', 'Valor mínimo (para type="number")'],
        ['<code>max</code>', 'number', '-', 'Valor máximo (para type="number")'],
    ]
}

LAYOUT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>layout_type</code>', 'string', 'sidebar-left', 'Tipo de layout: sidebar-left, sidebar-right, header-only, sidebar-only, full'],
        ['<code>sidebar_collapsible</code>', 'boolean', 'true', 'Se a sidebar pode ser recolhida'],
        ['<code>sidebar_width</code>', 'string', 'w-64', 'Largura da sidebar (classes Tailwind)'],
        ['<code>sidebar_collapsed_width</code>', 'string', 'w-16', 'Largura da sidebar quando recolhida'],
        ['<code>header_height</code>', 'string', 'h-16', 'Altura do header (classes Tailwind)'],
        ['<code>footer_height</code>', 'string', 'h-16', 'Altura do footer (classes Tailwind)'],
        ['<code>sidebar_content</code>', 'HTML', '-', 'Conteúdo personalizado da sidebar'],
        ['<code>header_content</code>', 'HTML', '-', 'Conteúdo personalizado do header'],
        ['<code>main_content</code>', 'HTML', '-', 'Conteúdo principal da página'],
        ['<code>footer_content</code>', 'HTML', '-', 'Conteúdo personalizado do footer'],
        ['<code>sidebar_class</code>', 'string', '-', 'Classes CSS adicionais para a sidebar'],
        ['<code>header_class</code>', 'string', '-', 'Classes CSS adicionais para o header'],
        ['<code>main_class</code>', 'string', '-', 'Classes CSS adicionais para o main'],
        ['<code>footer_class</code>', 'string', '-', 'Classes CSS adicionais para o footer'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais para o container principal'],
    ]
}

# Create your views here.

def index(request):
    return render(request, "index.html")

def demo(request):
    # Dados para os tabs
    tabs_data = [
        {
            "id": "account", 
            "label": "Conta", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Configurações da Conta</h3><p>Gerencie suas informações pessoais e preferências de conta.</p></div>"
        },
        {
            "id": "password", 
            "label": "Senha", 
            "icon": "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z' /></svg>", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Alterar Senha</h3><p>Atualize sua senha regularmente para manter sua conta segura.</p></div>"
        },
        {
            "id": "notifications", 
            "label": "Notificações", 
            "content": "<div class='space-y-4'><h3 class='text-lg font-medium'>Preferências de Notificação</h3><p>Escolha quais notificações você deseja receber.</p></div>"
        }
    ]
    
    # Dados para toggle-group (versão completa)
    # Alinhamento
    toggle_alignment_items = ["left", "center", "right"]
    toggle_alignment_labels = ["Esquerda", "Centro", "Direita"]
    toggle_alignment_icons = [
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12' /></svg>",
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5' /></svg>",
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M3.75 6.75h16.5M3.75 12h16.5M12 17.25h8.25' /></svg>"
    ]
    
    # Formatação
    toggle_formatting_items = ["bold", "italic", "underline"]
    toggle_formatting_labels = ["Negrito", "Itálico", "Sublinhado"]
    toggle_formatting_icons = [
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M6.75 3v18M6.75 3h7.5a3.75 3.75 0 0 1 3.75 3.75v0a3.75 3.75 0 0 1-3.75 3.75H6.75M6.75 10.5h7.5a3.75 3.75 0 0 1 3.75 3.75v0a3.75 3.75 0 0 1-3.75 3.75H6.75' /></svg>",
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M5.25 3v18L12 15.75 18.75 21V3H5.25Z' /></svg>",
        "<svg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke-width='1.5' stroke='currentColor'><path stroke-linecap='round' stroke-linejoin='round' d='M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5' /></svg>"
    ]
    
    # Tamanhos
    toggle_size_items = ["sm", "md", "lg"]
    toggle_size_labels = ["Pequeno", "Médio", "Grande"]
    
    # Dados para resizable
    resizable_horizontal_panels = ["sidebar", "main"]
    resizable_horizontal_contents = [
        "<div class='space-y-3'><h4 class='font-medium'>Sidebar</h4><nav class='space-y-1'><a href='#' class='block px-2 py-1 text-sm hover:bg-accent rounded'>Dashboard</a><a href='#' class='block px-2 py-1 text-sm hover:bg-accent rounded'>Usuários</a><a href='#' class='block px-2 py-1 text-sm hover:bg-accent rounded'>Relatórios</a></nav></div>",
        "<div class='space-y-3'><h4 class='font-medium'>Conteúdo Principal</h4><p class='text-sm text-muted-foreground'>Aqui fica o conteúdo principal da aplicação. Você pode redimensionar os painéis arrastando a barra central.</p><div class='grid grid-cols-2 gap-4 mt-4'><div class='p-3 bg-muted rounded'><p class='text-sm font-medium'>Card 1</p></div><div class='p-3 bg-muted rounded'><p class='text-sm font-medium'>Card 2</p></div></div></div>"
    ]
    resizable_horizontal_sizes = [25, 75]
    
    resizable_vertical_panels = ["header", "content"]
    resizable_vertical_contents = [
        "<div class='space-y-2'><h4 class='font-medium'>Header</h4><p class='text-sm text-muted-foreground'>Área do cabeçalho com informações importantes.</p></div>",
        "<div class='space-y-2'><h4 class='font-medium'>Conteúdo</h4><p class='text-sm text-muted-foreground'>Área principal do conteúdo. Redimensione arrastando a barra horizontal.</p><div class='mt-4 space-y-2'><div class='p-2 bg-muted rounded text-sm'>Item 1</div><div class='p-2 bg-muted rounded text-sm'>Item 2</div><div class='p-2 bg-muted rounded text-sm'>Item 3</div></div></div>"
    ]
    resizable_vertical_sizes = [30, 70]
    
    # Dados para carousel (exemplo)
    carousel_images = [
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop",
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=400&fit=crop", 
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=400&fit=crop"
    ]
    carousel_titles = ["Paisagem 1", "Paisagem 2", "Paisagem 3"]
    carousel_descriptions = [
        "Uma bela vista montanhosa ao amanhecer",
        "Floresta densa com névoa matinal", 
        "Campo aberto sob céu estrelado"
    ]
    
    # Dados para gráficos
    chart_line_data = {
        "labels": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "datasets": [
            {
                "label": "Vendas 2024",
                "data": [12, 19, 3, 5, 2, 3]
            },
            {
                "label": "Vendas 2023", 
                "data": [2, 3, 20, 5, 1, 4]
            }
        ]
    }
    
    chart_bar_data = {
        "labels": ["Produto A", "Produto B", "Produto C", "Produto D"],
        "datasets": [
            {
                "label": "Vendas",
                "data": [65, 59, 80, 81]
            }
        ]
    }
    
    chart_pie_data = {
        "labels": ["Desktop", "Mobile", "Tablet"],
        "datasets": [
            {
                "label": "Dispositivos",
                "data": [55, 35, 10]
            }
        ]
    }
    
    context = {
        'tabs_data': tabs_data,
        'toggle_alignment_items': toggle_alignment_items,
        'toggle_alignment_labels': toggle_alignment_labels,
        'toggle_alignment_icons': toggle_alignment_icons,
        'toggle_formatting_items': toggle_formatting_items,
        'toggle_formatting_labels': toggle_formatting_labels,
        'toggle_formatting_icons': toggle_formatting_icons,
        'toggle_size_items': toggle_size_items,
        'toggle_size_labels': toggle_size_labels,
        'resizable_horizontal_panels': resizable_horizontal_panels,
        'resizable_horizontal_contents': resizable_horizontal_contents,
        'resizable_horizontal_sizes': resizable_horizontal_sizes,
        'resizable_vertical_panels': resizable_vertical_panels,
        'resizable_vertical_contents': resizable_vertical_contents,
        'resizable_vertical_sizes': resizable_vertical_sizes,
        'carousel_images': carousel_images,
        'carousel_titles': carousel_titles,
        'carousel_descriptions': carousel_descriptions,
        'chart_line_data': json.dumps(chart_line_data),
        'chart_bar_data': json.dumps(chart_bar_data),
        'chart_pie_data': json.dumps(chart_pie_data),
    }
    
    return render(request, "demo.html", context)

def components_list(request):
    # Construir conteúdo da sidebar
    sidebar_content = '<nav class="space-y-1">'
    for component in COMPONENTS_LIST:
        icon_mapping = {
            'button': 'button', 'input': 'input', 'card': 'card-stack', 'table': 'table',
            'alert': 'bell', 'avatar': 'avatar', 'badge': 'badge', 'checkbox': 'checkbox',
            'accordion': 'chevron-down', 'progress': 'timer', 'select': 'caret-sort',
            'separator': 'dash', 'skeleton': 'transparency-grid', 'switch': 'switch',
            'tabs': 'dots-horizontal', 'textarea': 'text-align-top', 'tooltip': 'question-mark-circled',
            'label': 'pilcrow', 'layout': 'layout'
        }
        icon_name = icon_mapping.get(component['slug'], 'dot-filled')
        
        sidebar_content += f'''
        <a href="/components/{component['slug']}/" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium hover:bg-accent transition-colors">
            <img src="/static/radix-icons/{icon_name}.svg" class="size-4" alt="{component['name']}">
            <span x-show="!sidebarCollapsed || isMobile">{component['name']}</span>
        </a>
        '''
    sidebar_content += '</nav>'
    
    # Construir conteúdo do header
    header_content = '''
    <div class="flex items-center gap-4">
        <a href="/" class="text-xl font-bold">Django + Tailwind + Alpine.js</a>
        <nav class="hidden md:flex space-x-4">
            <a href="/" class="text-sm font-medium hover:text-primary transition-colors">Início</a>
            <a href="/components/" class="text-sm font-medium text-primary">Componentes</a>
            <a href="/demo/" class="text-sm font-medium hover:text-primary transition-colors">Demo</a>
            <a href="/icons/" class="text-sm font-medium hover:text-primary transition-colors">Ícones</a>
        </nav>
    </div>
    <div class="flex items-center gap-4">
        <button @click="darkMode = !darkMode" class="size-8 rounded-radius-md hover:bg-accent transition-colors flex items-center justify-center">
            <span x-show="!darkMode"><img src="/static/radix-icons/moon.svg" class="size-4" alt="Modo escuro"></span>
            <span x-show="darkMode"><img src="/static/radix-icons/sun.svg" class="size-4" alt="Modo claro"></span>
        </button>
    </div>
    '''
    
    # Construir conteúdo principal
    main_content = '''
    <div class="space-y-6">
        <div class="border-b border-border pb-4">
            <div class="flex items-center justify-between">
                <div>
                    <h1 class="text-3xl font-bold">Componentes</h1>
                    <p class="text-muted-foreground mt-1">Selecione um componente para ver a demonstração</p>
                </div>
                <a href="/" class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
                    Voltar
                </a>
            </div>
        </div>
        <div class="text-center py-12">
            <div class="text-6xl mb-4">🎨</div>
            <h3 class="text-xl font-semibold mb-2">Selecione um Componente</h3>
            <p class="text-muted-foreground">Escolha um componente no sidebar para ver a demonstração completa</p>
        </div>
    </div>
    '''
    
    context = {
        'components_list': COMPONENTS_LIST,
        'sidebar_content': sidebar_content,
        'header_content': header_content,
        'main_content': main_content,
    }
    return render(request, "components_base.html", context)

def component_detail(request, component_slug):
    # Encontrar o componente
    component = None
    for comp in COMPONENTS_LIST:
        if comp['slug'] == component_slug:
            component = comp
            break
    
    if not component:
        raise Http404("Componente não encontrado")
    
    # Construir conteúdo da sidebar
    sidebar_content = '<nav class="space-y-1">'
    for comp in COMPONENTS_LIST:
        icon_mapping = {
            'button': 'button', 'input': 'input', 'card': 'card-stack', 'table': 'table',
            'alert': 'bell', 'avatar': 'avatar', 'badge': 'badge', 'checkbox': 'checkbox',
            'accordion': 'chevron-down', 'progress': 'timer', 'select': 'caret-sort',
            'separator': 'dash', 'skeleton': 'transparency-grid', 'switch': 'switch',
            'tabs': 'dots-horizontal', 'textarea': 'text-align-top', 'tooltip': 'question-mark-circled',
            'label': 'pilcrow', 'layout': 'layout'
        }
        icon_name = icon_mapping.get(comp['slug'], 'dot-filled')
        active_class = 'bg-accent text-accent-foreground' if comp['slug'] == component_slug else 'hover:bg-accent'
        
        sidebar_content += f'''
        <a href="/components/{comp['slug']}/" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium transition-colors {active_class}">
            <img src="/static/radix-icons/{icon_name}.svg" class="size-4" alt="{comp['name']}">
            <span x-show="!sidebarCollapsed || isMobile">{comp['name']}</span>
        </a>
        '''
    sidebar_content += '</nav>'
    
    # Construir conteúdo do header
    header_content = '''
    <div class="flex items-center gap-4">
        <a href="/" class="text-xl font-bold">Django + Tailwind + Alpine.js</a>
        <nav class="hidden md:flex space-x-4">
            <a href="/" class="text-sm font-medium hover:text-primary transition-colors">Início</a>
            <a href="/components/" class="text-sm font-medium text-primary">Componentes</a>
            <a href="/demo/" class="text-sm font-medium hover:text-primary transition-colors">Demo</a>
            <a href="/icons/" class="text-sm font-medium hover:text-primary transition-colors">Ícones</a>
        </nav>
    </div>
    <div class="flex items-center gap-4">
        <button @click="darkMode = !darkMode" class="size-8 rounded-radius-md hover:bg-accent transition-colors flex items-center justify-center">
            <span x-show="!darkMode"><img src="/static/radix-icons/moon.svg" class="size-4" alt="Modo escuro"></span>
            <span x-show="darkMode"><img src="/static/radix-icons/sun.svg" class="size-4" alt="Modo claro"></span>
        </button>
    </div>
    '''
    
    # Preparar contexto base
    context = {
        'component': component,
        'components_list': COMPONENTS_LIST,
        'current_component': component_slug,
        'sidebar_content': sidebar_content,
        'header_content': header_content,
    }
    
    # Adicionar dados específicos do componente
    if component_slug == 'button':
        context.update({
            'button_params': BUTTON_PARAMS,
        })
    elif component_slug == 'card':
        context.update({
            'card_params': CARD_PARAMS,
        })
    elif component_slug == 'input':
        context.update({
            'input_params': INPUT_PARAMS,
        })
    elif component_slug == 'layout':
        context.update({
            'layout_params': LAYOUT_PARAMS,
        })
    
    # Renderizar template específico do componente ou usar fallback
    from django.template.loader import get_template
    from django.template import TemplateDoesNotExist
    
    try:
        # Tentar carregar o template específico
        template = get_template(f"components/demos/{component_slug}.html")
        # Renderizar o template completo primeiro (pois ele estende components_base.html)
        return render(request, f"components/demos/{component_slug}.html", context)
    except TemplateDoesNotExist:
        # Template não existe, usar fallback
        main_content = f'''
        <div class="space-y-6">
            <div class="border-b border-border pb-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h1 class="text-3xl font-bold">{component['name']}</h1>
                        <p class="text-muted-foreground mt-1">Demonstração do componente {component['name']}</p>
                    </div>
                    <a href="/components/" class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
                        Voltar
                    </a>
                </div>
            </div>
            <div class="text-center py-12">
                <div class="text-6xl mb-4">🚧</div>
                <h3 class="text-xl font-semibold mb-2">Em Desenvolvimento</h3>
                <p class="text-muted-foreground">A demonstração do componente {component['name']} ainda está em desenvolvimento.</p>
            </div>
        </div>
        '''
        
        context['main_content'] = main_content
        context['component_not_found'] = True
        return render(request, "components_base.html", context)

def icons_page(request):
    import os
    from django.conf import settings
    
    # Menu de navegação
    nav_menu = [
        {
            "title": "Início",
            "href": "/",
        },
        {
            "title": "Demo",
            "href": "/demo/",
        },
        {
            "title": "Componentes",
            "href": "/components/",
        },
        {
            "title": "Ícones",
            "href": "/icons/",
        }
    ]
    
    # Caminho para os ícones na pasta static
    icons_path = os.path.join(settings.BASE_DIR, 'theme', 'static', 'radix-icons')
    icons = []
    
    try:
        # Listar todos os arquivos SVG
        for filename in os.listdir(icons_path):
            if filename.endswith('.svg'):
                icon_name = filename.replace('.svg', '')
                
                icons.append({
                    'name': icon_name,
                    'filename': filename,
                    'display_name': icon_name.replace('-', ' ').title(),
                    'static_path': f'radix-icons/{filename}'
                })
    except FileNotFoundError:
        pass
    
    # Ordenar ícones por nome
    icons.sort(key=lambda x: x['name'])
    
    context = {
        'nav_menu': nav_menu,
        'icons': icons,
        'total_icons': len(icons)
    }
    
    return render(request, "icons.html", context)
