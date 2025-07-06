"""
Dados específicos para o componente Alert
"""

ALERT_EXAMPLES = [
    {
        'title': 'Sucesso',
        'description': 'Operação realizada com sucesso!',
        'variant': 'success',
        'icon': 'check-circled'
    },
    {
        'title': 'Informação',
        'description': 'Aqui está uma informação importante para você.',
        'variant': 'info',
        'icon': 'info-circled'
    },
    {
        'title': 'Atenção',
        'description': 'Verifique os dados antes de prosseguir.',
        'variant': 'warning',
        'icon': 'exclamation-triangle'
    },
    {
        'title': 'Erro',
        'description': 'Ocorreu um erro ao processar sua solicitação.',
        'variant': 'error',
        'icon': 'cross-circled'
    },
]

ALERT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do alerta'],
        ['<code>description</code>', 'string', '-', 'Descrição/conteúdo do alerta'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, destructive, warning, success'],
        ['<code>icon</code>', 'string', '-', 'Nome do ícone'],
        ['<code>dismissible</code>', 'boolean', 'false', 'Se pode ser fechado'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo HTML personalizado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

ALERT_DATA = {
    'examples': ALERT_EXAMPLES,
    'params': ALERT_PARAMS
} 