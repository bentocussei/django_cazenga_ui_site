"""
Dados específicos para o componente Radio Group
"""

RADIO_GROUP_OPTIONS = {
    'basic': [
        {'value': 'option1', 'label': 'Opção 1'},
        {'value': 'option2', 'label': 'Opção 2'},
        {'value': 'option3', 'label': 'Opção 3'},
    ],
    'payment': [
        {'value': 'card', 'label': 'Cartão de Crédito', 'description': 'Pagar com cartão de crédito ou débito'},
        {'value': 'pix', 'label': 'PIX', 'description': 'Pagamento instantâneo via PIX'},
        {'value': 'boleto', 'label': 'Boleto Bancário', 'description': 'Pagamento via boleto bancário'},
    ],
    'plan': [
        {'value': 'basic', 'label': 'Básico', 'description': 'Recursos essenciais para começar'},
        {'value': 'pro', 'label': 'Pro', 'description': 'Recursos avançados para profissionais'},
        {'value': 'enterprise', 'label': 'Enterprise', 'description': 'Recursos completos para empresas'},
    ],
    'size': [
        {'value': 'sm', 'label': 'Pequeno'},
        {'value': 'md', 'label': 'Médio'},
        {'value': 'lg', 'label': 'Grande'},
    ],
    'disabled': [
        {'value': 'available', 'label': 'Disponível'},
        {'value': 'limited', 'label': 'Limitado', 'disabled': True},
        {'value': 'unavailable', 'label': 'Indisponível', 'disabled': True},
    ],
}

RADIO_GROUP_DATA = {
    'basic': [
        {'value': 'option1', 'label': 'Opção 1'},
        {'value': 'option2', 'label': 'Opção 2'},
        {'value': 'option3', 'label': 'Opção 3'},
    ],
    'payment': [
        {'value': 'card', 'label': 'Cartão de Crédito', 'description': 'Visa, MasterCard, American Express'},
        {'value': 'pix', 'label': 'PIX', 'description': 'Pagamento instantâneo'},
        {'value': 'bank', 'label': 'Transferência Bancária', 'description': 'TED ou DOC'},
        {'value': 'boleto', 'label': 'Boleto Bancário', 'description': 'Vencimento em 3 dias úteis'},
    ],
    'size': [
        {'value': 'xs', 'label': 'XS'},
        {'value': 'sm', 'label': 'SM'},
        {'value': 'md', 'label': 'MD'},
        {'value': 'lg', 'label': 'LG'},
        {'value': 'xl', 'label': 'XL'},
    ],
    'disabled': [
        {'value': 'available', 'label': 'Disponível'},
        {'value': 'limited', 'label': 'Limitado'},
        {'value': 'unavailable', 'label': 'Indisponível', 'disabled': True},
    ],
    'plan': [
        {'value': 'basic', 'label': 'Básico', 'description': 'Recursos essenciais'},
        {'value': 'pro', 'label': 'Profissional', 'description': 'Recursos avançados'},
        {'value': 'enterprise', 'label': 'Empresarial', 'description': 'Recursos completos'},
    ]
}

RADIO_GROUP_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do grupo de radio buttons (obrigatório)'],
        ['<code>options</code>', 'array', '-', 'Lista de opções do grupo (obrigatório)'],
        ['<code>value</code>', 'string', '-', 'Valor selecionado inicialmente'],
        ['<code>orientation</code>', 'string', 'vertical', 'Orientação: vertical, horizontal'],
        ['<code>disabled</code>', 'boolean', 'false', 'Desabilitar todo o grupo'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>on_change</code>', 'string', '-', 'Função JavaScript no evento change'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
} 