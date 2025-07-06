"""
Dados específicos para o componente Progress
"""

PROGRESS_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>value</code>', 'number', '0', 'Valor atual do progresso (0-100)'],
        ['<code>max</code>', 'number', '100', 'Valor máximo do progresso'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: sm, default, lg'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, secondary, success, warning, error'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>show_percentage</code>', 'boolean', 'false', 'Mostrar porcentagem'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

PROGRESS_DATA = {
    'params': PROGRESS_PARAMS
}
