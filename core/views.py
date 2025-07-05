from django.shortcuts import render, get_object_or_404
from django.http import Http404
import json

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

def test(request):
    return render(request, "test.html")

def demo_simple(request):
    return render(request, "demo_simple.html")

def demo_especializado(request):
    return render(request, "demo_especializado.html")

def demo_clean(request):
    return render(request, "demo_clean.html")

def navigation_demo(request):
    """Página de demonstração dos componentes de navegação"""
    # Menu simples para o simple-nav
    nav_menu = [
        {'title': 'Início', 'href': '/'},
        {'title': 'Componentes', 'href': '/components/'},
        {'title': 'Visão Geral', 'href': '/demo-clean/'},
        {'title': 'Demo Completa', 'href': '/demo/'},
    ]
    
    # Menu complexo para o navigation-menu
    complex_nav_menu = [
        {
            'title': 'Produtos',
            'href': '/produtos',
            'description': 'Nossos produtos e serviços',
            'submenu': [
                {'title': 'Categoria A', 'href': '/produtos/categoria-a', 'description': 'Produtos da categoria A'},
                {'title': 'Categoria B', 'href': '/produtos/categoria-b', 'description': 'Produtos da categoria B'},
                {'title': 'Categoria C', 'href': '/produtos/categoria-c', 'description': 'Produtos da categoria C'},
            ]
        },
        {
            'title': 'Serviços',
            'href': '/servicos',
            'description': 'Nossos serviços especializados',
            'submenu': [
                {'title': 'Consultoria', 'href': '/servicos/consultoria', 'description': 'Consultoria especializada'},
                {'title': 'Desenvolvimento', 'href': '/servicos/desenvolvimento', 'description': 'Desenvolvimento de software'},
                {'title': 'Suporte', 'href': '/servicos/suporte', 'description': 'Suporte técnico'},
            ]
        },
        {
            'title': 'Sobre',
            'href': '/sobre'
        },
        {
            'title': 'Contato',
            'href': '/contato'
        }
    ]
    
    # Menubar para demo
    demo_menubar = [
        {
            'title': 'Arquivo',
            'items': [
                {'title': 'Novo', 'shortcut': 'Ctrl+N', 'action': 'alert("Novo arquivo")'},
                {'title': 'Abrir', 'shortcut': 'Ctrl+O', 'action': 'alert("Abrir arquivo")'},
                {'title': 'Salvar', 'shortcut': 'Ctrl+S', 'action': 'alert("Salvar arquivo")'},
                {'separator': True},
                {'title': 'Sair', 'shortcut': 'Ctrl+Q', 'action': 'alert("Sair")', 'variant': 'destructive'}
            ]
        },
        {
            'title': 'Editar',
            'items': [
                {'title': 'Desfazer', 'shortcut': 'Ctrl+Z', 'action': 'alert("Desfazer")'},
                {'title': 'Refazer', 'shortcut': 'Ctrl+Y', 'action': 'alert("Refazer")'},
                {'separator': True},
                {'title': 'Copiar', 'shortcut': 'Ctrl+C', 'action': 'alert("Copiar")'},
                {'title': 'Colar', 'shortcut': 'Ctrl+V', 'action': 'alert("Colar")'}
            ]
        },
        {
            'title': 'Visualizar',
            'items': [
                {'title': 'Zoom In', 'shortcut': 'Ctrl++', 'action': 'alert("Zoom In")'},
                {'title': 'Zoom Out', 'shortcut': 'Ctrl+-', 'action': 'alert("Zoom Out")'},
                {'title': 'Tela Cheia', 'shortcut': 'F11', 'action': 'alert("Tela Cheia")'}
            ]
        }
    ]
    
    context = {
        'nav_menu': nav_menu,
        'complex_nav_menu': complex_nav_menu,
        'demo_menubar': demo_menubar,
    }
    return render(request, 'navigation-demo.html', context)

