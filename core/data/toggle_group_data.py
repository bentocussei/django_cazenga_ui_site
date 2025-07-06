# Dados para o componente Toggle Group

# Parâmetros do componente
toggle_group_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens/valores (obrigatório)'],
        ['<code>labels</code>', 'array', 'items', 'Lista de labels para exibição'],
        ['<code>icons</code>', 'array', '-', 'Lista de ícones SVG'],
        ['<code>value</code>', 'string|array', '-', 'Valor selecionado inicial'],
        ['<code>type</code>', 'string', 'single', 'Tipo: single, multiple'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, outline'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: sm, default, lg'],
        ['<code>name</code>', 'string', '-', 'Nome do input hidden (obrigatório para formulários)'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o toggle group está desabilitado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>onchange</code>', 'string', '-', 'Função JavaScript para mudança'],
    ]
}

# Dados para as demos
toggle_group_alignment = {
    'items': ['left', 'center', 'right'],
    'labels': ['Esquerda', 'Centro', 'Direita'],
    'icons': [
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 15.75L3 12m0 0l3.75-3.75M3 12h18" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" /></svg>'
    ],
    'value': 'center',
    'type': 'single',
    'name': 'alignment'
}

toggle_group_format = {
    'items': ['bold', 'italic', 'underline'],
    'labels': ['Negrito', 'Itálico', 'Sublinhado'],
    'icons': [
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 2.25h3a3 3 0 0 1 3 3v.75h-3a3 3 0 0 1-3-3V2.25ZM6.75 21.75h3a3 3 0 0 0 3-3v-.75h-3a3 3 0 0 0-3 3v.75ZM6.75 8.25h3a3 3 0 0 1 3 3v.75h-3a3 3 0 0 1-3-3V8.25ZM6.75 15.75h3a3 3 0 0 0 3-3v-.75h-3a3 3 0 0 0-3 3v.75Z" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 6.75h15M4.5 12h15m-15 5.25h15" /></svg>'
    ],
    'value': ['bold'],
    'type': 'multiple',
    'name': 'format'
}

toggle_group_size = {
    'items': ['sm', 'md', 'lg'],
    'labels': ['Pequeno', 'Médio', 'Grande'],
    'value': 'md',
    'type': 'single',
    'name': 'size',
    'variant': 'outline'
}

toggle_group_view = {
    'items': ['list', 'grid', 'card'],
    'labels': ['Lista', 'Grade', 'Cartão'],
    'icons': [
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 6.75h12M8.25 12h12m-12 5.25h12M3.75 6.75h.007v.008H3.75V6.75Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0ZM3.75 12h.007v.008H3.75V12Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm-.375 5.25h.007v.008H3.75v-.008Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6A2.25 2.25 0 0 1 6 3.75h2.25A2.25 2.25 0 0 1 10.5 6v2.25a2.25 2.25 0 0 1-2.25 2.25H6a2.25 2.25 0 0 1-2.25-2.25V6ZM3.75 15.75A2.25 2.25 0 0 1 6 13.5h2.25a2.25 2.25 0 0 1 2.25 2.25V18a2.25 2.25 0 0 1-2.25 2.25H6A2.25 2.25 0 0 1 3.75 18v-2.25ZM13.5 6a2.25 2.25 0 0 1 2.25-2.25H18A2.25 2.25 0 0 1 20.25 6v2.25A2.25 2.25 0 0 1 18 10.5h-2.25a2.25 2.25 0 0 1-2.25-2.25V6ZM13.5 15.75a2.25 2.25 0 0 1 2.25-2.25H18a2.25 2.25 0 0 1 2.25 2.25V18A2.25 2.25 0 0 1 18 20.25h-2.25A2.25 2.25 0 0 1 13.5 18v-2.25Z" /></svg>',
        '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" /></svg>'
    ],
    'value': 'list',
    'type': 'single',
    'name': 'view'
}

toggle_group_priority = {
    'items': ['low', 'medium', 'high'],
    'labels': ['Baixa', 'Média', 'Alta'],
    'value': 'medium',
    'type': 'single',
    'name': 'priority',
    'size': 'sm'
}

toggle_group_disabled = {
    'items': ['option1', 'option2', 'option3'],
    'labels': ['Opção 1', 'Opção 2', 'Opção 3'],
    'value': 'option2',
    'type': 'single',
    'name': 'disabled_toggle',
    'disabled': True
} 