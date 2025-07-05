from django.shortcuts import render
import json

# Create your views here.

def index(request):
    return render(request, "base.html")

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
