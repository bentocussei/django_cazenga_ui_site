from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
import json
import os
from django.conf import settings
from .data import *

# Lista de componentes disponíveis
COMPONENTS_LIST = [
    {'name': 'Accordion', 'slug': 'accordion'},
    {'name': 'Alert', 'slug': 'alert'},
    {'name': 'Alert Dialog', 'slug': 'alert-dialog'},
    {'name': 'Aspect Ratio', 'slug': 'aspect-ratio'},
    {'name': 'Avatar', 'slug': 'avatar'},
    {'name': 'Badge', 'slug': 'badge'},
    {'name': 'Breadcrumb', 'slug': 'breadcrumb'},
    {'name': 'Button', 'slug': 'button'},
    {'name': 'Calendar', 'slug': 'calendar'},
    {'name': 'Card', 'slug': 'card'},
    {'name': 'Carousel', 'slug': 'carousel'},
    {'name': 'Chart', 'slug': 'chart'},
    {'name': 'Checkbox', 'slug': 'checkbox'},
    {'name': 'Collapsible', 'slug': 'collapsible'},
    {'name': 'Command', 'slug': 'command'},
    {'name': 'Content Manager', 'slug': 'content-manager'},
    {'name': 'Context Menu', 'slug': 'context-menu'},
    {'name': 'Dialog', 'slug': 'dialog'},
    {'name': 'Drawer', 'slug': 'drawer'},
    {'name': 'Dropdown', 'slug': 'dropdown'},
    {'name': 'Dropdown Menu', 'slug': 'dropdown-menu'},
    {'name': 'Form', 'slug': 'form'},
    {'name': 'Hover Card', 'slug': 'hover-card'},
    {'name': 'Input', 'slug': 'input'},
    {'name': 'Input OTP', 'slug': 'input-otp'},
    {'name': 'Label', 'slug': 'label'},
    {'name': 'Layout', 'slug': 'layout'},
    {'name': 'Menubar', 'slug': 'menubar'},
    {'name': 'Modal', 'slug': 'modal'},
    {'name': 'Navigation Menu', 'slug': 'navigation-menu'},
    {'name': 'Pagination', 'slug': 'pagination'},
    {'name': 'Popover', 'slug': 'popover'},
    {'name': 'Progress', 'slug': 'progress'},
    {'name': 'Radio Group', 'slug': 'radio-group'},
    {'name': 'Resizable', 'slug': 'resizable'},
    {'name': 'Scroll Area', 'slug': 'scroll-area'},
    {'name': 'Select', 'slug': 'select'},
    {'name': 'Separator', 'slug': 'separator'},
    {'name': 'Sheet', 'slug': 'sheet'},
    {'name': 'Sidebar', 'slug': 'sidebar'},
    {'name': 'Skeleton', 'slug': 'skeleton'},
    {'name': 'Slider', 'slug': 'slider'},
    {'name': 'Sonner', 'slug': 'sonner'},
    {'name': 'Spinner', 'slug': 'spinner'},
    {'name': 'Switch', 'slug': 'switch'},
    {'name': 'Table', 'slug': 'table'},
    {'name': 'Tabs', 'slug': 'tabs'},
    {'name': 'Text Editor', 'slug': 'text-editor'},
    {'name': 'Textarea', 'slug': 'textarea'},
    {'name': 'Toggle', 'slug': 'toggle'},
    {'name': 'Toggle Group', 'slug': 'toggle-group'},
    {'name': 'Tooltip', 'slug': 'tooltip'},
]

