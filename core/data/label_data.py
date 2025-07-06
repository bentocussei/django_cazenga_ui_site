"""
Dados específicos para o componente Label
"""

LABEL_EXAMPLES = [
    {'text': 'Nome', 'for': 'name', 'required': False},
    {'text': 'E-mail', 'for': 'email', 'required': True},
    {'text': 'Senha', 'for': 'password', 'required': True},
    {'text': 'Telefone', 'for': 'phone', 'required': False},
]

LABEL_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do label'],
        ['<code>for</code>', 'string', '-', 'ID do campo associado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório (adiciona asterisco)'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>description</code>', 'string', '-', 'Texto de ajuda/descrição'],
    ]
}

LABEL_DATA = {
    'examples': LABEL_EXAMPLES,
    'params': LABEL_PARAMS
} 