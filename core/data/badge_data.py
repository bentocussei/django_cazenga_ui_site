"""
Dados específicos para o componente Badge
"""

BADGE_EXAMPLES = [
    {'text': 'Novo', 'variant': 'default'},
    {'text': 'Popular', 'variant': 'secondary'},
    {'text': 'Descontinuado', 'variant': 'destructive'},
    {'text': 'Em breve', 'variant': 'outline'},
]

BADGE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do badge'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, secondary, destructive, outline'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do badge: sm, md, lg'],
        ['<code>icon</code>', 'string', '-', 'Nome do ícone'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

BADGE_DATA = {
    'examples': BADGE_EXAMPLES,
    'params': BADGE_PARAMS
} 