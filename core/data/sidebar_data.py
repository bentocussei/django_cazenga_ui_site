# Dados do componente Sidebar

# Sidebar básico (navegação)
sidebar_basic = {
    'collapsible': True,
    'collapsed': False,
    'items': [
        {
            'type': 'group',
            'label': 'Principal',
            'items': [
                {'label': 'Dashboard', 'icon': 'dashboard', 'active': True, 'link': '/dashboard'},
                {'label': 'Usuários', 'icon': 'person', 'count': 142, 'link': '/usuarios'},
                {'label': 'Produtos', 'icon': 'box', 'count': 89, 'link': '/produtos'},
                {'label': 'Pedidos', 'icon': 'archive', 'count': 56, 'link': '/pedidos'},
            ]
        },
        {
            'type': 'group',
            'label': 'Vendas',
            'items': [
                {'label': 'Relatórios', 'icon': 'bar-chart', 'link': '/relatorios'},
                {'label': 'Métricas', 'icon': 'activity-log', 'link': '/metricas'},
                {'label': 'Análises', 'icon': 'pie-chart', 'link': '/analises'},
            ]
        },
        {
            'type': 'group',
            'label': 'Sistema',
            'items': [
                {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
                {'label': 'Integrações', 'icon': 'component-instance', 'link': '/integracoes'},
                {'label': 'Logs', 'icon': 'clipboard', 'link': '/logs'},
            ]
        }
    ],
    'footer': '''
    <div class="p-4 border-t border-border">
        <div class="flex items-center space-x-3">
            <div class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center">
                <span class="text-white text-sm font-medium">JS</span>
            </div>
            <div class="flex-1 min-w-0">
                <p class="text-sm font-medium">João Silva</p>
                <p class="text-xs text-gray-500">Administrador</p>
            </div>
        </div>
    </div>
    '''
}

# Sidebar com submenus
sidebar_submenu = {
    'collapsible': True,
    'collapsed': False,
    'items': [
        {
            'type': 'group',
            'label': 'Navegação',
            'items': [
                {'label': 'Início', 'icon': 'home', 'link': '/'},
                {
                    'label': 'Produtos',
                    'icon': 'box',
                    'expandable': True,
                    'expanded': False,
                    'submenu': [
                        {'label': 'Todos os Produtos', 'link': '/produtos'},
                        {'label': 'Categorias', 'link': '/produtos/categorias'},
                        {'label': 'Marcas', 'link': '/produtos/marcas'},
                        {'label': 'Estoque', 'link': '/produtos/estoque'},
                    ]
                },
                {
                    'label': 'Vendas',
                    'icon': 'bar-chart',
                    'expandable': True,
                    'expanded': True,
                    'submenu': [
                        {'label': 'Pedidos', 'link': '/vendas/pedidos', 'active': True},
                        {'label': 'Faturas', 'link': '/vendas/faturas'},
                        {'label': 'Devoluções', 'link': '/vendas/devolucoes'},
                        {'label': 'Relatórios', 'link': '/vendas/relatorios'},
                    ]
                },
                {
                    'label': 'Clientes',
                    'icon': 'person',
                    'expandable': True,
                    'expanded': False,
                    'submenu': [
                        {'label': 'Todos os Clientes', 'link': '/clientes'},
                        {'label': 'Grupos', 'link': '/clientes/grupos'},
                        {'label': 'Segmentação', 'link': '/clientes/segmentacao'},
                    ]
                },
            ]
        },
        {
            'type': 'group',
            'label': 'Ferramentas',
            'items': [
                {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
                {'label': 'Ajuda', 'icon': 'question-mark-circled', 'link': '/ajuda'},
            ]
        }
    ]
}

# Sidebar minimalista
sidebar_minimal = {
    'collapsible': False,
    'collapsed': False,
    'variant': 'minimal',
    'items': [
        {'label': 'Início', 'icon': 'home', 'link': '/'},
        {'label': 'Explorar', 'icon': 'magnifying-glass', 'link': '/explorar'},
        {'label': 'Favoritos', 'icon': 'heart', 'link': '/favoritos'},
        {'label': 'Biblioteca', 'icon': 'archive', 'link': '/biblioteca'},
        {'label': 'Histórico', 'icon': 'clock', 'link': '/historico'},
        {'type': 'separator'},
        {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
        {'label': 'Suporte', 'icon': 'question-mark-circled', 'link': '/suporte'},
    ]
}

# Sidebar com badges
sidebar_with_badges = {
    'collapsible': True,
    'collapsed': False,
    'items': [
        {
            'type': 'group',
            'label': 'Caixa de Entrada',
            'items': [
                {'label': 'Todas as Mensagens', 'icon': 'envelope-closed', 'count': 24, 'link': '/mensagens'},
                {'label': 'Não Lidas', 'icon': 'envelope-open', 'count': 8, 'badge_color': 'red', 'link': '/mensagens/nao-lidas'},
                {'label': 'Importantes', 'icon': 'star', 'count': 3, 'badge_color': 'yellow', 'link': '/mensagens/importantes'},
                {'label': 'Arquivadas', 'icon': 'archive', 'count': 156, 'link': '/mensagens/arquivadas'},
            ]
        },
        {
            'type': 'group',
            'label': 'Projetos',
            'items': [
                {'label': 'Site E-commerce', 'icon': 'component-instance', 'status': 'active', 'progress': 75, 'link': '/projetos/ecommerce'},
                {'label': 'App Mobile', 'icon': 'mobile', 'status': 'review', 'progress': 90, 'link': '/projetos/mobile'},
                {'label': 'Dashboard Admin', 'icon': 'dashboard', 'status': 'completed', 'progress': 100, 'link': '/projetos/dashboard'},
            ]
        },
        {
            'type': 'group',
            'label': 'Equipe',
            'items': [
                {'label': 'Desenvolvedores', 'icon': 'code', 'count': 8, 'link': '/equipe/desenvolvedores'},
                {'label': 'Designers', 'icon': 'design', 'count': 4, 'link': '/equipe/designers'},
                {'label': 'Gerentes', 'icon': 'person', 'count': 2, 'link': '/equipe/gerentes'},
            ]
        }
    ]
}

# Sidebar colapsada
sidebar_collapsed = {
    'collapsible': True,
    'collapsed': True,
    'items': [
        {'label': 'Dashboard', 'icon': 'dashboard', 'active': True, 'link': '/dashboard'},
        {'label': 'Usuários', 'icon': 'person', 'link': '/usuarios'},
        {'label': 'Produtos', 'icon': 'box', 'link': '/produtos'},
        {'label': 'Pedidos', 'icon': 'archive', 'link': '/pedidos'},
        {'label': 'Relatórios', 'icon': 'bar-chart', 'link': '/relatorios'},
        {'type': 'separator'},
        {'label': 'Configurações', 'icon': 'gear', 'link': '/configuracoes'},
        {'label': 'Ajuda', 'icon': 'question-mark-circled', 'link': '/ajuda'},
    ]
}

# Parâmetros do sidebar
sidebar_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '[]', 'Array de itens do sidebar (obrigatório)'],
        ['<code>collapsible</code>', 'boolean', 'true', 'Se o sidebar pode ser colapsado'],
        ['<code>collapsed</code>', 'boolean', 'false', 'Estado inicial colapsado'],
        ['<code>variant</code>', 'string', 'default', 'Variante visual: default, minimal, floating'],
        ['<code>width</code>', 'string', 'w-64', 'Largura do sidebar (classes Tailwind)'],
        ['<code>collapsed_width</code>', 'string', 'w-16', 'Largura quando colapsado'],
        ['<code>label</code>', 'string', '-', 'Texto do item'],
        ['<code>icon</code>', 'string', '-', 'Ícone do item'],
        ['<code>link</code>', 'string', '-', 'URL de destino'],
        ['<code>active</code>', 'boolean', 'false', 'Se o item está ativo'],
        ['<code>count</code>', 'number', '-', 'Número para exibir badge'],
        ['<code>badge_color</code>', 'string', 'gray', 'Cor do badge: gray, red, yellow, green, blue'],
        ['<code>expandable</code>', 'boolean', 'false', 'Se o item pode expandir submenu'],
        ['<code>expanded</code>', 'boolean', 'false', 'Se o submenu está expandido'],
        ['<code>submenu</code>', 'array', '-', 'Array de subitens'],
        ['<code>type</code>', 'string', 'item', 'Tipo: item, group, separator'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do sidebar
SIDEBAR_DATA = {
    'basic': sidebar_basic,
    'submenu': sidebar_submenu,
    'minimal': sidebar_minimal,
    'with_badges': sidebar_with_badges,
    'collapsed': sidebar_collapsed,
    'params': sidebar_params,
} 