# Dados do componente Navigation Menu

# Navigation menu básico (site)
navigation_menu_basic = {
    'orientation': 'horizontal',
    'items': [
        {'label': 'Início', 'link': '/', 'active': True},
        {
            'label': 'Produtos',
            'submenu': [
                {'label': 'Notebooks', 'link': '/produtos/notebooks', 'description': 'Laptops e ultrabooks'},
                {'label': 'Smartphones', 'link': '/produtos/smartphones', 'description': 'Celulares e acessórios'},
                {'label': 'Tablets', 'link': '/produtos/tablets', 'description': 'iPads e tablets Android'},
                {'label': 'Acessórios', 'link': '/produtos/acessorios', 'description': 'Capas, carregadores e mais'},
            ]
        },
        {
            'label': 'Categorias',
            'submenu': [
                {
                    'label': 'Eletrônicos',
                    'items': [
                        {'label': 'Computadores', 'link': '/categoria/computadores'},
                        {'label': 'Áudio & Vídeo', 'link': '/categoria/audio-video'},
                        {'label': 'Gaming', 'link': '/categoria/gaming'},
                    ]
                },
                {
                    'label': 'Casa & Jardim',
                    'items': [
                        {'label': 'Móveis', 'link': '/categoria/moveis'},
                        {'label': 'Decoração', 'link': '/categoria/decoracao'},
                        {'label': 'Jardim', 'link': '/categoria/jardim'},
                    ]
                },
                {
                    'label': 'Moda',
                    'items': [
                        {'label': 'Roupas', 'link': '/categoria/roupas'},
                        {'label': 'Calçados', 'link': '/categoria/calcados'},
                        {'label': 'Acessórios', 'link': '/categoria/acessorios-moda'},
                    ]
                }
            ]
        },
        {'label': 'Sobre', 'link': '/sobre'},
        {'label': 'Contato', 'link': '/contato'},
    ]
}

