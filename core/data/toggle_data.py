"""
Dados específicos para o componente Toggle
"""

TOGGLE_EXAMPLES = [
    {'text': 'Negrito', 'pressed': False, 'variant': 'default'},
    {'text': 'Itálico', 'pressed': True, 'variant': 'default'},
    {'icon': 'font-bold', 'pressed': False, 'variant': 'default'},
    {'icon': 'font-italic', 'pressed': True, 'variant': 'outline'},
]

TOGGLE_GROUPS = [
    {
        'name': 'Formatação de Texto',
        'items': [
            {'icon': 'font-bold', 'aria_label': 'Negrito'},
            {'icon': 'font-italic', 'aria_label': 'Itálico'},
            {'icon': 'underline', 'aria_label': 'Sublinhado'},
        ]
    },
    {
        'name': 'Alinhamento',
        'items': [
            {'icon': 'text-align-left', 'aria_label': 'Alinhar à esquerda'},
            {'icon': 'text-align-center', 'aria_label': 'Centralizar'},
            {'icon': 'text-align-right', 'aria_label': 'Alinhar à direita'},
        ]
    }
]

TOGGLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do botão toggle'],
        ['<code>icon</code>', 'string', '-', 'Ícone do botão (nome do ícone)'],
        ['<code>pressed</code>', 'boolean', 'false', 'Estado pressionado inicial'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, outline'],
        ['<code>disabled</code>', 'boolean', 'false', 'Desabilita o botão'],
        ['<code>aria_label</code>', 'string', '-', 'Label para acessibilidade'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TOGGLE_DATA = {
    'examples': TOGGLE_EXAMPLES,
    'groups': TOGGLE_GROUPS,
    'params': TOGGLE_PARAMS
} 