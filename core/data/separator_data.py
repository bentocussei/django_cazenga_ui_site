"""
Dados específicos para o componente Separator
"""

SEPARATOR_EXAMPLES = [
    {'orientation': 'horizontal', 'text': None},
    {'orientation': 'vertical', 'text': None},
    {'orientation': 'horizontal', 'text': 'OU'},
    {'orientation': 'horizontal', 'text': 'Mais opções'},
]

SEPARATOR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>text</code>', 'string', '-', 'Texto opcional no meio do separador'],
        ['<code>color</code>', 'string', 'border', 'Cor: border, muted, primary'],
        ['<code>thickness</code>', 'string', 'default', 'Espessura: thin, default, thick'],
        ['<code>length</code>', 'string', 'full', 'Comprimento: full, partial'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

SEPARATOR_DATA = {
    'examples': SEPARATOR_EXAMPLES,
    'params': SEPARATOR_PARAMS
} 