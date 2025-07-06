# Dados para o componente Select

# Parâmetros do componente
select_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório)'],
        ['<code>options</code>', 'array', '-', 'Lista de opções [{\"value\": \"val\", \"label\": \"Label\"}, ...]'],
        ['<code>placeholder</code>', 'string', '"Selecione uma opção"', 'Texto placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor selecionado inicialmente'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: sm, default'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o select está desabilitado'],
        ['<code>multiple</code>', 'boolean', 'false', 'Se permite seleção múltipla'],
        ['<code>searchable</code>', 'boolean', 'false', 'Se permite busca'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>on_change</code>', 'string', '-', 'Função JavaScript no change'],
    ]
}

# Dados para as demos
select_basic_options = [
    {"value": "option1", "label": "Opção 1"},
    {"value": "option2", "label": "Opção 2"},
    {"value": "option3", "label": "Opção 3"},
]

select_countries = [
    {"value": "br", "label": "Brasil"},
    {"value": "us", "label": "Estados Unidos"},
    {"value": "ca", "label": "Canadá"},
    {"value": "mx", "label": "México"},
    {"value": "ar", "label": "Argentina"},
    {"value": "cl", "label": "Chile"},
    {"value": "co", "label": "Colômbia"},
    {"value": "pe", "label": "Peru"},
]

select_priority = [
    {"value": "low", "label": "Baixa"},
    {"value": "medium", "label": "Média"},
    {"value": "high", "label": "Alta"},
    {"value": "urgent", "label": "Urgente"},
]

select_status = [
    {"value": "draft", "label": "Rascunho"},
    {"value": "review", "label": "Em revisão"},
    {"value": "approved", "label": "Aprovado"},
    {"value": "published", "label": "Publicado"},
    {"value": "archived", "label": "Arquivado"},
]

select_sizes = [
    {"value": "xs", "label": "Extra Small (XS)"},
    {"value": "sm", "label": "Small (SM)"},
    {"value": "md", "label": "Medium (MD)"},
    {"value": "lg", "label": "Large (LG)"},
    {"value": "xl", "label": "Extra Large (XL)"},
    {"value": "xxl", "label": "XX Large (XXL)"},
] 