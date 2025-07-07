"""
Dados específicos para o componente Breadcrumb
"""

BREADCRUMB_ITEMS = [
    [
        {'label': 'Início', 'href': '/'},
        {'label': 'Componentes', 'href': '/components/ui/'},
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

BREADCRUMB_WITH_ICONS = [
    {'label': 'Home', 'href': '/', 'icon': 'home'},
    {'label': 'Documentos', 'href': '/docs', 'icon': 'file-text'},
    {'label': 'Projetos', 'href': '/docs/projetos', 'icon': 'folder'},
    {'label': 'Projeto Alpha', 'current': True, 'icon': 'star'}
]

BREADCRUMB_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do breadcrumb (obrigatório)'],
        ['<code>separator</code>', 'string/HTML', 'seta', 'Separador customizado entre os itens'],
        ['<code>max_items</code>', 'number', '5', 'Número máximo de itens antes de mostrar ellipsis'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

BREADCRUMB_DATA = {
    'items': [
        # Exemplo básico
        [
            {'label': 'Home', 'href': '/'},
            {'label': 'Produtos', 'href': '/produtos'},
            {'label': 'Categoria', 'href': '/produtos/categoria'},
            {'label': 'Item Atual', 'current': True}
        ],
        # Múltiplos níveis
        [
            {'label': 'Dashboard', 'href': '/dashboard'},
            {'label': 'Usuários', 'href': '/dashboard/usuarios'},
            {'label': 'Perfil', 'href': '/dashboard/usuarios/perfil'},
            {'label': 'Configurações', 'href': '/dashboard/usuarios/perfil/config'},
            {'label': 'Segurança', 'current': True}
        ],
        # Muitos itens
        [
            {'label': 'Raiz', 'href': '/'},
            {'label': 'Nível 1', 'href': '/nivel1'},
            {'label': 'Nível 2', 'href': '/nivel1/nivel2'},
            {'label': 'Nível 3', 'href': '/nivel1/nivel2/nivel3'},
            {'label': 'Nível 4', 'href': '/nivel1/nivel2/nivel3/nivel4'},
            {'label': 'Nível 5', 'href': '/nivel1/nivel2/nivel3/nivel4/nivel5'},
            {'label': 'Nível 6', 'href': '/nivel1/nivel2/nivel3/nivel4/nivel5/nivel6'},
            {'label': 'Página Atual', 'current': True}
        ]
    ],
    'with_icons': BREADCRUMB_WITH_ICONS,
    'params': BREADCRUMB_PARAMS
} 