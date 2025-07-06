"""
Dados específicos para o componente Tooltip
"""

TOOLTIP_EXAMPLES = [
    {'text': 'Esta é uma dica básica', 'placement': 'top', 'trigger': 'hover'},
    {'text': 'Tooltip à direita', 'placement': 'right', 'trigger': 'hover'},
    {'text': 'Clique para ver', 'placement': 'bottom', 'trigger': 'click'},
    {'text': 'Tooltip com delay', 'placement': 'left', 'trigger': 'hover', 'delay': 500},
]

TOOLTIP_PLACEMENTS = [
    {'name': 'Topo', 'placement': 'top', 'text': 'Tooltip no topo'},
    {'name': 'Direita', 'placement': 'right', 'text': 'Tooltip à direita'},
    {'name': 'Embaixo', 'placement': 'bottom', 'text': 'Tooltip embaixo'},
    {'name': 'Esquerda', 'placement': 'left', 'text': 'Tooltip à esquerda'},
]

TOOLTIP_CONTEXTS = [
    {
        'name': 'Com Ícones',
        'items': [
            {'icon': 'info-circled', 'text': 'Informação importante'},
            {'icon': 'gear', 'text': 'Configurações'},
            {'icon': 'trash', 'text': 'Excluir item'},
        ]
    },
    {
        'name': 'Delays',
        'items': [
            {'text': 'Aparece imediatamente', 'delay': 0},
            {'text': 'Aparece após 500ms', 'delay': 500},
            {'text': 'Aparece após 1 segundo', 'delay': 1000},
        ]
    }
]

TOOLTIP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do tooltip'],
        ['<code>placement</code>', 'string', 'top', 'Posição: top, bottom, left, right'],
        ['<code>trigger</code>', 'string', 'hover', 'Evento: hover, click, focus'],
        ['<code>delay</code>', 'integer', '0', 'Delay em milissegundos para aparecer'],
        ['<code>arrow</code>', 'boolean', 'true', 'Exibir seta do tooltip'],
        ['<code>content</code>', 'string', '-', 'Conteúdo HTML rico (para tooltips avançados)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TOOLTIP_DATA = {
    'examples': TOOLTIP_EXAMPLES,
    'placements': TOOLTIP_PLACEMENTS,
    'contexts': TOOLTIP_CONTEXTS,
    'params': TOOLTIP_PARAMS
} 