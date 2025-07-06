# Dados do componente Menubar

# Menubar básico (aplicação)
menubar_basic = {
    'items': [
        {
            'label': 'Arquivo',
            'items': [
                {'label': 'Novo', 'shortcut': 'Ctrl+N', 'action': 'new_file'},
                {'label': 'Abrir', 'shortcut': 'Ctrl+O', 'action': 'open_file'},
                {'label': 'Salvar', 'shortcut': 'Ctrl+S', 'action': 'save_file'},
                {'type': 'separator'},
                {'label': 'Importar', 'submenu': [
                    {'label': 'Importar CSV', 'action': 'import_csv'},
                    {'label': 'Importar JSON', 'action': 'import_json'},
                    {'label': 'Importar XML', 'action': 'import_xml'},
                ]},
                {'label': 'Exportar', 'submenu': [
                    {'label': 'Exportar PDF', 'action': 'export_pdf'},
                    {'label': 'Exportar Excel', 'action': 'export_excel'},
                    {'label': 'Exportar Word', 'action': 'export_word'},
                ]},
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
            'label': 'Visualizar',
            'items': [
                {'label': 'Tela Cheia', 'shortcut': 'F11', 'action': 'fullscreen'},
                {'label': 'Zoom In', 'shortcut': 'Ctrl++', 'action': 'zoom_in'},
                {'label': 'Zoom Out', 'shortcut': 'Ctrl+-', 'action': 'zoom_out'},
                {'label': 'Zoom Padrão', 'shortcut': 'Ctrl+0', 'action': 'zoom_reset'},
                {'type': 'separator'},
                {'label': 'Mostrar Sidebar', 'checkbox': True, 'checked': True, 'action': 'toggle_sidebar'},
                {'label': 'Mostrar Barra de Status', 'checkbox': True, 'checked': True, 'action': 'toggle_status'},
                {'label': 'Mostrar Minimap', 'checkbox': True, 'checked': False, 'action': 'toggle_minimap'},
            ]
        },
        {
            'label': 'Ajuda',
            'items': [
                {'label': 'Documentação', 'action': 'open_docs'},
                {'label': 'Atalhos de Teclado', 'shortcut': 'Ctrl+/', 'action': 'show_shortcuts'},
                {'type': 'separator'},
                {'label': 'Reportar Bug', 'action': 'report_bug'},
                {'label': 'Sobre', 'action': 'about'},
            ]
        }
    ]
}

# Menubar simples (site)
menubar_simple = {
    'items': [
        {'label': 'Início', 'link': '/'},
        {'label': 'Produtos', 'link': '/produtos'},
        {'label': 'Serviços', 'submenu': [
            {'label': 'Consultoria', 'link': '/servicos/consultoria'},
            {'label': 'Desenvolvimento', 'link': '/servicos/desenvolvimento'},
            {'label': 'Suporte', 'link': '/servicos/suporte'},
        ]},
        {'label': 'Sobre', 'link': '/sobre'},
        {'label': 'Contato', 'link': '/contato'},
    ]
}

# Menubar com ícones
menubar_with_icons = {
    'items': [
        {
            'label': 'Dashboard',
            'icon': 'dashboard',
            'items': [
                {'label': 'Visão Geral', 'icon': 'eye-open', 'action': 'overview'},
                {'label': 'Relatórios', 'icon': 'bar-chart', 'action': 'reports'},
                {'label': 'Métricas', 'icon': 'activity-log', 'action': 'metrics'},
            ]
        },
        {
            'label': 'Usuários',
            'icon': 'person',
            'items': [
                {'label': 'Todos os Usuários', 'icon': 'group', 'action': 'all_users'},
                {'label': 'Adicionar Usuário', 'icon': 'plus', 'action': 'add_user'},
                {'label': 'Grupos', 'icon': 'mix', 'action': 'groups'},
                {'label': 'Permissões', 'icon': 'lock-closed', 'action': 'permissions'},
            ]
        },
        {
            'label': 'Configurações',
            'icon': 'gear',
            'items': [
                {'label': 'Geral', 'icon': 'gear', 'action': 'general_settings'},
                {'label': 'Segurança', 'icon': 'shield', 'action': 'security'},
                {'label': 'Notificações', 'icon': 'bell', 'action': 'notifications'},
                {'label': 'Integrações', 'icon': 'component-instance', 'action': 'integrations'},
            ]
        }
    ]
}

# Menubar de editor
menubar_editor = {
    'items': [
        {
            'label': 'Ferramentas',
            'items': [
                {'label': 'Texto', 'icon': 'text', 'action': 'text_tool'},
                {'label': 'Forma', 'icon': 'square', 'action': 'shape_tool'},
                {'label': 'Linha', 'icon': 'slash', 'action': 'line_tool'},
                {'label': 'Caneta', 'icon': 'pencil-1', 'action': 'pen_tool'},
                {'type': 'separator'},
                {'label': 'Borracha', 'icon': 'eraser', 'action': 'eraser_tool'},
                {'label': 'Preenchimento', 'icon': 'bucket', 'action': 'fill_tool'},
            ]
        },
        {
            'label': 'Camadas',
            'items': [
                {'label': 'Nova Camada', 'icon': 'plus', 'action': 'new_layer'},
                {'label': 'Duplicar Camada', 'icon': 'copy', 'action': 'duplicate_layer'},
                {'label': 'Excluir Camada', 'icon': 'trash', 'action': 'delete_layer'},
                {'type': 'separator'},
                {'label': 'Mover para Frente', 'icon': 'arrow-up', 'action': 'move_forward'},
                {'label': 'Mover para Trás', 'icon': 'arrow-down', 'action': 'move_backward'},
            ]
        },
        {
            'label': 'Filtros',
            'items': [
                {'label': 'Blur', 'action': 'blur_filter'},
                {'label': 'Sharpen', 'action': 'sharpen_filter'},
                {'label': 'Brightness', 'action': 'brightness_filter'},
                {'label': 'Contrast', 'action': 'contrast_filter'},
                {'type': 'separator'},
                {'label': 'Sepia', 'action': 'sepia_filter'},
                {'label': 'Preto e Branco', 'action': 'grayscale_filter'},
            ]
        }
    ]
}

# Parâmetros do menubar
menubar_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '[]', 'Array de itens do menu (obrigatório)'],
        ['<code>label</code>', 'string', '-', 'Texto do item de menu'],
        ['<code>icon</code>', 'string', '-', 'Ícone do item (nome do ícone)'],
        ['<code>link</code>', 'string', '-', 'URL de destino do item'],
        ['<code>action</code>', 'string', '-', 'Ação JavaScript a ser executada'],
        ['<code>shortcut</code>', 'string', '-', 'Atalho de teclado exibido'],
        ['<code>submenu</code>', 'array', '-', 'Array de subitens'],
        ['<code>checkbox</code>', 'boolean', 'false', 'Se o item é um checkbox'],
        ['<code>checked</code>', 'boolean', 'false', 'Estado inicial do checkbox'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o item está desabilitado'],
        ['<code>type</code>', 'string', '-', 'Tipo especial: "separator"'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>trigger_on_hover</code>', 'boolean', 'false', 'Se abre submenu ao passar o mouse'],
        ['<code>close_on_click</code>', 'boolean', 'true', 'Se fecha menu ao clicar'],
    ]
}

# Dados consolidados do menubar
MENUBAR_DATA = {
    'basic': menubar_basic,
    'simple': menubar_simple,
    'with_icons': menubar_with_icons,
    'editor': menubar_editor,
    'params': menubar_params,
} 