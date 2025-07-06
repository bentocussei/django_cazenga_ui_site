# Dados do componente Dropdown Menu

# Dropdown menu básico
dropdown_menu_basic = {
    'trigger_text': 'Menu',
    'items': [
        {'label': 'Início', 'icon': 'home', 'href': '/'},
        {'label': 'Perfil', 'icon': 'person', 'href': '/profile'},
        {'label': 'Configurações', 'icon': 'gear', 'href': '/settings'},
        {'type': 'separator'},
        {'label': 'Sair', 'icon': 'exit', 'href': '/logout'}
    ]
}

# Dropdown menu de usuário
dropdown_menu_user = {
    'trigger_text': 'João Silva',
    'trigger_avatar': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=32&h=32&fit=crop&crop=face',
    'items': [
        {'label': 'Meu Perfil', 'icon': 'person', 'href': '/profile'},
        {'label': 'Configurações', 'icon': 'gear', 'href': '/settings'},
        {'label': 'Faturamento', 'icon': 'card-stack', 'href': '/billing'},
        {'type': 'separator'},
        {'label': 'Equipe', 'icon': 'group', 'href': '/team'},
        {'label': 'Convidar usuários', 'icon': 'plus', 'href': '/invite'},
        {'type': 'separator'},
        {'label': 'Suporte', 'icon': 'question-mark', 'href': '/support'},
        {'label': 'Documentação', 'icon': 'book', 'href': '/docs'},
        {'type': 'separator'},
        {'label': 'Sair', 'icon': 'exit', 'href': '/logout'}
    ]
}

# Dropdown menu com submenus
dropdown_menu_submenu = {
    'trigger_text': 'Ações',
    'items': [
        {'label': 'Novo Item', 'icon': 'plus', 'href': '/new'},
        {
            'label': 'Importar',
            'icon': 'download',
            'submenu': [
                {'label': 'Do CSV', 'icon': 'file-text', 'href': '/import/csv'},
                {'label': 'Do JSON', 'icon': 'code', 'href': '/import/json'},
                {'label': 'Do Excel', 'icon': 'table', 'href': '/import/excel'}
            ]
        },
        {
            'label': 'Exportar',
            'icon': 'upload',
            'submenu': [
                {'label': 'Para CSV', 'icon': 'file-text', 'href': '/export/csv'},
                {'label': 'Para JSON', 'icon': 'code', 'href': '/export/json'},
                {'label': 'Para PDF', 'icon': 'document', 'href': '/export/pdf'}
            ]
        },
        {'type': 'separator'},
        {'label': 'Configurações', 'icon': 'gear', 'href': '/settings'}
    ]
}

# Dropdown menu de notificações
dropdown_menu_notifications = {
    'trigger_icon': 'bell',
    'trigger_badge': 3,
    'items': [
        {
            'type': 'notification',
            'title': 'Nova mensagem',
            'description': 'Você recebeu uma nova mensagem de Ana Silva',
            'time': '2 min atrás',
            'unread': True
        },
        {
            'type': 'notification',
            'title': 'Pedido confirmado',
            'description': 'Seu pedido #1234 foi confirmado e será enviado em breve',
            'time': '1 hora atrás',
            'unread': True
        },
        {
            'type': 'notification',
            'title': 'Atualização disponível',
            'description': 'Uma nova versão do sistema está disponível',
            'time': '2 horas atrás',
            'unread': False
        },
        {'type': 'separator'},
        {'label': 'Ver todas as notificações', 'href': '/notifications'},
        {'label': 'Configurar notificações', 'href': '/notifications/settings'}
    ]
}

# Parâmetros do dropdown menu
dropdown_menu_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', '-', 'Texto do trigger do menu'],
        ['<code>trigger_icon</code>', 'string', '-', 'Ícone do trigger (opcional)'],
        ['<code>trigger_avatar</code>', 'string', '-', 'Avatar do trigger (opcional)'],
        ['<code>trigger_badge</code>', 'number', '-', 'Badge numérico no trigger (opcional)'],
        ['<code>items</code>', 'array', '-', 'Array de itens do menu (obrigatório)'],
        ['<code>position</code>', 'string', 'bottom', 'Posição do menu: top, bottom, left, right'],
        ['<code>align</code>', 'string', 'start', 'Alinhamento: start, center, end'],
        ['<code>offset</code>', 'number', '5', 'Distância do trigger em pixels'],
        ['<code>animation</code>', 'boolean', 'true', 'Se deve ter animação'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do dropdown menu
DROPDOWN_MENU_DATA = {
    'basic': dropdown_menu_basic,
    'user': dropdown_menu_user,
    'submenu': dropdown_menu_submenu,
    'notifications': dropdown_menu_notifications,
    'params': dropdown_menu_params,
} 