# Dados do componente Context Menu

# Menu contextual básico
context_menu_basic = {
    'items': [
        {'label': 'Copiar', 'icon': 'copy', 'action': 'copy'},
        {'label': 'Recortar', 'icon': 'scissors', 'action': 'cut'},
        {'label': 'Colar', 'icon': 'clipboard', 'action': 'paste'},
        {'type': 'separator'},
        {'label': 'Editar', 'icon': 'pencil-1', 'action': 'edit'},
        {'label': 'Excluir', 'icon': 'trash', 'action': 'delete', 'destructive': True}
    ]
}

# Menu contextual com submenus
context_menu_submenu = {
    'items': [
        {'label': 'Visualizar', 'icon': 'eye', 'action': 'view'},
        {
            'label': 'Exportar',
            'icon': 'upload',
            'submenu': [
                {'label': 'Como PDF', 'icon': 'file-text', 'action': 'export-pdf'},
                {'label': 'Como Imagem', 'icon': 'image', 'action': 'export-image'},
                {'label': 'Como JSON', 'icon': 'code', 'action': 'export-json'}
            ]
        },
        {
            'label': 'Compartilhar',
            'icon': 'share-1',
            'submenu': [
                {'label': 'Copiar Link', 'icon': 'link-1', 'action': 'copy-link'},
                {'label': 'Por Email', 'icon': 'envelope-closed', 'action': 'share-email'},
                {'label': 'No Twitter', 'icon': 'twitter-logo', 'action': 'share-twitter'}
            ]
        },
        {'type': 'separator'},
        {'label': 'Configurações', 'icon': 'gear', 'action': 'settings'}
    ]
}

# Menu contextual para lista de arquivos
context_menu_files = {
    'items': [
        {'label': 'Abrir', 'icon': 'eye', 'action': 'open'},
        {'label': 'Baixar', 'icon': 'download', 'action': 'download'},
        {'label': 'Renomear', 'icon': 'pencil-1', 'action': 'rename'},
        {'type': 'separator'},
        {'label': 'Excluir', 'icon': 'trash', 'action': 'delete', 'destructive': True}
    ]
}

# Parâmetros do context menu
context_menu_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Array de itens do menu (obrigatório)'],
        ['<code>trigger</code>', 'string', 'contextmenu', 'Evento que ativa o menu: contextmenu, click'],
        ['<code>position</code>', 'string', 'auto', 'Posição do menu: auto, top, bottom, left, right'],
        ['<code>offset</code>', 'object', '{x: 0, y: 0}', 'Deslocamento da posição do mouse'],
        ['<code>animation</code>', 'boolean', 'true', 'Se deve ter animação'],
        ['<code>backdrop</code>', 'boolean', 'true', 'Se clique fora deve fechar o menu'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>item_class</code>', 'string', '-', 'Classes CSS para itens do menu'],
    ]
}

# Dados consolidados do context menu
CONTEXT_MENU_DATA = {
    'basic': context_menu_basic,
    'submenu': context_menu_submenu,
    'files': context_menu_files,
    'params': context_menu_params,
} 