# Dados de fallback (para componentes ainda não migrados)
BUTTON_PARAMS_FALLBACK = {
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

CARD_PARAMS_FALLBACK = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do card'],
        ['<code>description</code>', 'string', '-', 'Descrição do card'],
        ['<code>content</code>', 'string/HTML', '-', 'Conteúdo principal do card (aceita HTML)'],
        ['<code>footer</code>', 'string/HTML', '-', 'Conteúdo do footer (aceita HTML)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

INPUT_PARAMS_FALLBACK = {
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

# Parâmetros do Layout (mantém original já que não foi migrado ainda)
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

# Função auxiliar para detectar requisições SPA
def is_spa_request(request):
    """Detecta se é uma requisição SPA (AJAX) baseada nos parâmetros ou headers"""
    is_partial = request.GET.get('partial') == 'true'
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    return is_partial or is_ajax

# Função auxiliar para retornar resposta SPA
def spa_response(request, template_name, context, page_title=None):
    """
    Retorna resposta apropriada para SPA:
    - Se for requisição AJAX, retorna JSON com conteúdo parcial
    - Se for requisição normal, retorna HTML completo
    """
    if is_spa_request(request):
        print(f"🚀 SPA Request detectada para template: {template_name}")
        
        # Para requisições SPA, vamos renderizar apenas o conteúdo principal
        # Se o contexto já tem main_content pronto, usar ele
        if 'main_content' in context:
            main_content = context['main_content']
        else:
            # Renderizar o template específico do componente apenas
            main_content = render_to_string(template_name, context, request=request)
        
        # Preparar dados para resposta JSON
        response_data = {
            'content': main_content,
            'title': page_title or context.get('page_title', ''),
            'path': request.path,
            'success': True
        }
        
        print(f"✅ SPA Response - Tamanho do conteúdo: {len(main_content)} chars")
        
        return JsonResponse(response_data)
    else:
        print(f"🔄 Request normal para template: {template_name}")
        # Requisição normal, retornar HTML completo
        return render(request, template_name, context)

# Create your views here.

def index(request):
    # Verificar se é requisição SPA
    if is_spa_request(request):
        print("🚀 SPA Request para página inicial")
        
        # Para SPA, retornar apenas o conteúdo principal
        main_content = '''
        <div class="text-center py-16">
            <h1 class="text-4xl font-bold mb-4">Bem-vindo!</h1>
            <p class="text-xl text-muted-foreground mb-8">Sistema de componentes usando Django, Tailwind CSS e Alpine.js</p>
            
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/components/" data-spa-link class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-11 px-8">
                    Ver Componentes
                </a>
                <a href="/demo/" data-spa-link class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-11 px-8">
                    Demo Completa
                </a>
            </div>
        </div>
        '''
        
        response_data = {
            'content': main_content,
            'title': 'Django Tailwind Alpine - Biblioteca de Componentes UI',
            'path': request.path,
            'success': True
        }
        
        print("✅ SPA Response enviada para página inicial")
        return JsonResponse(response_data)
    
    # Se não for SPA, continuar com o fluxo normal
    context = {
        'page_title': 'Django Tailwind Alpine - Biblioteca de Componentes UI'
    }
    return render(request, "index.html", context)

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
        'page_title': 'Demo - Componentes UI',
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
    
    return spa_response(request, "demo.html", context)

def component_detail(request, component_name):
    # Encontrar o componente
    component = None
    for comp in COMPONENTS_LIST:
        if comp['slug'] == component_name:
            component = comp
            break
    
    if not component:
        raise Http404("Componente não encontrado")
    
    # Preparar contexto base
    context = {
        'page_title': f'{component["name"]} - Componente UI',
        'component': component,
        'components_list': COMPONENTS_LIST,
        'current_component': component_name,
    }
    
    # Usar o mapeamento da nova estrutura modular
    if component_name in COMPONENT_DATA:
        component_data_context = COMPONENT_DATA[component_name]
        
        # Mapear dados específicos para cada componente
        if component_name == 'button':
            context['button_params'] = component_data_context.get('params')
        elif component_name == 'alert':
            context['alert_examples'] = component_data_context.get('examples')
            context['alert_params'] = component_data_context.get('params')
        elif component_name == 'input':
            context['input_params'] = component_data_context.get('params')
        elif component_name == 'table':
            context['table_data'] = component_data_context
            context['table_params'] = component_data_context.get('params')
        elif component_name == 'card':
            context['card_params'] = component_data_context.get('params')
        elif component_name == 'accordion':
            context['accordion_items'] = component_data_context.get('items')
            # Dados do accordion_data para diferentes seções
            accordion_data = component_data_context.get('data', {})
            context['accordion_basic_items'] = accordion_data.get('basic_items', [])
            context['accordion_advanced_items'] = accordion_data.get('advanced_items', [])
            context['accordion_params'] = component_data_context.get('params')
        elif component_name == 'aspect-ratio':
            context['aspect_ratio_data'] = component_data_context.get('data')
            context['aspect_ratio_sample_images'] = component_data_context.get('sample_images')
            context['aspect_ratio_sample_videos'] = component_data_context.get('sample_videos')
            context['aspect_ratio_params'] = component_data_context.get('params')
        elif component_name == 'avatar':
            context['avatar_examples'] = component_data_context.get('examples')
            context['avatar_params'] = component_data_context.get('params')
        elif component_name == 'badge':
            context['badge_examples'] = component_data_context.get('examples')
            context['badge_params'] = component_data_context.get('params')
        elif component_name == 'breadcrumb':
            context['breadcrumb_items'] = component_data_context.get('items')
            context['breadcrumb_data'] = component_data_context.get('data')
            context['breadcrumb_with_icons'] = component_data_context.get('with_icons')
            context['breadcrumb_params'] = component_data_context.get('params')
        elif component_name == 'calendar':
            context['calendar_events'] = component_data_context.get('events')
            context['calendar_multiple_dates'] = component_data_context.get('multiple_dates')
            context['calendar_min_date'] = component_data_context.get('min_date')
            context['calendar_max_date'] = component_data_context.get('max_date')
            context['calendar_highlight_dates'] = component_data_context.get('highlight_dates')
            context['calendar_params'] = component_data_context.get('params')
        elif component_name == 'checkbox':
            context['checkbox_params'] = component_data_context.get('params')
        elif component_name == 'progress':
            context['progress_params'] = component_data_context.get('params')
        elif component_name == 'radio-group':
            context['radio_group_options'] = component_data_context.get('options')
            context['radio_group_data'] = component_data_context.get('data')
            context['radio_group_params'] = component_data_context.get('params')
        elif component_name == 'switch':
            context['switch_params'] = component_data_context.get('params')
        elif component_name == 'tabs':
            context['tabs_data'] = component_data_context
            from .data.tabs_data import TABS_PARAMS
            context['tabs_params'] = TABS_PARAMS
        elif component_name == 'collapsible':
            collapsible_data = component_data_context.get('data', {})
            context['collapsible_basic_content'] = collapsible_data.get('basic_content')
            context['collapsible_advanced_content'] = collapsible_data.get('advanced_content')
            context['collapsible_params'] = component_data_context.get('params')
        elif component_name == 'alert-dialog':
            context['alert_dialog_params'] = component_data_context.get('params')
        elif component_name == 'dialog':
            context['dialog_params'] = component_data_context.get('params')
        # Novos componentes adicionados na FASE 1
        elif component_name == 'label':
            context['label_examples'] = component_data_context.get('examples')
            context['label_params'] = component_data_context.get('params')
        elif component_name == 'separator':
            context['separator_examples'] = component_data_context.get('examples')
            context['separator_params'] = component_data_context.get('params')
        elif component_name == 'skeleton':
            context['skeleton_examples'] = component_data_context.get('examples')
            context['skeleton_layouts'] = component_data_context.get('data', {}).get('layouts', [])
            context['skeleton_params'] = component_data_context.get('params')
        elif component_name == 'spinner':
            context['spinner_examples'] = component_data_context.get('examples')
            context['spinner_contexts'] = component_data_context.get('data', {}).get('contexts', [])
            context['spinner_params'] = component_data_context.get('params')
        elif component_name == 'toggle':
            context['toggle_examples'] = component_data_context.get('examples')
            context['toggle_groups'] = component_data_context.get('data', {}).get('groups', [])
            context['toggle_params'] = component_data_context.get('params')
        elif component_name == 'tooltip':
            context['tooltip_examples'] = component_data_context.get('examples')
            context['tooltip_placements'] = component_data_context.get('data', {}).get('placements', [])
            context['tooltip_contexts'] = component_data_context.get('data', {}).get('contexts', [])
            context['tooltip_params'] = component_data_context.get('params')
        elif component_name == 'textarea':
            context['textarea_params'] = component_data_context.get('params')
        # Novos componentes do GRUPO 1
        elif component_name == 'select':
            # Dados do select
            context['select_basic_options'] = component_data_context.get('basic_options')
            context['select_countries'] = component_data_context.get('countries')
            context['select_priority'] = component_data_context.get('priority')
            context['select_status'] = component_data_context.get('status')
            context['select_sizes'] = component_data_context.get('sizes')
            context['select_params'] = component_data_context.get('params')
        elif component_name == 'slider':
            # Dados do slider
            context['slider_basic'] = component_data_context.get('basic')
            context['slider_range'] = component_data_context.get('range')
            context['slider_volume'] = component_data_context.get('volume')
            context['slider_price'] = component_data_context.get('price')
            context['slider_opacity'] = component_data_context.get('opacity')
            context['slider_disabled'] = component_data_context.get('disabled')
            context['slider_vertical'] = component_data_context.get('vertical')
            context['slider_params'] = component_data_context.get('params')
        elif component_name == 'toggle-group':
            # Dados do toggle-group
            context['toggle_group_alignment'] = component_data_context.get('alignment')
            context['toggle_group_format'] = component_data_context.get('format')
            context['toggle_group_size'] = component_data_context.get('size')
            context['toggle_group_view'] = component_data_context.get('view')
            context['toggle_group_priority'] = component_data_context.get('priority')
            context['toggle_group_disabled'] = component_data_context.get('disabled')
            context['toggle_group_params'] = component_data_context.get('params')
        # Componentes Sonner e Form
        elif component_name == 'sonner':
            # Dados do sonner
            context['sonner_basic'] = component_data_context.get('basic')
            context['sonner_with_action'] = component_data_context.get('with_action')
            context['sonner_permanent'] = component_data_context.get('permanent')
            context['sonner_positions'] = component_data_context.get('positions')
            context['sonner_special'] = component_data_context.get('special')
            context['sonner_params'] = component_data_context.get('params')
        elif component_name == 'form':
            # Dados do form
            context['form_basic_contact'] = component_data_context.get('basic_contact')
            context['form_register'] = component_data_context.get('register')
            context['form_profile'] = component_data_context.get('profile')
            context['form_settings'] = component_data_context.get('settings')
            context['form_validation'] = component_data_context.get('validation')
            context['form_field_types'] = component_data_context.get('field_types')
            context['form_params'] = component_data_context.get('params')
        # Novos componentes corrigidos com dados
        elif component_name == 'carousel':
            # Dados do carousel
            context['carousel_basic'] = component_data_context.get('basic')
            context['carousel_autoplay'] = component_data_context.get('autoplay')
            context['carousel_simple'] = component_data_context.get('simple')
            context['carousel_params'] = component_data_context.get('params')
        elif component_name == 'drawer':
            # Dados do drawer
            context['drawer_basic'] = component_data_context.get('basic')
            context['drawer_right'] = component_data_context.get('right')
            context['drawer_footer'] = component_data_context.get('footer')
            context['drawer_params'] = component_data_context.get('params')
        elif component_name == 'dropdown':
            # Dados do dropdown
            context['dropdown_states'] = component_data_context.get('states')
            context['dropdown_colors'] = component_data_context.get('colors')
            context['dropdown_basic'] = component_data_context.get('basic')
            context['dropdown_countries'] = component_data_context.get('countries')
            context['dropdown_sizes'] = component_data_context.get('sizes')
            context['dropdown_params'] = component_data_context.get('params')
        elif component_name == 'chart':
            # Dados do chart
            context['chart_bar'] = component_data_context.get('bar')
            context['chart_pie'] = component_data_context.get('pie')
            context['chart_line'] = component_data_context.get('line')
            context['chart_metrics'] = component_data_context.get('metrics')
            context['chart_params'] = component_data_context.get('params')
        elif component_name == 'context-menu':
            # Dados do context-menu
            context['context_menu_basic'] = component_data_context.get('basic')
            context['context_menu_submenu'] = component_data_context.get('submenu')
            context['context_menu_files'] = component_data_context.get('files')
            context['context_menu_params'] = component_data_context.get('params')
        elif component_name == 'dropdown-menu':
            # Dados do dropdown-menu
            context['dropdown_menu_basic'] = component_data_context.get('basic')
            context['dropdown_menu_user'] = component_data_context.get('user')
            context['dropdown_menu_submenu'] = component_data_context.get('submenu')
            context['dropdown_menu_notifications'] = component_data_context.get('notifications')
            context['dropdown_menu_params'] = component_data_context.get('params')
        elif component_name == 'hover-card':
            # Dados do hover-card
            context['hover_card_basic'] = component_data_context.get('basic')
            context['hover_card_user'] = component_data_context.get('user')
            context['hover_card_product'] = component_data_context.get('product')
            context['hover_card_location'] = component_data_context.get('location')
            context['hover_card_params'] = component_data_context.get('params')
        elif component_name == 'layout':
            # Dados do layout
            context['layout_sidebar_left'] = component_data_context.get('sidebar_left')
            context['layout_sidebar_right'] = component_data_context.get('sidebar_right')
            context['layout_header_only'] = component_data_context.get('header_only')
            context['layout_full'] = component_data_context.get('full')
            context['layout_params'] = component_data_context.get('params')
        elif component_name == 'input-otp':
            # Dados do input-otp
            context['input_otp_basic'] = component_data_context.get('basic')
            context['input_otp_pin'] = component_data_context.get('pin')
            context['input_otp_long'] = component_data_context.get('long')
            context['input_otp_validation'] = component_data_context.get('validation')
            context['input_otp_custom'] = component_data_context.get('custom')
            context['input_otp_sizes'] = component_data_context.get('sizes')
            context['input_otp_states'] = component_data_context.get('states')
            context['input_otp_params'] = component_data_context.get('params')
        elif component_name == 'modal':
            # Dados do modal
            context['modal_basic'] = component_data_context.get('basic')
            context['modal_confirmation'] = component_data_context.get('confirmation')
            context['modal_form'] = component_data_context.get('form')
            context['modal_info'] = component_data_context.get('info')
            context['modal_fullscreen'] = component_data_context.get('fullscreen')
            context['modal_params'] = component_data_context.get('params')
        elif component_name == 'menubar':
            # Dados do menubar
            context['menubar_basic'] = component_data_context.get('basic')
            context['menubar_simple'] = component_data_context.get('simple')
            context['menubar_with_icons'] = component_data_context.get('with_icons')
            context['menubar_editor'] = component_data_context.get('editor')
            context['menubar_params'] = component_data_context.get('params')
        elif component_name == 'sheet':
            # Dados do sheet
            context['sheet_basic'] = component_data_context.get('basic')
            context['sheet_form'] = component_data_context.get('form')
            context['sheet_details'] = component_data_context.get('details')
            context['sheet_filters'] = component_data_context.get('filters')
            context['sheet_params'] = component_data_context.get('params')
        elif component_name == 'sidebar':
            # Dados do sidebar
            context['sidebar_basic'] = component_data_context.get('basic')
            context['sidebar_submenu'] = component_data_context.get('submenu')
            context['sidebar_minimal'] = component_data_context.get('minimal')
            context['sidebar_with_badges'] = component_data_context.get('with_badges')
            context['sidebar_collapsed'] = component_data_context.get('collapsed')
            context['sidebar_params'] = component_data_context.get('params')
        elif component_name == 'navigation-menu':
            # Dados do navigation-menu
            context['navigation_menu_basic'] = component_data_context.get('basic')
            context['navigation_menu_with_icons'] = component_data_context.get('with_icons')
            context['navigation_menu_vertical'] = component_data_context.get('vertical')
            context['navigation_menu_compact'] = component_data_context.get('compact')
            context['navigation_menu_mobile'] = component_data_context.get('mobile')
            context['navigation_menu_params'] = component_data_context.get('params')
        elif component_name == 'resizable':
            # Dados do resizable
            context['resizable_horizontal'] = component_data_context.get('horizontal')
            context['resizable_vertical'] = component_data_context.get('vertical')
            context['resizable_three_panels'] = component_data_context.get('three_panels')
            context['resizable_nested'] = component_data_context.get('nested')
            context['resizable_dynamic'] = component_data_context.get('dynamic')
            context['resizable_params'] = component_data_context.get('params')
        elif component_name == 'scroll-area':
            # Dados do scroll-area
            context['scroll_area_basic'] = component_data_context.get('basic')
            context['scroll_area_horizontal'] = component_data_context.get('horizontal')
            context['scroll_area_mixed'] = component_data_context.get('mixed')
            context['scroll_area_custom'] = component_data_context.get('custom')
            context['scroll_area_table'] = component_data_context.get('table')
            context['scroll_area_infinite'] = component_data_context.get('infinite')
            context['scroll_area_params'] = component_data_context.get('params')
            context['text_editor_basic'] = component_data_context.get('basic')
            context['text_editor_complete'] = component_data_context.get('complete')
            context['text_editor_minimal'] = component_data_context.get('minimal')
            context['text_editor_readonly'] = component_data_context.get('readonly')
            context['text_editor_code'] = component_data_context.get('code')
            context['text_editor_collaborative'] = component_data_context.get('collaborative')
            context['text_editor_toolbar_options'] = component_data_context.get('toolbar_options')
            context['text_editor_params'] = component_data_context.get('params')
            context['content_manager_blog'] = component_data_context.get('blog')
            context['content_manager_news'] = component_data_context.get('news')
            context['content_manager_product'] = component_data_context.get('product')
            context['content_manager_page'] = component_data_context.get('page')
            context['content_manager_field_types'] = component_data_context.get('field_types')
            context['content_manager_params'] = component_data_context.get('params')
    else:
        # Fallback para componentes ainda não migrados
        print(f"⚠️ Componente {component_name} não encontrado no COMPONENT_DATA, usando fallback")
        if component_name == 'button':
            context['button_params'] = BUTTON_PARAMS_FALLBACK
        elif component_name == 'card':
            context['card_params'] = CARD_PARAMS_FALLBACK
        elif component_name == 'input':
            context['input_params'] = INPUT_PARAMS_FALLBACK
        elif component_name == 'layout':
            context['layout_params'] = LAYOUT_PARAMS
    
    # Construir conteúdo da sidebar
    sidebar_content = '<nav class="space-y-1">'
    for comp in COMPONENTS_LIST:
        icon_mapping = {
            'accordion': 'chevron-down', 'alert': 'bell', 'alert-dialog': 'exclamation-triangle',
            'aspect-ratio': 'aspect-ratio', 'avatar': 'avatar', 'badge': 'badge',
            'breadcrumb': 'slash', 'button': 'button', 'calendar': 'calendar', 
            'card': 'card-stack', 'carousel': 'dots-horizontal', 'chart': 'bar-chart',
            'checkbox': 'checkbox', 'collapsible': 'chevron-up', 'command': 'magnifying-glass',
            'content-manager': 'clipboard', 'context-menu': 'dots-vertical', 'dialog': 'chat-bubble', 
            'drawer': 'hamburger-menu', 'dropdown': 'caret-down', 'dropdown-menu': 'dropdown-menu', 
            'form': 'clipboard', 'hover-card': 'card-stack', 'input': 'input', 'input-otp': 'lock-closed',
            'label': 'pilcrow', 'layout': 'layout', 'menubar': 'hamburger-menu',
            'modal': 'external-link', 'navigation-menu': 'hamburger-menu', 'pagination': 'dots-horizontal',
            'popover': 'chat-bubble', 'progress': 'timer', 'radio-group': 'radiobutton',
            'resizable': 'size', 'scroll-area': 'double-arrow-up', 'select': 'caret-sort',
            'separator': 'dash', 'sheet': 'hamburger-menu', 'sidebar': 'layout',
            'skeleton': 'transparency-grid', 'slider': 'slider', 'sonner': 'bell',
            'spinner': 'reload', 'switch': 'switch', 'table': 'table',
            'tabs': 'dots-horizontal', 'text-editor': 'pencil-1', 'textarea': 'text-align-top', 
            'toggle': 'switch', 'toggle-group': 'mix', 'tooltip': 'question-mark-circled'
        }
        icon_name = icon_mapping.get(comp['slug'], 'dot-filled')
        active_class = 'bg-accent text-accent-foreground' if comp['slug'] == component_name else 'hover:bg-accent'
        
        sidebar_content += f'''
        <a href="/components/{comp['slug']}/" data-spa-link class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium transition-colors {active_class}">
            <img src="/static/radix-icons/{icon_name}.svg" class="size-4" alt="{comp['name']}">
            <span x-show="!sidebarCollapsed || isMobile">{comp['name']}</span>
        </a>
        '''
    sidebar_content += '</nav>'
    
    # Construir conteúdo do header
    header_content = '''
    <div class="flex items-center gap-4">
        <a href="/" data-spa-link class="text-xl font-bold">Django Cazenga-UI</a>
        <nav class="hidden md:flex space-x-4">
            <a href="/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Início</a>
            <a href="/components/" data-spa-link class="text-sm font-medium text-primary">Componentes</a>
            <a href="/demo/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Demo</a>
            <a href="/icons/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Ícones</a>
        </nav>
    </div>
    <div class="flex items-center gap-4">
        <button @click="darkMode = !darkMode" class="size-8 rounded-radius-md hover:bg-accent transition-colors flex items-center justify-center">
            <span x-show="!darkMode"><img src="/static/radix-icons/moon.svg" class="size-4" alt="Modo escuro"></span>
            <span x-show="darkMode"><img src="/static/radix-icons/sun.svg" class="size-4" alt="Modo claro"></span>
        </button>
    </div>
    '''
    
    # Tentar renderizar template específico
    from django.template.loader import get_template
    from django.template import TemplateDoesNotExist
    
    try:
        template = get_template(f"components/demos/{component_name}.html")
        template_exists = True
        print(f"📄 Template encontrado: components/demos/{component_name}.html")
    except TemplateDoesNotExist:
        template_exists = False
        print(f"⚠️ Template não encontrado para {component_name}, usando fallback")
    
    # Construir o main_content
    if template_exists:
        main_content = render_to_string(f"components/demos/{component_name}.html", context, request=request)
    else:
        main_content = f'''
        <div class="space-y-6">
            <div class="border-b border-border pb-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h1 class="text-3xl font-bold">{component['name']}</h1>
                        <p class="text-muted-foreground mt-1">Demonstração do componente {component['name']}</p>
                    </div>
                    <a href="/components/" data-spa-link class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
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
    
    # Verificar se é requisição SPA
    if is_spa_request(request):
        print(f"🚀 SPA Request para componente: {component_name}")
        
        response_data = {
            'content': main_content,
            'title': f'{component["name"]} - Componente UI',
            'path': request.path,
            'success': True
        }
        
        print(f"✅ SPA Response enviada para {component_name}")
        return JsonResponse(response_data)
    
    # Para requisições normais
    context.update({
        'sidebar_content': sidebar_content,
        'header_content': header_content,
        'main_content': main_content,
    })
    
    return render(request, "components_base.html", context)

def components_list(request):
    # Verificar se é requisição SPA
    if is_spa_request(request):
        print("🚀 SPA Request para lista de componentes")
        
        # Para SPA, retornar apenas o conteúdo principal
        main_content = '''
        <div class="space-y-6">
            <div class="border-b border-border pb-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h1 class="text-3xl font-bold">Componentes</h1>
                        <p class="text-muted-foreground mt-1">Selecione um componente para ver a demonstração</p>
                    </div>
                    <a href="/" data-spa-link class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
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
        
        response_data = {
            'content': main_content,
            'title': 'Componentes - Biblioteca UI',
            'path': request.path,
            'success': True
        }
        
        print("✅ SPA Response enviada para lista de componentes")
        return JsonResponse(response_data)
    
    # Se não for SPA, continuar com o fluxo normal
    # Construir conteúdo da sidebar
    sidebar_content = '<nav class="space-y-1">'
    for component in COMPONENTS_LIST:
        icon_mapping = {
            'accordion': 'chevron-down', 'alert': 'bell', 'alert-dialog': 'exclamation-triangle',
            'aspect-ratio': 'aspect-ratio', 'avatar': 'avatar', 'badge': 'badge',
            'breadcrumb': 'slash', 'button': 'button', 'calendar': 'calendar', 
            'card': 'card-stack', 'carousel': 'dots-horizontal', 'chart': 'bar-chart',
            'checkbox': 'checkbox', 'collapsible': 'chevron-up', 'command': 'magnifying-glass',
            'content-manager': 'clipboard', 'context-menu': 'dots-vertical', 'dialog': 'chat-bubble', 
            'drawer': 'hamburger-menu', 'dropdown': 'caret-down', 'dropdown-menu': 'dropdown-menu', 
            'form': 'clipboard', 'hover-card': 'card-stack', 'input': 'input', 'input-otp': 'lock-closed',
            'label': 'pilcrow', 'layout': 'layout', 'menubar': 'hamburger-menu',
            'modal': 'external-link', 'navigation-menu': 'hamburger-menu', 'pagination': 'dots-horizontal',
            'popover': 'chat-bubble', 'progress': 'timer', 'radio-group': 'radiobutton',
            'resizable': 'size', 'scroll-area': 'double-arrow-up', 'select': 'caret-sort',
            'separator': 'dash', 'sheet': 'hamburger-menu', 'sidebar': 'layout',
            'skeleton': 'transparency-grid', 'slider': 'slider', 'sonner': 'bell',
            'spinner': 'reload', 'switch': 'switch', 'table': 'table',
            'tabs': 'dots-horizontal', 'text-editor': 'pencil-1', 'textarea': 'text-align-top', 
            'toggle': 'switch', 'toggle-group': 'mix', 'tooltip': 'question-mark-circled'
        }
        icon_name = icon_mapping.get(component['slug'], 'dot-filled')
        
        sidebar_content += f'''
        <a href="/components/{component['slug']}/" data-spa-link class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium hover:bg-accent transition-colors">
            <img src="/static/radix-icons/{icon_name}.svg" class="size-4" alt="{component['name']}">
            <span x-show="!sidebarCollapsed || isMobile">{component['name']}</span>
        </a>
        '''
    sidebar_content += '</nav>'
    
    # Construir conteúdo do header
    header_content = '''
    <div class="flex items-center gap-4">
        <a href="/" data-spa-link class="text-xl font-bold">Django Cazenga-UI</a>
        <nav class="hidden md:flex space-x-4">
            <a href="/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Início</a>
            <a href="/components/" data-spa-link class="text-sm font-medium text-primary">Componentes</a>
            <a href="/demo/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Demo</a>
            <a href="/icons/" data-spa-link class="text-sm font-medium hover:text-primary transition-colors">Ícones</a>
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
                <a href="/" data-spa-link class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
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
        'page_title': 'Componentes - Biblioteca UI',
        'components_list': COMPONENTS_LIST,
        'sidebar_content': sidebar_content,
        'header_content': header_content,
        'main_content': main_content,
    }
    
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
        'page_title': 'Ícones - Biblioteca UI',
        'nav_menu': nav_menu,
        'icons': icons,
        'total_icons': len(icons)
    }
    
    return spa_response(request, "icons.html", context) 