# Navigation menu com ícones
navigation_menu_with_icons = {
    'orientation': 'horizontal',
    'items': [
        {'label': 'Dashboard', 'icon': 'dashboard', 'link': '/dashboard', 'active': True},
        {
            'label': 'Projetos',
            'icon': 'component-instance',
            'submenu': [
                {'label': 'Todos os Projetos', 'icon': 'grid', 'link': '/projetos', 'description': 'Ver todos os projetos'},
                {'label': 'Criar Novo', 'icon': 'plus', 'link': '/projetos/novo', 'description': 'Iniciar um novo projeto'},
                {'label': 'Templates', 'icon': 'component-placeholder', 'link': '/projetos/templates', 'description': 'Modelos prontos'},
                {'label': 'Arquivados', 'icon': 'archive', 'link': '/projetos/arquivados', 'description': 'Projetos arquivados'},
            ]
        },
        {
            'label': 'Equipe',
            'icon': 'group',
            'submenu': [
                {
                    'label': 'Membros',
                    'icon': 'person',
                    'items': [
                        {'label': 'Desenvolvedores', 'link': '/equipe/desenvolvedores'},
                        {'label': 'Designers', 'link': '/equipe/designers'},
                        {'label': 'Gerentes', 'link': '/equipe/gerentes'},
                    ]
                },
                {
                    'label': 'Permissões',
                    'icon': 'lock-closed',
                    'items': [
                        {'label': 'Roles', 'link': '/equipe/roles'},
                        {'label': 'Configurações', 'link': '/equipe/config'},
                    ]
                }
            ]
        },
        {'label': 'Relatórios', 'icon': 'bar-chart', 'link': '/relatorios'},
        {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
    ]
}

# Navigation menu vertical
navigation_menu_vertical = {
    'orientation': 'vertical',
    'items': [
        {'label': 'Visão Geral', 'icon': 'dashboard', 'link': '/overview', 'active': True},
        {
            'label': 'Gerenciamento',
            'icon': 'gear',
            'submenu': [
                {'label': 'Usuários', 'icon': 'person', 'link': '/users', 'count': 142},
                {'label': 'Grupos', 'icon': 'mix', 'link': '/groups', 'count': 12},
                {'label': 'Permissões', 'icon': 'lock-closed', 'link': '/permissions'},
                {'label': 'Auditoria', 'icon': 'activity-log', 'link': '/audit'},
            ]
        },
        {
            'label': 'Conteúdo',
            'icon': 'component-instance',
            'submenu': [
                {'label': 'Páginas', 'icon': 'reader', 'link': '/pages', 'count': 89},
                {'label': 'Posts', 'icon': 'pencil-1', 'link': '/posts', 'count': 245},
                {'label': 'Mídia', 'icon': 'image', 'link': '/media', 'count': 1205},
                {'label': 'Comentários', 'icon': 'chat-bubble', 'link': '/comments', 'count': 56},
            ]
        },
        {
            'label': 'E-commerce',
            'icon': 'archive',
            'submenu': [
                {'label': 'Produtos', 'icon': 'box', 'link': '/products', 'count': 156},
                {'label': 'Pedidos', 'icon': 'clipboard', 'link': '/orders', 'count': 42},
                {'label': 'Clientes', 'icon': 'person', 'link': '/customers', 'count': 789},
                {'label': 'Cupons', 'icon': 'badge', 'link': '/coupons', 'count': 23},
            ]
        },
        {'label': 'Análises', 'icon': 'bar-chart', 'link': '/analytics'},
        {'label': 'Configurações', 'icon': 'gear', 'link': '/settings'},
    ]
}

# Navigation menu compacto
navigation_menu_compact = {
    'orientation': 'horizontal',
    'compact': True,
    'items': [
        {'label': 'Home', 'link': '/', 'active': True},
        {'label': 'Produtos', 'link': '/produtos'},
        {'label': 'Serviços', 'link': '/servicos'},
        {'label': 'Blog', 'link': '/blog'},
        {'label': 'Contato', 'link': '/contato'},
    ]
}

# Navigation menu de aplicação móvel
navigation_menu_mobile = {
    'orientation': 'vertical',
    'mobile': True,
    'items': [
        {'label': 'Feed', 'icon': 'home', 'link': '/feed', 'active': True},
        {'label': 'Explorar', 'icon': 'magnifying-glass', 'link': '/explorar'},
        {'label': 'Notificações', 'icon': 'bell', 'link': '/notificacoes', 'count': 5},
        {'label': 'Mensagens', 'icon': 'chat-bubble', 'link': '/mensagens', 'count': 12},
        {'label': 'Perfil', 'icon': 'person', 'link': '/perfil'},
        {
            'label': 'Mais',
            'icon': 'dots-horizontal',
            'submenu': [
                {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
                {'label': 'Ajuda', 'icon': 'question-mark-circled', 'link': '/ajuda'},
                {'label': 'Sobre', 'icon': 'info-circled', 'link': '/sobre'},
                {'type': 'separator'},
                {'label': 'Sair', 'icon': 'exit', 'link': '/logout'},
            ]
        }
    ]
}

# Parâmetros do navigation menu
navigation_menu_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '[]', 'Array de itens do menu (obrigatório)'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>compact</code>', 'boolean', 'false', 'Se usa layout compacto'],
        ['<code>mobile</code>', 'boolean', 'false', 'Se é otimizado para mobile'],
        ['<code>label</code>', 'string', '-', 'Texto do item'],
        ['<code>icon</code>', 'string', '-', 'Ícone do item'],
        ['<code>link</code>', 'string', '-', 'URL de destino'],
        ['<code>active</code>', 'boolean', 'false', 'Se o item está ativo'],
        ['<code>count</code>', 'number', '-', 'Número para badge'],
        ['<code>description</code>', 'string', '-', 'Descrição do item (tooltip)'],
        ['<code>submenu</code>', 'array', '-', 'Array de subitens'],
        ['<code>items</code>', 'array', '-', 'Para submenus multinível'],
        ['<code>type</code>', 'string', 'item', 'Tipo: item, separator'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o item está desabilitado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>trigger_on_hover</code>', 'boolean', 'true', 'Se abre submenu ao passar o mouse'],
    ]
}

# Dados consolidados do navigation menu
NAVIGATION_MENU_DATA = {
    'basic': navigation_menu_basic,
    'with_icons': navigation_menu_with_icons,
    'vertical': navigation_menu_vertical,
    'compact': navigation_menu_compact,
    'mobile': navigation_menu_mobile,
    'params': navigation_menu_params,
} 