def components_list(request):
    """Página principal dos componentes com sidebar"""
    # Menu de navegação
    nav_menu = [
        {'title': 'Início', 'href': '/'},
        {'title': 'Componentes', 'href': '/components/'},
        {'title': 'Visão Geral', 'href': '/demo-clean/'},
        {'title': 'Demo Completa', 'href': '/demo/'},
    ]
    
    # Conteúdo da sidebar
    sidebar_content = {
        'header': {
            'title': 'Componentes',
            'logo': '<svg class="size-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12a7.5 7.5 0 0015 0m-15 0a7.5 7.5 0 1115 0m-15 0H3m16.5 0H21m-1.5 0H12m-8.457 3.077l1.41-.513m14.095-5.13l1.41-.513M5.106 17.785l1.15-.964m11.49-9.642l1.149-.964M7.501 19.795l.75-1.3m7.5-12.99l.75-1.3m-6.063 16.658l.26-1.477m2.605-14.772l.26-1.477m0 17.726l-.26-1.477M10.698 4.614l-.26-1.477M16.5 19.794l-.75-1.299M7.5 4.205L12 12m6.894 5.785l-1.149-.964M6.256 7.178l-1.15-.964m15.352 8.864l-1.41-.513M4.954 9.435l-1.41-.513M12.002 12l-3.75 6.495"/></svg>'
        },
        'menu': []
    }
    
    # Adicionar componentes ao menu da sidebar
    for component in COMPONENTS_LIST:
        sidebar_content['menu'].append({
            'title': component['name'],
            'href': f"/components/{component['slug']}/",
            'active': False
        })
    
    context = {
        'components_list': COMPONENTS_LIST,
        'current_component': None,
        'nav_menu': nav_menu,
        'sidebar_content': sidebar_content,
    }
    return render(request, 'components_base.html', context)

def component_detail(request, component_slug):
    """Página de demonstração de um componente específico"""
    # Verificar se o componente existe
    component = None
    for comp in COMPONENTS_LIST:
        if comp['slug'] == component_slug:
            component = comp
            break
    
    if not component:
        raise Http404("Componente não encontrado")
    
    # Menu de navegação
    nav_menu = [
        {'title': 'Início', 'href': '/'},
        {'title': 'Componentes', 'href': '/components/'},
        {'title': 'Visão Geral', 'href': '/demo-clean/'},
        {'title': 'Demo Completa', 'href': '/demo/'},
    ]
    
    # Conteúdo da sidebar
    sidebar_content = {
        'header': {
            'title': 'Componentes',
            'logo': '<svg class="size-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12a7.5 7.5 0 0015 0m-15 0a7.5 7.5 0 1115 0m-15 0H3m16.5 0H21m-1.5 0H12m-8.457 3.077l1.41-.513m14.095-5.13l1.41-.513M5.106 17.785l1.15-.964m11.49-9.642l1.149-.964M7.501 19.795l.75-1.3m7.5-12.99l.75-1.3m-6.063 16.658l.26-1.477m2.605-14.772l.26-1.477m0 17.726l-.26-1.477M10.698 4.614l-.26-1.477M16.5 19.794l-.75-1.299M7.5 4.205L12 12m6.894 5.785l-1.149-.964M6.256 7.178l-1.15-.964m15.352 8.864l-1.41-.513M4.954 9.435l-1.41-.513M12.002 12l-3.75 6.495"/></svg>'
        },
        'menu': []
    }
    
    # Adicionar componentes ao menu da sidebar
    for comp in COMPONENTS_LIST:
        sidebar_content['menu'].append({
            'title': comp['name'],
            'href': f"/components/{comp['slug']}/",
            'active': comp['slug'] == component_slug
        })
    
    context = {
        'components_list': COMPONENTS_LIST,
        'current_component': component_slug,
        'component': component,
        'nav_menu': nav_menu,
        'sidebar_content': sidebar_content,
    }
    
    # Tentar renderizar template específico do componente
    template_name = f'components/demos/{component_slug}.html'
    try:
        return render(request, template_name, context)
    except:
        # Se não existir template específico, usar template padrão
        return render(request, 'components/demos/default.html', context)
