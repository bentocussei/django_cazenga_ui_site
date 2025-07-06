"""
Dados específicos para o componente Skeleton
"""

SKELETON_EXAMPLES = [
    {'type': 'text', 'lines': 3, 'width': 'full'},
    {'type': 'avatar', 'size': 'md'},
    {'type': 'card', 'height': '200px'},
    {'type': 'line', 'width': '3/4'},
    {'type': 'block', 'width': 'full', 'height': '100px'},
]

SKELETON_LAYOUTS = [
    {
        'name': 'Lista de Usuários',
        'items': [
            {'type': 'avatar', 'size': 'md'},
            {'type': 'text', 'lines': 2, 'width': '3/4'},
        ]
    },
    {
        'name': 'Card de Produto',
        'items': [
            {'type': 'block', 'height': '200px'},
            {'type': 'text', 'lines': 3},
        ]
    }
]

SKELETON_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>type</code>', 'string', 'text', 'Tipo: text, avatar, card, line, block'],
        ['<code>lines</code>', 'integer', '1', 'Número de linhas (para tipo text)'],
        ['<code>width</code>', 'string', 'full', 'Largura: full, 1/2, 1/3, 1/4, 3/4'],
        ['<code>height</code>', 'string', 'auto', 'Altura específica'],
        ['<code>size</code>', 'string', 'md', 'Tamanho (para avatar): sm, md, lg'],
        ['<code>animate</code>', 'boolean', 'true', 'Ativar/desativar animação'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

SKELETON_DATA = {
    'examples': SKELETON_EXAMPLES,
    'layouts': SKELETON_LAYOUTS,
    'params': SKELETON_PARAMS
} 