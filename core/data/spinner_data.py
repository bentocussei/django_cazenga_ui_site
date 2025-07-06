"""
Dados específicos para o componente Spinner
"""

SPINNER_EXAMPLES = [
    {'size': 'sm', 'color': 'primary', 'text': None},
    {'size': 'md', 'color': 'secondary', 'text': 'Carregando...'},
    {'size': 'lg', 'color': 'success', 'text': 'Processando...'},
    {'size': 'xl', 'color': 'warning', 'text': None},
]

SPINNER_CONTEXTS = [
    {
        'name': 'Em Botões',
        'examples': [
            {'size': 'sm', 'color': 'white', 'inline': True},
            {'size': 'sm', 'color': 'primary', 'inline': True},
        ]
    },
    {
        'name': 'Como Overlay',
        'examples': [
            {'size': 'lg', 'color': 'primary', 'overlay': True, 'text': 'Carregando dados...'},
        ]
    },
    {
        'name': 'Centralizado',
        'examples': [
            {'size': 'md', 'color': 'primary', 'centered': True, 'text': 'Aguarde...'},
        ]
    }
]

SPINNER_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl'],
        ['<code>color</code>', 'string', 'primary', 'Cor: primary, secondary, success, warning, danger'],
        ['<code>text</code>', 'string', '-', 'Texto a ser exibido junto ao spinner'],
        ['<code>centered</code>', 'boolean', 'false', 'Centraliza o spinner no container'],
        ['<code>overlay</code>', 'boolean', 'false', 'Exibe como overlay sobre o conteúdo'],
        ['<code>inline</code>', 'boolean', 'false', 'Exibe inline (para uso em botões)'],
        ['<code>animate</code>', 'boolean', 'true', 'Ativar/desativar animação'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

SPINNER_DATA = {
    'examples': SPINNER_EXAMPLES,
    'contexts': SPINNER_CONTEXTS,
    'params': SPINNER_PARAMS
} 