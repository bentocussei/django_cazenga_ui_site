"""
Dados dos componentes para demonstrações
"""

# Dados para Button
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

# Dados para Card
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

# Dados para Input
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
        ['<code>step</code>', 'number', '-', 'Incremento (para type="number")'],
        ['<code>minlength</code>', 'number', '-', 'Comprimento mínimo do texto'],
        ['<code>maxlength</code>', 'number', '-', 'Comprimento máximo do texto'],
        ['<code>pattern</code>', 'string', '-', 'Padrão regex para validação'],
        ['<code>autocomplete</code>', 'string', '-', 'Controle de autocompletar'],
        ['<code>autofocus</code>', 'boolean', 'false', 'Focar automaticamente no campo'],
    ]
}

# Dados para Layout
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

# Dados para Accordion
ACCORDION_ITEMS = [
    {
        'id': 'item-1',
        'title': 'O que é um componente?',
        'content': 'Um componente é uma parte reutilizável de interface que pode ser configurada através de parâmetros. Ele encapsula funcionalidades e estilos específicos.'
    },
    {
        'id': 'item-2',
        'title': 'Como personalizar estilos?',
        'content': 'Você pode personalizar estilos utilizando as classes CSS do Tailwind CSS ou definindo suas próprias classes customizadas através do parâmetro class.'
    },
    {
        'id': 'item-3',
        'title': 'Posso usar Alpine.js?',
        'content': 'Sim! Todos os componentes são compatíveis com Alpine.js. Você pode adicionar reatividade e interatividade usando as diretivas x-data, x-show, x-model, etc.'
    },
]

# Dados para Alert
ALERT_EXAMPLES = [
    {
        'title': 'Sucesso',
        'description': 'Operação realizada com sucesso!',
        'variant': 'success',
        'icon': 'check-circled'
    },
    {
        'title': 'Informação',
        'description': 'Aqui está uma informação importante para você.',
        'variant': 'info',
        'icon': 'info-circled'
    },
    {
        'title': 'Atenção',
        'description': 'Verifique os dados antes de prosseguir.',
        'variant': 'warning',
        'icon': 'exclamation-triangle'
    },
    {
        'title': 'Erro',
        'description': 'Ocorreu um erro ao processar sua solicitação.',
        'variant': 'error',
        'icon': 'cross-circled'
    },
]

# Dados para Avatar
AVATAR_EXAMPLES = [
    {
        'src': 'https://github.com/shadcn.png',
        'alt': 'shadcn',
        'fallback': 'CN'
    },
    {
        'src': 'https://github.com/vercel.png',
        'alt': 'Vercel',
        'fallback': 'VC'
    },
    {
        'src': 'https://github.com/nextjs.png',
        'alt': 'Next.js',
        'fallback': 'NX'
    },
]

# Dados para Badge
BADGE_EXAMPLES = [
    {'text': 'Novo', 'variant': 'default'},
    {'text': 'Popular', 'variant': 'secondary'},
    {'text': 'Descontinuado', 'variant': 'destructive'},
    {'text': 'Em breve', 'variant': 'outline'},
]

# Dados para Breadcrumb
BREADCRUMB_ITEMS = [
    [
        {'label': 'Início', 'href': '/'},
        {'label': 'Componentes', 'href': '/components/'},
        {'label': 'Breadcrumb'},
    ],
    [
        {'label': 'Dashboard', 'href': '/dashboard'},
        {'label': 'Usuários', 'href': '/dashboard/users'},
        {'label': 'Perfil', 'href': '/dashboard/users/profile'},
        {'label': 'Configurações'},
    ],
    [
        {'label': 'Loja', 'href': '/'},
        {'label': 'Produtos', 'href': '/products'},
        {'label': 'Eletrônicos', 'href': '/products/electronics'},
        {'label': 'Smartphones', 'href': '/products/electronics/smartphones'},
        {'label': 'iPhone 15 Pro Max'},
    ],
]

# Dados para parâmetros do Breadcrumb
BREADCRUMB_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do breadcrumb (obrigatório)'],
        ['<code>separator</code>', 'string/HTML', 'seta', 'Separador customizado entre os itens'],
        ['<code>max_items</code>', 'number', '5', 'Número máximo de itens antes de mostrar ellipsis'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para parâmetros do Checkbox
CHECKBOX_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>checked</code>', 'boolean', 'false', 'Se o checkbox está marcado'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o checkbox está desabilitado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>value</code>', 'string', 'on', 'Valor do checkbox'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para parâmetros do Progress
PROGRESS_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>value</code>', 'number', '0', 'Valor do progresso (0-100)'],
        ['<code>max</code>', 'number', '100', 'Valor máximo'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>show_value</code>', 'boolean', 'false', 'Mostrar porcentagem'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, success, warning, danger'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>striped</code>', 'boolean', 'false', 'Adicionar listras'],
        ['<code>animated</code>', 'boolean', 'false', 'Animar listras'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Radio Group
RADIO_GROUP_OPTIONS = {
    'basic': [
        {'value': 'option1', 'label': 'Opção 1'},
        {'value': 'option2', 'label': 'Opção 2'},
        {'value': 'option3', 'label': 'Opção 3'},
    ],
    'payment': [
        {'value': 'card', 'label': 'Cartão de Crédito', 'description': 'Pagar com cartão de crédito ou débito'},
        {'value': 'pix', 'label': 'PIX', 'description': 'Pagamento instantâneo via PIX'},
        {'value': 'boleto', 'label': 'Boleto Bancário', 'description': 'Pagamento via boleto bancário'},
    ],
    'plan': [
        {'value': 'basic', 'label': 'Básico', 'description': 'Recursos essenciais para começar'},
        {'value': 'pro', 'label': 'Pro', 'description': 'Recursos avançados para profissionais'},
        {'value': 'enterprise', 'label': 'Enterprise', 'description': 'Recursos completos para empresas'},
    ],
    'size': [
        {'value': 'sm', 'label': 'Pequeno'},
        {'value': 'md', 'label': 'Médio'},
        {'value': 'lg', 'label': 'Grande'},
    ],
    'disabled': [
        {'value': 'available', 'label': 'Disponível'},
        {'value': 'limited', 'label': 'Limitado', 'disabled': True},
        {'value': 'unavailable', 'label': 'Indisponível', 'disabled': True},
    ],
}

# Dados para parâmetros do Radio Group
RADIO_GROUP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do grupo de radio buttons (obrigatório)'],
        ['<code>options</code>', 'array', '-', 'Lista de opções do grupo (obrigatório)'],
        ['<code>value</code>', 'string', '-', 'Valor selecionado inicialmente'],
        ['<code>orientation</code>', 'string', 'vertical', 'Orientação: vertical, horizontal'],
        ['<code>disabled</code>', 'boolean', 'false', 'Desabilitar todo o grupo'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>on_change</code>', 'string', '-', 'Função JavaScript no evento change'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para parâmetros do Separator
SEPARATOR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>decorative</code>', 'boolean', 'true', 'Se é apenas decorativo ou tem significado semântico'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para parâmetros do Switch
SWITCH_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>checked</code>', 'boolean', 'false', 'Se o switch está ligado'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o switch está desabilitado'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: sm, default, lg'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para parâmetros do Textarea
TEXTAREA_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>placeholder</code>', 'string', '-', 'Texto de placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor inicial'],
        ['<code>rows</code>', 'number', '4', 'Número de linhas'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>readonly</code>', 'boolean', 'false', 'Se o campo é somente leitura'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>resize</code>', 'string', 'vertical', 'Controle de redimensionamento: none, vertical, horizontal, both'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>maxlength</code>', 'number', '-', 'Limite máximo de caracteres'],
        ['<code>minlength</code>', 'number', '-', 'Limite mínimo de caracteres'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Calendar
CALENDAR_EVENTS = [
    {
        'date': '2024-01-15',
        'title': 'Reunião de equipe',
        'time': '10:00'
    },
    {
        'date': '2024-01-20',
        'title': 'Apresentação do projeto',
        'time': '14:30'
    },
    {
        'date': '2024-01-25',
        'title': 'Revisão de código',
        'time': '09:00'
    },
]

# Dados para Carousel
CAROUSEL_ITEMS = [
    {
        'image': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop',
        'title': 'Paisagem 1',
        'description': 'Uma bela vista montanhosa ao amanhecer'
    },
    {
        'image': 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=400&fit=crop',
        'title': 'Paisagem 2',
        'description': 'Floresta densa com névoa matinal'
    },
    {
        'image': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=400&fit=crop',
        'title': 'Paisagem 3',
        'description': 'Campo aberto sob céu estrelado'
    },
]

# Dados para parâmetros do Carousel
CAROUSEL_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do carousel'],
        ['<code>items.image</code>', 'string', '-', 'URL da imagem'],
        ['<code>items.title</code>', 'string', '-', 'Título do slide'],
        ['<code>items.description</code>', 'string', '-', 'Descrição do slide'],
        ['<code>autoplay</code>', 'boolean', 'true', 'Reprodução automática'],
        ['<code>interval</code>', 'number', '5000', 'Intervalo entre slides (ms)'],
        ['<code>controls</code>', 'boolean', 'true', 'Mostrar controles de navegação'],
        ['<code>indicators</code>', 'boolean', 'true', 'Mostrar indicadores de posição'],
        ['<code>loop</code>', 'boolean', 'true', 'Loop infinito'],
        ['<code>fade</code>', 'boolean', 'false', 'Transição fade ao invés de slide'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Chart
CHART_DATA = {
    'line': {
        'labels': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'datasets': [
            {
                'label': 'Vendas 2024',
                'data': [12, 19, 3, 5, 2, 3]
            },
            {
                'label': 'Vendas 2023',
                'data': [2, 3, 20, 5, 1, 4]
            }
        ]
    },
    'bar': {
        'labels': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
        'datasets': [
            {
                'label': 'Vendas',
                'data': [65, 59, 80, 81]
            }
        ]
    },
    'pie': {
        'labels': ['Desktop', 'Mobile', 'Tablet'],
        'datasets': [
            {
                'label': 'Dispositivos',
                'data': [55, 35, 10]
            }
        ]
    }
}

# Dados para parâmetros do Chart
CHART_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>type</code>', 'string', 'line', 'Tipo do gráfico: line, bar, pie, doughnut, radar, polarArea'],
        ['<code>data</code>', 'object', '-', 'Dados do gráfico (labels e datasets)'],
        ['<code>width</code>', 'number', '400', 'Largura do gráfico em pixels'],
        ['<code>height</code>', 'number', '300', 'Altura do gráfico em pixels'],
        ['<code>responsive</code>', 'boolean', 'true', 'Se o gráfico deve ser responsivo'],
        ['<code>legend</code>', 'boolean', 'true', 'Mostrar legenda'],
        ['<code>grid</code>', 'boolean', 'true', 'Mostrar grade'],
        ['<code>animation</code>', 'boolean', 'true', 'Animação na renderização'],
        ['<code>colors</code>', 'array', 'default', 'Cores customizadas para o gráfico'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Command
COMMAND_ITEMS = [
    {
        'group': 'Sugestões',
        'items': [
            {'icon': 'calendar', 'text': 'Agenda', 'shortcut': 'Ctrl+A'},
            {'icon': 'gear', 'text': 'Configurações', 'shortcut': 'Ctrl+,'},
            {'icon': 'person', 'text': 'Perfil', 'shortcut': 'Ctrl+P'},
        ]
    },
    {
        'group': 'Configurações',
        'items': [
            {'icon': 'desktop', 'text': 'Sistema', 'shortcut': None},
            {'icon': 'bell', 'text': 'Notificações', 'shortcut': None},
            {'icon': 'moon', 'text': 'Aparência', 'shortcut': None},
        ]
    },
]

# Dados para Context Menu
CONTEXT_MENU_ITEMS = [
    {'text': 'Voltar', 'icon': 'arrow-left', 'shortcut': 'Ctrl+Z'},
    {'text': 'Avançar', 'icon': 'arrow-right', 'shortcut': 'Ctrl+Y'},
    {'text': 'Atualizar', 'icon': 'reload', 'shortcut': 'F5'},
    {'separator': True},
    {'text': 'Cortar', 'icon': 'scissors', 'shortcut': 'Ctrl+X'},
    {'text': 'Copiar', 'icon': 'copy', 'shortcut': 'Ctrl+C'},
    {'text': 'Colar', 'icon': 'clipboard', 'shortcut': 'Ctrl+V'},
    {'separator': True},
    {'text': 'Inspecionar', 'icon': 'magnifying-glass', 'shortcut': 'F12'},
]

# Dados para Dialog
DIALOG_EXAMPLES = [
    {
        'title': 'Excluir conta',
        'description': 'Tem certeza que deseja excluir sua conta? Esta ação não pode ser desfeita.',
        'type': 'destructive'
    },
    {
        'title': 'Salvar alterações',
        'description': 'Suas alterações foram salvas localmente. Deseja sincronizar com o servidor?',
        'type': 'default'
    },
]

# Dados para Dropdown Menu
DROPDOWN_MENU_ITEMS = [
    {'text': 'Perfil', 'icon': 'person', 'shortcut': 'Ctrl+P'},
    {'text': 'Configurações', 'icon': 'gear', 'shortcut': 'Ctrl+,'},
    {'text': 'Ajuda', 'icon': 'question-mark', 'shortcut': 'F1'},
    {'separator': True},
    {'text': 'Sair', 'icon': 'exit', 'shortcut': 'Ctrl+Q'},
]

# Dados para Form
FORM_FIELDS = [
    {
        'name': 'name',
        'type': 'text',
        'label': 'Nome completo',
        'placeholder': 'Digite seu nome',
        'required': True
    },
    {
        'name': 'email',
        'type': 'email',
        'label': 'E-mail',
        'placeholder': 'seu@email.com',
        'required': True
    },
    {
        'name': 'phone',
        'type': 'tel',
        'label': 'Telefone',
        'placeholder': '(11) 99999-9999',
        'required': False
    },
    {
        'name': 'message',
        'type': 'textarea',
        'label': 'Mensagem',
        'placeholder': 'Digite sua mensagem',
        'required': True
    },
]

# Dados para Input OTP
INPUT_OTP_DATA = {
    'default_length': 6,
    'types': ['numeric', 'alphanumeric', 'alphabetic'],
    'examples': [
        {'type': 'numeric', 'length': 4, 'description': 'PIN de 4 dígitos'},
        {'type': 'numeric', 'length': 6, 'description': 'Código de verificação'},
        {'type': 'alphanumeric', 'length': 8, 'description': 'Código de backup'},
    ]
}

# Dados para parâmetros do Input OTP
INPUT_OTP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo'],
        ['<code>length</code>', 'number', '6', 'Número de caracteres do código'],
        ['<code>type</code>', 'string', 'numeric', 'Tipo: numeric, alphanumeric, alphabetic'],
        ['<code>placeholder</code>', 'string', '·', 'Caractere placeholder'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>required</code>', 'boolean', 'true', 'Se o campo é obrigatório'],
        ['<code>autocomplete</code>', 'string', 'one-time-code', 'Tipo de autocompletar'],
        ['<code>separator</code>', 'boolean', 'false', 'Mostrar separadores entre grupos'],
        ['<code>mask</code>', 'boolean', 'false', 'Mascarar caracteres inseridos'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Drawer
DRAWER_DATA = {
    'menu_items': [
        {'icon': 'home', 'text': 'Dashboard', 'href': '/dashboard'},
        {'icon': 'person', 'text': 'Usuários', 'href': '/users'},
        {'icon': 'box', 'text': 'Produtos', 'href': '/products'},
        {'icon': 'bar-chart', 'text': 'Relatórios', 'href': '/reports'},
        {'icon': 'gear', 'text': 'Configurações', 'href': '/settings'},
    ],
    'user_profile': {
        'name': 'Ana Silva',
        'email': 'ana@empresa.com',
        'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100&h=100&fit=crop&crop=face'
    },
    'notifications': [
        {'title': 'Nova mensagem', 'description': 'Você tem 3 mensagens não lidas', 'time': '2 min atrás'},
        {'title': 'Relatório pronto', 'description': 'O relatório mensal foi gerado', 'time': '1 hora atrás'},
        {'title': 'Backup concluído', 'description': 'Backup automático finalizado', 'time': '2 horas atrás'},
    ]
}

# Dados para parâmetros do Drawer
DRAWER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>position</code>', 'string', 'left', 'Posição: left, right, top, bottom'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, full'],
        ['<code>overlay</code>', 'boolean', 'true', 'Mostrar overlay de fundo'],
        ['<code>dismissible</code>', 'boolean', 'true', 'Pode ser fechado clicando fora'],
        ['<code>backdrop_blur</code>', 'boolean', 'false', 'Aplicar blur no fundo'],
        ['<code>animation</code>', 'string', 'slide', 'Animação: slide, fade, scale'],
        ['<code>persistent</code>', 'boolean', 'false', 'Não pode ser fechado pelo usuário'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Sheet
SHEET_DATA = {
    'user_profile': {
        'name': 'Maria Santos',
        'email': 'maria@empresa.com',
        'role': 'Gerente',
        'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100&h=100&fit=crop&crop=face'
    },
    'form_fields': [
        {'name': 'title', 'type': 'text', 'label': 'Título', 'placeholder': 'Digite o título'},
        {'name': 'description', 'type': 'textarea', 'label': 'Descrição', 'placeholder': 'Descreva os detalhes'},
        {'name': 'priority', 'type': 'select', 'label': 'Prioridade', 'options': [
            {'value': 'low', 'label': 'Baixa'},
            {'value': 'medium', 'label': 'Média'},
            {'value': 'high', 'label': 'Alta'}
        ]},
        {'name': 'due_date', 'type': 'date', 'label': 'Data de Vencimento'},
    ],
    'settings': [
        {'key': 'notifications', 'label': 'Notificações', 'description': 'Receber notificações por email', 'type': 'toggle'},
        {'key': 'theme', 'label': 'Tema', 'description': 'Modo escuro/claro', 'type': 'select', 'options': [
            {'value': 'light', 'label': 'Claro'},
            {'value': 'dark', 'label': 'Escuro'},
            {'value': 'auto', 'label': 'Automático'}
        ]},
        {'key': 'language', 'label': 'Idioma', 'description': 'Idioma da interface', 'type': 'select', 'options': [
            {'value': 'pt', 'label': 'Português'},
            {'value': 'en', 'label': 'English'},
            {'value': 'es', 'label': 'Español'}
        ]},
    ],
    'recent_files': [
        {'name': 'Relatório Q3.pdf', 'size': '2.4 MB', 'date': '2 horas atrás'},
        {'name': 'Apresentação.pptx', 'size': '1.8 MB', 'date': '1 dia atrás'},
        {'name': 'Planilha Orçamento.xlsx', 'size': '890 KB', 'date': '3 dias atrás'},
    ]
}

# Dados para parâmetros do Sheet
SHEET_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>position</code>', 'string', 'right', 'Posição: left, right, top, bottom'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, full'],
        ['<code>overlay</code>', 'boolean', 'true', 'Mostrar overlay de fundo'],
        ['<code>dismissible</code>', 'boolean', 'true', 'Pode ser fechado clicando fora'],
        ['<code>closable</code>', 'boolean', 'true', 'Mostrar botão de fechar'],
        ['<code>scrollable</code>', 'boolean', 'true', 'Permitir rolagem do conteúdo'],
        ['<code>backdrop_blur</code>', 'boolean', 'false', 'Aplicar blur no fundo'],
        ['<code>animation</code>', 'string', 'slide', 'Animação: slide, fade, scale'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Sidebar
SIDEBAR_DATA = {
    'menu_items': [
        {'icon': 'home', 'text': 'Dashboard', 'href': '/dashboard', 'active': True},
        {'icon': 'person', 'text': 'Usuários', 'href': '/users', 'badge': '12'},
        {'icon': 'box', 'text': 'Produtos', 'href': '/products', 'children': [
            {'icon': 'plus', 'text': 'Adicionar', 'href': '/products/add'},
            {'icon': 'table', 'text': 'Listar', 'href': '/products/list'},
            {'icon': 'bar-chart', 'text': 'Relatórios', 'href': '/products/reports'},
        ]},
        {'icon': 'clipboard', 'text': 'Pedidos', 'href': '/orders', 'badge': '3'},
        {'icon': 'bar-chart', 'text': 'Relatórios', 'href': '/reports'},
        {'icon': 'gear', 'text': 'Configurações', 'href': '/settings'},
    ],
    'user_info': {
        'name': 'João Silva',
        'email': 'joao@empresa.com',
        'role': 'Administrador',
        'avatar': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face'
    },
    'company_info': {
        'name': 'Empresa ABC',
        'logo': 'https://via.placeholder.com/40x40/3B82F6/FFFFFF?text=ABC'
    },
    'quick_actions': [
        {'icon': 'plus', 'text': 'Novo Projeto', 'href': '/projects/new'},
        {'icon': 'upload', 'text': 'Upload', 'href': '/upload'},
        {'icon': 'calendar', 'text': 'Agendar', 'href': '/schedule'},
    ]
}

# Dados para parâmetros do Sidebar
SIDEBAR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>position</code>', 'string', 'left', 'Posição: left, right'],
        ['<code>collapsible</code>', 'boolean', 'true', 'Pode ser recolhida'],
        ['<code>collapsed</code>', 'boolean', 'false', 'Estado inicial recolhido'],
        ['<code>width</code>', 'string', 'w-64', 'Largura da sidebar (classes Tailwind)'],
        ['<code>collapsed_width</code>', 'string', 'w-16', 'Largura quando recolhida'],
        ['<code>overlay_on_mobile</code>', 'boolean', 'true', 'Mostrar overlay no mobile'],
        ['<code>auto_collapse</code>', 'boolean', 'true', 'Recolher automaticamente no mobile'],
        ['<code>persistent</code>', 'boolean', 'false', 'Sempre visível (não pode ser fechada)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Context Menu
CONTEXT_MENU_DATA = {
    'basic_items': [
        {'icon': 'copy', 'text': 'Copiar', 'shortcut': 'Ctrl+C', 'action': 'copy'},
        {'icon': 'clipboard', 'text': 'Colar', 'shortcut': 'Ctrl+V', 'action': 'paste'},
        {'type': 'separator'},
        {'icon': 'pencil-1', 'text': 'Editar', 'action': 'edit'},
        {'icon': 'trash', 'text': 'Excluir', 'action': 'delete', 'variant': 'danger'},
    ],
    'file_items': [
        {'icon': 'file-plus', 'text': 'Novo Arquivo', 'action': 'new_file'},
        {'icon': 'card-stuck-plus', 'text': 'Nova Pasta', 'action': 'new_folder'},
        {'type': 'separator'},
        {'icon': 'copy', 'text': 'Copiar', 'shortcut': 'Ctrl+C', 'action': 'copy'},
        {'icon': 'scissors', 'text': 'Recortar', 'shortcut': 'Ctrl+X', 'action': 'cut'},
        {'icon': 'clipboard', 'text': 'Colar', 'shortcut': 'Ctrl+V', 'action': 'paste'},
        {'type': 'separator'},
        {'icon': 'pencil-1', 'text': 'Renomear', 'action': 'rename'},
        {'icon': 'trash', 'text': 'Excluir', 'action': 'delete', 'variant': 'danger'},
        {'type': 'separator'},
        {'icon': 'gear', 'text': 'Propriedades', 'action': 'properties'},
    ],
    'text_items': [
        {'icon': 'font-bold', 'text': 'Negrito', 'shortcut': 'Ctrl+B', 'action': 'bold'},
        {'icon': 'font-italic', 'text': 'Itálico', 'shortcut': 'Ctrl+I', 'action': 'italic'},
        {'icon': 'underline', 'text': 'Sublinhado', 'shortcut': 'Ctrl+U', 'action': 'underline'},
        {'type': 'separator'},
        {'icon': 'text-align-left', 'text': 'Alinhar à Esquerda', 'action': 'align_left'},
        {'icon': 'text-align-center', 'text': 'Centralizar', 'action': 'align_center'},
        {'icon': 'text-align-right', 'text': 'Alinhar à Direita', 'action': 'align_right'},
        {'type': 'separator'},
        {'icon': 'link-1', 'text': 'Inserir Link', 'action': 'insert_link'},
        {'icon': 'image', 'text': 'Inserir Imagem', 'action': 'insert_image'},
    ],
    'table_items': [
        {'icon': 'row-spacing', 'text': 'Inserir Linha Acima', 'action': 'insert_row_above'},
        {'icon': 'row-spacing', 'text': 'Inserir Linha Abaixo', 'action': 'insert_row_below'},
        {'type': 'separator'},
        {'icon': 'column-spacing', 'text': 'Inserir Coluna à Esquerda', 'action': 'insert_column_left'},
        {'icon': 'column-spacing', 'text': 'Inserir Coluna à Direita', 'action': 'insert_column_right'},
        {'type': 'separator'},
        {'icon': 'trash', 'text': 'Excluir Linha', 'action': 'delete_row', 'variant': 'danger'},
        {'icon': 'trash', 'text': 'Excluir Coluna', 'action': 'delete_column', 'variant': 'danger'},
        {'type': 'separator'},
        {'icon': 'table', 'text': 'Propriedades da Tabela', 'action': 'table_properties'},
    ]
}

# Dados para parâmetros do Context Menu
CONTEXT_MENU_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do menu'],
        ['<code>items.icon</code>', 'string', '-', 'Ícone do item'],
        ['<code>items.text</code>', 'string', '-', 'Texto do item'],
        ['<code>items.shortcut</code>', 'string', '-', 'Atalho do teclado'],
        ['<code>items.action</code>', 'string', '-', 'Ação a ser executada'],
        ['<code>items.variant</code>', 'string', 'default', 'Variante: default, danger'],
        ['<code>items.type</code>', 'string', 'item', 'Tipo: item, separator'],
        ['<code>trigger</code>', 'string', 'right-click', 'Evento que abre o menu'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Navigation Menu
NAVIGATION_MENU_ITEMS = [
    {
        'text': 'Início',
        'href': '/',
        'description': 'Página inicial do site'
    },
    {
        'text': 'Produtos',
        'href': '/products/',
        'description': 'Veja nossos produtos',
        'children': [
            {'text': 'Notebooks', 'href': '/products/notebooks/'},
            {'text': 'Desktops', 'href': '/products/desktops/'},
            {'text': 'Acessórios', 'href': '/products/accessories/'},
        ]
    },
    {
        'text': 'Sobre',
        'href': '/about/',
        'description': 'Conheça nossa história'
    },
    {
        'text': 'Contato',
        'href': '/contact/',
        'description': 'Entre em contato'
    },
]

# Dados para parâmetros do Navigation Menu
NAVIGATION_MENU_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do menu'],
        ['<code>items.text</code>', 'string', '-', 'Texto do item'],
        ['<code>items.href</code>', 'string', '-', 'Link do item'],
        ['<code>items.description</code>', 'string', '-', 'Descrição do item'],
        ['<code>items.children</code>', 'array', '-', 'Sub-itens do menu'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>trigger</code>', 'string', 'hover', 'Trigger do submenu: hover, click'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Pagination
PAGINATION_DATA = {
    'current_page': 3,
    'total_pages': 10,
    'per_page': 10,
    'total_items': 97,
    'has_previous': True,
    'has_next': True,
    'previous_page': 2,
    'next_page': 4,
}

# Dados para Radio Group
RADIO_GROUP_OPTIONS = [
    {'value': 'comfortable', 'label': 'Confortável', 'description': 'Espaçamento adequado para leitura'},
    {'value': 'compact', 'label': 'Compacto', 'description': 'Menos espaçamento, mais informações'},
    {'value': 'comfortable-dense', 'label': 'Denso', 'description': 'Máximo de informações por tela'},
]

# Dados para Select
SELECT_OPTIONS = [
    {'value': 'apple', 'label': 'Maçã'},
    {'value': 'banana', 'label': 'Banana'},
    {'value': 'orange', 'label': 'Laranja'},
    {'value': 'grape', 'label': 'Uva'},
    {'value': 'watermelon', 'label': 'Melancia'},
]

# Dados para Table
TABLE_DATA = {
    'headers': ['Nome', 'E-mail', 'Cargo', 'Status'],
    'rows': [
        ['Ana Silva', 'ana@email.com', 'Desenvolvedora', 'Ativo'],
        ['Carlos Santos', 'carlos@email.com', 'Designer', 'Ativo'],
        ['Maria Oliveira', 'maria@email.com', 'Gerente', 'Inativo'],
        ['João Pereira', 'joao@email.com', 'Analista', 'Ativo'],
        ['Lucia Costa', 'lucia@email.com', 'Desenvolvedora', 'Ativo'],
    ]
}

# Dados para Tabs
TABS_DATA = [
    {
        'id': 'account',
        'label': 'Conta',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Configurações da Conta</h3><p>Gerencie suas informações pessoais e preferências de conta.</p></div>'
    },
    {
        'id': 'password',
        'label': 'Senha',
        'icon': 'lock-closed',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Alterar Senha</h3><p>Atualize sua senha regularmente para manter sua conta segura.</p></div>'
    },
    {
        'id': 'notifications',
        'label': 'Notificações',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Preferências de Notificação</h3><p>Escolha quais notificações você deseja receber.</p></div>'
    }
]

# Dados para Toggle Group
TOGGLE_GROUP_DATA = {
    'alignment': {
        'items': ['left', 'center', 'right'],
        'labels': ['Esquerda', 'Centro', 'Direita'],
        'icons': ['text-align-left', 'text-align-center', 'text-align-right']
    },
    'formatting': {
        'items': ['bold', 'italic', 'underline'],
        'labels': ['Negrito', 'Itálico', 'Sublinhado'],
        'icons': ['font-bold', 'font-italic', 'underline']
    },
    'size': {
        'items': ['sm', 'md', 'lg'],
        'labels': ['Pequeno', 'Médio', 'Grande'],
        'icons': None
    }
}

# Dados para Resizable
RESIZABLE_DATA = {
    'horizontal': {
        'panels': ['sidebar', 'main'],
        'contents': [
            '<div class="space-y-3"><h4 class="font-medium">Sidebar</h4><nav class="space-y-1"><a href="#" class="block px-2 py-1 text-sm hover:bg-accent rounded">Dashboard</a><a href="#" class="block px-2 py-1 text-sm hover:bg-accent rounded">Usuários</a><a href="#" class="block px-2 py-1 text-sm hover:bg-accent rounded">Relatórios</a></nav></div>',
            '<div class="space-y-3"><h4 class="font-medium">Conteúdo Principal</h4><p class="text-sm text-muted-foreground">Aqui fica o conteúdo principal da aplicação. Você pode redimensionar os painéis arrastando a barra central.</p><div class="grid grid-cols-2 gap-4 mt-4"><div class="p-3 bg-muted rounded"><p class="text-sm font-medium">Card 1</p></div><div class="p-3 bg-muted rounded"><p class="text-sm font-medium">Card 2</p></div></div></div>'
        ],
        'sizes': [25, 75]
    },
    'vertical': {
        'panels': ['header', 'content'],
        'contents': [
            '<div class="space-y-2"><h4 class="font-medium">Header</h4><p class="text-sm text-muted-foreground">Área do cabeçalho com informações importantes.</p></div>',
            '<div class="space-y-2"><h4 class="font-medium">Conteúdo</h4><p class="text-sm text-muted-foreground">Área principal do conteúdo. Redimensione arrastando a barra horizontal.</p><div class="mt-4 space-y-2"><div class="p-2 bg-muted rounded text-sm">Item 1</div><div class="p-2 bg-muted rounded text-sm">Item 2</div><div class="p-2 bg-muted rounded text-sm">Item 3</div></div></div>'
        ],
        'sizes': [30, 70]
    }
}

# Adicionar dados dos parâmetros para novos componentes
ACCORDION_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'list', '-', 'Lista de itens do accordion'],
        ['<code>items.id</code>', 'string', '-', 'ID único do item'],
        ['<code>items.title</code>', 'string', '-', 'Título do item'],
        ['<code>items.content</code>', 'string/HTML', '-', 'Conteúdo do item'],
        ['<code>allow_multiple</code>', 'boolean', 'false', 'Permite múltiplos itens abertos'],
        ['<code>collapsible</code>', 'boolean', 'true', 'Permite fechar todos os itens'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

ALERT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do alert'],
        ['<code>description</code>', 'string', '-', 'Descrição do alert'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, success, warning, error, info'],
        ['<code>icon</code>', 'string', '-', 'Nome do ícone'],
        ['<code>dismissible</code>', 'boolean', 'false', 'Se o alert pode ser fechado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

AVATAR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>src</code>', 'string', '-', 'URL da imagem'],
        ['<code>alt</code>', 'string', '-', 'Texto alternativo'],
        ['<code>fallback</code>', 'string', '-', 'Texto a ser exibido se a imagem não carregar'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do avatar: sm, md, lg, xl'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

BADGE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do badge'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, secondary, destructive, outline'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do badge: sm, md, lg'],
        ['<code>icon</code>', 'string', '-', 'Nome do ícone'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TABS_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>tabs</code>', 'list', '-', 'Lista de abas'],
        ['<code>tabs.id</code>', 'string', '-', 'ID único da aba'],
        ['<code>tabs.label</code>', 'string', '-', 'Rótulo da aba'],
        ['<code>tabs.content</code>', 'string/HTML', '-', 'Conteúdo da aba'],
        ['<code>tabs.icon</code>', 'string', '-', 'Nome do ícone da aba'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>default_tab</code>', 'string', '-', 'ID da aba padrão ativa'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

COLLAPSIBLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do collapsible'],
        ['<code>content</code>', 'string/HTML', '-', 'Conteúdo do collapsible'],
        ['<code>trigger_text</code>', 'string', '-', 'Texto do trigger personalizado'],
        ['<code>open</code>', 'boolean', 'false', 'Estado inicial (aberto/fechado)'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o collapsible está desabilitado'],
        ['<code>trigger_class</code>', 'string', '-', 'Classes CSS adicionais para o trigger'],
        ['<code>content_class</code>', 'string', '-', 'Classes CSS adicionais para o conteúdo'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

SELECT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo'],
        ['<code>options</code>', 'list', '-', 'Lista de opções'],
        ['<code>options.value</code>', 'string', '-', 'Valor da opção'],
        ['<code>options.label</code>', 'string', '-', 'Rótulo da opção'],
        ['<code>placeholder</code>', 'string', '-', 'Texto do placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor selecionado'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TABLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>headers</code>', 'list', '-', 'Lista de cabeçalhos'],
        ['<code>rows</code>', 'list', '-', 'Lista de linhas de dados'],
        ['<code>hover</code>', 'boolean', 'false', 'Habilita hover nas linhas'],
        ['<code>responsive</code>', 'boolean', 'false', 'Tabela responsiva'],
        ['<code>striped</code>', 'boolean', 'false', 'Linhas alternadas'],
        ['<code>bordered</code>', 'boolean', 'false', 'Bordas nas células'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados extras para demonstrações
TABS_DATA_WITH_ICONS = [
    {
        'id': 'home',
        'label': 'Início',
        'icon': 'home',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Início</h3><p>Bem-vindo à página inicial.</p></div>'
    },
    {
        'id': 'profile',
        'label': 'Perfil',
        'icon': 'person',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Perfil</h3><p>Informações do seu perfil.</p></div>'
    },
    {
        'id': 'settings',
        'label': 'Configurações',
        'icon': 'gear',
        'content': '<div class="space-y-4"><h3 class="text-lg font-medium">Configurações</h3><p>Ajuste suas preferências.</p></div>'
    }
]

TABLE_DATA_WITH_ACTIONS = {
    'headers': ['Nome', 'E-mail', 'Cargo', 'Status', 'Ações'],
    'rows': [
        ['Ana Silva', 'ana@email.com', 'Desenvolvedora', 'Ativo', '<button class="text-sm text-primary hover:underline">Editar</button>'],
        ['Carlos Santos', 'carlos@email.com', 'Designer', 'Ativo', '<button class="text-sm text-primary hover:underline">Editar</button>'],
        ['Maria Oliveira', 'maria@email.com', 'Gerente', 'Inativo', '<button class="text-sm text-primary hover:underline">Editar</button>'],
        ['João Pereira', 'joao@email.com', 'Analista', 'Ativo', '<button class="text-sm text-primary hover:underline">Editar</button>'],
        ['Lucia Costa', 'lucia@email.com', 'Desenvolvedora', 'Ativo', '<button class="text-sm text-primary hover:underline">Editar</button>'],
    ]
}

# Dados para Alert Dialog
ALERT_DIALOG_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do dialog'],
        ['<code>description</code>', 'string', '-', 'Descrição/conteúdo do dialog'],
        ['<code>confirm_text</code>', 'string', 'Confirmar', 'Texto do botão de confirmação'],
        ['<code>cancel_text</code>', 'string', 'Cancelar', 'Texto do botão de cancelamento'],
        ['<code>confirm_variant</code>', 'string', 'destructive', 'Variante do botão de confirmação'],
        ['<code>trigger_text</code>', 'string', 'Abrir Dialog', 'Texto do botão que abre o dialog'],
        ['<code>trigger_variant</code>', 'string', 'outline', 'Variante do botão trigger'],
        ['<code>icon</code>', 'string', '-', 'Ícone para o dialog'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Calendar
CALENDAR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>selected_date</code>', 'string', 'hoje', 'Data selecionada inicial (formato: DD/MM/YYYY)'],
        ['<code>min_date</code>', 'string', '-', 'Data mínima selecionável'],
        ['<code>max_date</code>', 'string', '-', 'Data máxima selecionável'],
        ['<code>disabled_dates</code>', 'array', '[]', 'Lista de datas desabilitadas'],
        ['<code>highlight_dates</code>', 'array', '[]', 'Lista de datas para destacar'],
        ['<code>show_week_numbers</code>', 'boolean', 'false', 'Mostrar números das semanas'],
        ['<code>first_day_of_week</code>', 'number', '0', 'Primeiro dia da semana (0=domingo, 1=segunda)'],
        ['<code>multiple</code>', 'boolean', 'false', 'Permitir seleção múltipla'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Dialog
DIALOG_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do dialog'],
        ['<code>description</code>', 'string', '-', 'Descrição do dialog'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo personalizado do dialog'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer (botões)'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do dialog: sm, md, lg, xl'],
        ['<code>close_button</code>', 'boolean', 'true', 'Mostrar botão de fechar'],
        ['<code>trigger_text</code>', 'string', 'Abrir Dialog', 'Texto do botão que abre o dialog'],
        ['<code>trigger_variant</code>', 'string', 'default', 'Variante do botão trigger'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Form
FORM_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>method</code>', 'string', 'POST', 'Método HTTP do formulário'],
        ['<code>action</code>', 'string', '#', 'URL de destino do formulário'],
        ['<code>enctype</code>', 'string', '-', 'Tipo de codificação (ex: multipart/form-data)'],
        ['<code>novalidate</code>', 'boolean', 'false', 'Desabilitar validação HTML nativa'],
        ['<code>autocomplete</code>', 'string', 'on', 'Controle de autocompletar'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Label
LABEL_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>for</code>', 'string', '-', 'ID do elemento associado'],
        ['<code>text</code>', 'string', '-', 'Texto do rótulo'],
        ['<code>required</code>', 'boolean', 'false', 'Adicionar indicador de obrigatório'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Pagination
PAGINATION_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>current_page</code>', 'number', '1', 'Página atual'],
        ['<code>total_pages</code>', 'number', '1', 'Total de páginas'],
        ['<code>show_edges</code>', 'boolean', 'true', 'Mostrar primeira e última página'],
        ['<code>show_prev_next</code>', 'boolean', 'true', 'Mostrar botões anterior/próximo'],
        ['<code>max_visible</code>', 'number', '5', 'Máximo de páginas visíveis'],
        ['<code>base_url</code>', 'string', '?page=', 'URL base para links'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Popover
POPOVER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do popover'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo do popover'],
        ['<code>trigger_text</code>', 'string', 'Abrir Popover', 'Texto do elemento trigger'],
        ['<code>placement</code>', 'string', 'top', 'Posição: top, bottom, left, right'],
        ['<code>trigger_type</code>', 'string', 'click', 'Tipo de trigger: click, hover'],
        ['<code>arrow</code>', 'boolean', 'true', 'Mostrar seta apontando para o trigger'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Skeleton
SKELETON_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>type</code>', 'string', 'text', 'Tipo: text, avatar, card, line, block'],
        ['<code>lines</code>', 'number', '3', 'Número de linhas (para type="text")'],
        ['<code>width</code>', 'string', 'full', 'Largura: full, 1/2, 1/3, 1/4, custom'],
        ['<code>height</code>', 'string', 'auto', 'Altura: auto ou valor específico'],
        ['<code>animate</code>', 'boolean', 'true', 'Animação de loading'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Slider
SLIDER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo'],
        ['<code>value</code>', 'number', '50', 'Valor inicial'],
        ['<code>min</code>', 'number', '0', 'Valor mínimo'],
        ['<code>max</code>', 'number', '100', 'Valor máximo'],
        ['<code>step</code>', 'number', '1', 'Incremento'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o slider está desabilitado'],
        ['<code>show_value</code>', 'boolean', 'true', 'Mostrar valor atual'],
        ['<code>show_labels</code>', 'boolean', 'false', 'Mostrar rótulos min/max'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Spinner
SPINNER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl'],
        ['<code>color</code>', 'string', 'primary', 'Cor: primary, secondary, success, warning, danger'],
        ['<code>text</code>', 'string', '-', 'Texto de carregamento'],
        ['<code>centered</code>', 'boolean', 'false', 'Centralizar o spinner'],
        ['<code>overlay</code>', 'boolean', 'false', 'Mostrar como overlay'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Toggle
TOGGLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo'],
        ['<code>checked</code>', 'boolean', 'false', 'Estado inicial'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o toggle está desabilitado'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>label</code>', 'string', '-', 'Rótulo do toggle'],
        ['<code>description</code>', 'string', '-', 'Descrição do toggle'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Tooltip
TOOLTIP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do tooltip'],
        ['<code>position</code>', 'string', 'top', 'Posição: top, bottom, left, right'],
        ['<code>trigger</code>', 'string', 'hover', 'Trigger: hover, click, focus'],
        ['<code>delay</code>', 'number', '0', 'Delay em milissegundos'],
        ['<code>arrow</code>', 'boolean', 'true', 'Mostrar seta apontadora'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Dropdown Menu
DROPDOWN_MENU_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', 'Menu', 'Texto do botão trigger'],
        ['<code>items</code>', 'array', '[]', 'Lista de itens do menu'],
        ['<code>items.text</code>', 'string', '-', 'Texto do item'],
        ['<code>items.icon</code>', 'string', '-', 'Ícone do item'],
        ['<code>items.href</code>', 'string', '-', 'Link do item'],
        ['<code>items.action</code>', 'string', '-', 'Ação JavaScript do item'],
        ['<code>items.separator</code>', 'boolean', 'false', 'Se é um separador'],
        ['<code>items.disabled</code>', 'boolean', 'false', 'Se está desabilitado'],
        ['<code>position</code>', 'string', 'bottom-start', 'Posição do menu'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Modal
MODAL_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do modal'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo do modal'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, full'],
        ['<code>closable</code>', 'boolean', 'true', 'Se pode ser fechado'],
        ['<code>backdrop_close</code>', 'boolean', 'true', 'Fechar ao clicar no backdrop'],
        ['<code>trigger_text</code>', 'string', 'Abrir Modal', 'Texto do botão trigger'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Toggle Group
TOGGLE_GROUP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '[]', 'Lista de itens do grupo'],
        ['<code>items.value</code>', 'string', '-', 'Valor do item'],
        ['<code>items.label</code>', 'string', '-', 'Rótulo do item'],
        ['<code>items.icon</code>', 'string', '-', 'Ícone do item'],
        ['<code>multiple</code>', 'boolean', 'false', 'Permite seleção múltipla'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, outline'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Command
COMMAND_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>placeholder</code>', 'string', 'Digite um comando...', 'Placeholder do input'],
        ['<code>items</code>', 'array', '[]', 'Lista de comandos disponíveis'],
        ['<code>items.value</code>', 'string', '-', 'Valor do comando'],
        ['<code>items.label</code>', 'string', '-', 'Rótulo do comando'],
        ['<code>items.description</code>', 'string', '-', 'Descrição do comando'],
        ['<code>items.icon</code>', 'string', '-', 'Ícone do comando'],
        ['<code>items.category</code>', 'string', '-', 'Categoria do comando'],
        ['<code>empty_text</code>', 'string', 'Nenhum resultado encontrado', 'Texto quando vazio'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Hover Card
HOVER_CARD_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_content</code>', 'HTML', '-', 'Conteúdo do elemento trigger'],
        ['<code>card_content</code>', 'HTML', '-', 'Conteúdo do hover card'],
        ['<code>position</code>', 'string', 'top', 'Posição: top, bottom, left, right'],
        ['<code>delay</code>', 'number', '0', 'Delay em milissegundos'],
        ['<code>width</code>', 'string', 'w-80', 'Largura do card (classes Tailwind)'],
        ['<code>interactive</code>', 'boolean', 'false', 'Se o card permite interação'],
        ['<code>arrow</code>', 'boolean', 'true', 'Mostrar seta apontadora'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Aspect Ratio
ASPECT_RATIO_DATA = {
    'common_ratios': [
        {'ratio': '16:9', 'description': 'Padrão widescreen', 'percentage': '56.25%', 'usage': 'Vídeos HD, monitores'},
        {'ratio': '4:3', 'description': 'Padrão tradicional', 'percentage': '75%', 'usage': 'Monitores antigos, fotos'},
        {'ratio': '1:1', 'description': 'Quadrado', 'percentage': '100%', 'usage': 'Instagram, avatares'},
        {'ratio': '3:2', 'description': 'Fotografia clássica', 'percentage': '66.67%', 'usage': 'Câmeras, impressão'},
        {'ratio': '21:9', 'description': 'Ultra-widescreen', 'percentage': '42.86%', 'usage': 'Cinema, ultrawide'},
        {'ratio': '9:16', 'description': 'Vertical (Stories)', 'percentage': '177.78%', 'usage': 'Instagram Stories, TikTok'},
    ],
    'sample_images': [
        'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&h=600&fit=crop',
    ],
    'sample_videos': [
        {'title': 'Vídeo Paisagem', 'thumbnail': 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=400&h=300&fit=crop'},
        {'title': 'Vídeo Natureza', 'thumbnail': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=400&h=300&fit=crop'},
    ]
}

# Dados para parâmetros do Aspect Ratio
ASPECT_RATIO_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>ratio</code>', 'string', '16:9', 'Proporção desejada (largura:altura)'],
        ['<code>width</code>', 'number', '16', 'Valor da largura na proporção'],
        ['<code>height</code>', 'number', '9', 'Valor da altura na proporção'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo interno (imagem, vídeo, etc.)'],
        ['<code>background</code>', 'string', 'transparent', 'Cor de fundo do container'],
        ['<code>object_fit</code>', 'string', 'cover', 'Ajuste do conteúdo: cover, contain, fill'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Dropdown
DROPDOWN_DATA = {
    'countries': [
        {'value': 'br', 'label': 'Brasil', 'flag': '🇧🇷'},
        {'value': 'us', 'label': 'Estados Unidos', 'flag': '🇺🇸'},
        {'value': 'ca', 'label': 'Canadá', 'flag': '🇨🇦'},
        {'value': 'gb', 'label': 'Reino Unido', 'flag': '🇬🇧'},
        {'value': 'fr', 'label': 'França', 'flag': '🇫🇷'},
        {'value': 'de', 'label': 'Alemanha', 'flag': '🇩🇪'},
        {'value': 'jp', 'label': 'Japão', 'flag': '🇯🇵'},
        {'value': 'au', 'label': 'Austrália', 'flag': '🇦🇺'},
    ],
    'languages': [
        {'value': 'pt', 'label': 'Português'},
        {'value': 'en', 'label': 'English'},
        {'value': 'es', 'label': 'Español'},
        {'value': 'fr', 'label': 'Français'},
        {'value': 'de', 'label': 'Deutsch'},
        {'value': 'it', 'label': 'Italiano'},
        {'value': 'ja', 'label': '日本語'},
        {'value': 'ko', 'label': '한국어'},
    ],
    'categories': [
        {'value': 'technology', 'label': 'Tecnologia', 'icon': 'laptop'},
        {'value': 'business', 'label': 'Negócios', 'icon': 'bar-chart'},
        {'value': 'design', 'label': 'Design', 'icon': 'color-wheel'},
        {'value': 'marketing', 'label': 'Marketing', 'icon': 'speaker-loud'},
        {'value': 'education', 'label': 'Educação', 'icon': 'reader'},
        {'value': 'health', 'label': 'Saúde', 'icon': 'heart'},
    ],
    'users': [
        {'value': 'john', 'label': 'João Silva', 'email': 'joao@email.com', 'avatar': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face'},
        {'value': 'maria', 'label': 'Maria Santos', 'email': 'maria@email.com', 'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100&h=100&fit=crop&crop=face'},
        {'value': 'carlos', 'label': 'Carlos Costa', 'email': 'carlos@email.com', 'avatar': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face'},
        {'value': 'ana', 'label': 'Ana Oliveira', 'email': 'ana@email.com', 'avatar': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop&crop=face'},
    ],
    'status_options': [
        {'value': 'active', 'label': 'Ativo', 'color': 'green'},
        {'value': 'inactive', 'label': 'Inativo', 'color': 'gray'},
        {'value': 'pending', 'label': 'Pendente', 'color': 'yellow'},
        {'value': 'suspended', 'label': 'Suspenso', 'color': 'red'},
    ]
}

# Dados para parâmetros do Dropdown
DROPDOWN_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>options</code>', 'array', '-', 'Lista de opções disponíveis'],
        ['<code>options.value</code>', 'string', '-', 'Valor da opção'],
        ['<code>options.label</code>', 'string', '-', 'Texto exibido da opção'],
        ['<code>placeholder</code>', 'string', 'Selecione...', 'Texto quando nenhuma opção está selecionada'],
        ['<code>searchable</code>', 'boolean', 'false', 'Permitir busca nas opções'],
        ['<code>multiple</code>', 'boolean', 'false', 'Permitir múltiplas seleções'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o dropdown está desabilitado'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Menubar
MENUBAR_DATA = {
    'menu_items': [
        {
            'label': 'Arquivo',
            'items': [
                {'label': 'Novo', 'shortcut': 'Ctrl+N', 'action': 'new'},
                {'label': 'Abrir', 'shortcut': 'Ctrl+O', 'action': 'open'},
                {'label': 'Salvar', 'shortcut': 'Ctrl+S', 'action': 'save'},
                {'label': 'Salvar Como...', 'shortcut': 'Ctrl+Shift+S', 'action': 'save_as'},
                {'type': 'separator'},
                {'label': 'Importar', 'action': 'import'},
                {'label': 'Exportar', 'action': 'export'},
                {'type': 'separator'},
                {'label': 'Sair', 'shortcut': 'Ctrl+Q', 'action': 'quit'},
            ]
        },
        {
            'label': 'Editar',
            'items': [
                {'label': 'Desfazer', 'shortcut': 'Ctrl+Z', 'action': 'undo'},
                {'label': 'Refazer', 'shortcut': 'Ctrl+Y', 'action': 'redo'},
                {'type': 'separator'},
                {'label': 'Cortar', 'shortcut': 'Ctrl+X', 'action': 'cut'},
                {'label': 'Copiar', 'shortcut': 'Ctrl+C', 'action': 'copy'},
                {'label': 'Colar', 'shortcut': 'Ctrl+V', 'action': 'paste'},
                {'type': 'separator'},
                {'label': 'Selecionar Tudo', 'shortcut': 'Ctrl+A', 'action': 'select_all'},
                {'label': 'Localizar', 'shortcut': 'Ctrl+F', 'action': 'find'},
                {'label': 'Substituir', 'shortcut': 'Ctrl+H', 'action': 'replace'},
            ]
        },
        {
            'label': 'Exibir',
            'items': [
                {'label': 'Zoom In', 'shortcut': 'Ctrl++', 'action': 'zoom_in'},
                {'label': 'Zoom Out', 'shortcut': 'Ctrl+-', 'action': 'zoom_out'},
                {'label': 'Zoom Real', 'shortcut': 'Ctrl+0', 'action': 'zoom_reset'},
                {'type': 'separator'},
                {'label': 'Tela Cheia', 'shortcut': 'F11', 'action': 'fullscreen'},
                {'label': 'Modo Escuro', 'action': 'toggle_dark_mode', 'checkable': True},
                {'type': 'separator'},
                {'label': 'Barra de Ferramentas', 'action': 'toggle_toolbar', 'checkable': True, 'checked': True},
                {'label': 'Barra de Status', 'action': 'toggle_statusbar', 'checkable': True, 'checked': True},
            ]
        },
        {
            'label': 'Ferramentas',
            'items': [
                {'label': 'Preferências', 'shortcut': 'Ctrl+,', 'action': 'preferences'},
                {'label': 'Plugins', 'action': 'plugins'},
                {'type': 'separator'},
                {'label': 'Desenvolvedor', 'submenu': [
                    {'label': 'Console', 'shortcut': 'F12', 'action': 'console'},
                    {'label': 'Inspecionar Elemento', 'shortcut': 'Ctrl+Shift+I', 'action': 'inspect'},
                    {'label': 'Recarregar', 'shortcut': 'Ctrl+R', 'action': 'reload'},
                ]},
            ]
        },
        {
            'label': 'Ajuda',
            'items': [
                {'label': 'Documentação', 'action': 'documentation'},
                {'label': 'Atalhos de Teclado', 'shortcut': 'Ctrl+?', 'action': 'shortcuts'},
                {'label': 'Relatório de Bug', 'action': 'report_bug'},
                {'type': 'separator'},
                {'label': 'Sobre', 'action': 'about'},
            ]
        }
    ]
}

# Dados para parâmetros do Menubar
MENUBAR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de menus da barra'],
        ['<code>items.label</code>', 'string', '-', 'Texto do menu'],
        ['<code>items.items</code>', 'array', '-', 'Itens do submenu'],
        ['<code>items.items.label</code>', 'string', '-', 'Texto do item'],
        ['<code>items.items.shortcut</code>', 'string', '-', 'Atalho do teclado'],
        ['<code>items.items.action</code>', 'string', '-', 'Ação a ser executada'],
        ['<code>items.items.checkable</code>', 'boolean', 'false', 'Item pode ser marcado/desmarcado'],
        ['<code>items.items.checked</code>', 'boolean', 'false', 'Estado inicial marcado'],
        ['<code>items.items.submenu</code>', 'array', '-', 'Submenu aninhado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Resizable
RESIZABLE_DATA = {
    'demo_content': {
        'left_panel': {
            'title': 'Navegação',
            'content': [
                'Dashboard',
                'Projetos',
                'Equipe',
                'Configurações',
                'Relatórios'
            ]
        },
        'main_panel': {
            'title': 'Conteúdo Principal',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        'right_panel': {
            'title': 'Painel Lateral',
            'content': 'Informações adicionais, widgets, notificações e outras funcionalidades auxiliares.'
        }
    },
    'code_examples': [
        {
            'title': 'Editor de Código',
            'lines': [
                'import React from "react";',
                '',
                'function App() {',
                '  return (',
                '    <div className="app">',
                '      <h1>Hello World</h1>',
                '    </div>',
                '  );',
                '}',
                '',
                'export default App;'
            ]
        }
    ]
}

# Dados para parâmetros do Resizable
RESIZABLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>direction</code>', 'string', 'horizontal', 'Direção: horizontal, vertical'],
        ['<code>defaultSizes</code>', 'array', '[50, 50]', 'Tamanhos iniciais em porcentagem'],
        ['<code>minSizes</code>', 'array', '[10, 10]', 'Tamanhos mínimos em porcentagem'],
        ['<code>maxSizes</code>', 'array', '[90, 90]', 'Tamanhos máximos em porcentagem'],
        ['<code>onResize</code>', 'function', '-', 'Callback chamado ao redimensionar'],
        ['<code>disabled</code>', 'boolean', 'false', 'Desabilita o redimensionamento'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Scroll Area
SCROLL_AREA_DATA = {
    'long_content': [
        'Item 1 - Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Item 2 - Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'Item 3 - Ut enim ad minim veniam, quis nostrud exercitation ullamco.',
        'Item 4 - Duis aute irure dolor in reprehenderit in voluptate velit esse.',
        'Item 5 - Excepteur sint occaecat cupidatat non proident, sunt in culpa.',
        'Item 6 - Sed ut perspiciatis unde omnis iste natus error sit voluptatem.',
        'Item 7 - Accusantium doloremque laudantium, totam rem aperiam, eaque ipsa.',
        'Item 8 - Quae ab illo inventore veritatis et quasi architecto beatae vitae.',
        'Item 9 - Dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit.',
        'Item 10 - Aspernatur aut odit aut fugit, sed quia consequuntur magni dolores.',
        'Item 11 - Eos qui ratione voluptatem sequi nesciunt, neque porro quisquam est.',
        'Item 12 - Qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.',
        'Item 13 - Sed quia non numquam eius modi tempora incidunt ut labore.',
        'Item 14 - Et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam.',
        'Item 15 - Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse.',
        'Item 16 - Quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat.',
        'Item 17 - Quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio.',
        'Item 18 - Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti.',
        'Item 19 - Atque corrupti quos dolores et quas molestias excepturi sint occaecati.',
        'Item 20 - Cupiditate non provident, similique sunt in culpa qui officia deserunt.',
    ],
    'horizontal_content': [
        'Seção A - Conteúdo horizontal que se estende para além da largura visível',
        'Seção B - Mais conteúdo horizontal que requer rolagem lateral',
        'Seção C - Informações que continuam horizontalmente',
        'Seção D - Dados adicionais na direção horizontal',
        'Seção E - Conteúdo final da rolagem horizontal'
    ]
}

# Dados para parâmetros do Scroll Area
SCROLL_AREA_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>height</code>', 'string', 'auto', 'Altura da área de rolagem'],
        ['<code>width</code>', 'string', 'auto', 'Largura da área de rolagem'],
        ['<code>scrollbarStyle</code>', 'string', 'auto', 'Estilo da barra: auto, overlay, native'],
        ['<code>thumbStyle</code>', 'string', 'default', 'Estilo do thumb: default, thin, thick'],
        ['<code>scrollHideDelay</code>', 'number', '1000', 'Delay para ocultar scrollbar (ms)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados para Sonner
SONNER_DATA = {
    'toast_types': [
        {'type': 'success', 'title': 'Sucesso!', 'description': 'Operação concluída com sucesso.', 'icon': 'check-circled'},
        {'type': 'error', 'title': 'Erro!', 'description': 'Ocorreu um erro ao processar a solicitação.', 'icon': 'cross-circled'},
        {'type': 'warning', 'title': 'Atenção!', 'description': 'Verifique os dados antes de continuar.', 'icon': 'exclamation-triangle'},
        {'type': 'info', 'title': 'Informação', 'description': 'Nova atualização disponível.', 'icon': 'info-circled'},
    ],
    'toast_positions': [
        {'position': 'top-right', 'label': 'Superior Direita'},
        {'position': 'top-left', 'label': 'Superior Esquerda'},
        {'position': 'bottom-right', 'label': 'Inferior Direita'},
        {'position': 'bottom-left', 'label': 'Inferior Esquerda'},
        {'position': 'top-center', 'label': 'Superior Centro'},
        {'position': 'bottom-center', 'label': 'Inferior Centro'},
    ]
}

# Dados para parâmetros do Sonner
SONNER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>type</code>', 'string', 'info', 'Tipo: success, error, warning, info'],
        ['<code>title</code>', 'string', '-', 'Título da notificação'],
        ['<code>description</code>', 'string', '-', 'Descrição da notificação'],
        ['<code>duration</code>', 'number', '4000', 'Duração em milissegundos (0 = permanente)'],
        ['<code>position</code>', 'string', 'top-right', 'Posição na tela'],
        ['<code>closable</code>', 'boolean', 'true', 'Permite fechar manualmente'],
        ['<code>action</code>', 'object', '-', 'Botão de ação personalizado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
} 