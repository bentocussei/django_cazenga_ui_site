# Dados do componente Dropdown

# Dropdown de estados
dropdown_states = {
    'options': [
        {'value': 'sp', 'label': 'São Paulo'},
        {'value': 'rj', 'label': 'Rio de Janeiro'},
        {'value': 'mg', 'label': 'Minas Gerais'},
        {'value': 'pr', 'label': 'Paraná'},
        {'value': 'rs', 'label': 'Rio Grande do Sul'},
        {'value': 'sc', 'label': 'Santa Catarina'},
        {'value': 'ba', 'label': 'Bahia'},
        {'value': 'pe', 'label': 'Pernambuco'},
        {'value': 'ce', 'label': 'Ceará'},
        {'value': 'go', 'label': 'Goiás'},
    ]
}

# Dropdown de cores
dropdown_colors = {
    'options': [
        {'value': 'red', 'label': 'Vermelho'},
        {'value': 'blue', 'label': 'Azul'},
        {'value': 'green', 'label': 'Verde'},
        {'value': 'yellow', 'label': 'Amarelo'},
        {'value': 'purple', 'label': 'Roxo'},
        {'value': 'pink', 'label': 'Rosa'},
        {'value': 'orange', 'label': 'Laranja'},
        {'value': 'gray', 'label': 'Cinza'},
    ]
}

# Dropdown básico
dropdown_basic = {
    'options': [
        {'value': 'option1', 'label': 'Opção 1'},
        {'value': 'option2', 'label': 'Opção 2'},
        {'value': 'option3', 'label': 'Opção 3'},
        {'value': 'option4', 'label': 'Opção 4'},
    ]
}

# Dropdown de países
dropdown_countries = {
    'options': [
        {'value': 'br', 'label': 'Brasil'},
        {'value': 'us', 'label': 'Estados Unidos'},
        {'value': 'ca', 'label': 'Canadá'},
        {'value': 'fr', 'label': 'França'},
        {'value': 'de', 'label': 'Alemanha'},
        {'value': 'it', 'label': 'Itália'},
        {'value': 'es', 'label': 'Espanha'},
        {'value': 'jp', 'label': 'Japão'},
        {'value': 'au', 'label': 'Austrália'},
        {'value': 'uk', 'label': 'Reino Unido'},
    ]
}

# Dropdown de tamanhos
dropdown_sizes = {
    'options': [
        {'value': 'xs', 'label': 'Extra Pequeno (XS)'},
        {'value': 's', 'label': 'Pequeno (S)'},
        {'value': 'm', 'label': 'Médio (M)'},
        {'value': 'l', 'label': 'Grande (L)'},
        {'value': 'xl', 'label': 'Extra Grande (XL)'},
        {'value': 'xxl', 'label': 'Extra Extra Grande (XXL)'},
    ]
}

# Parâmetros do dropdown
dropdown_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>options</code>', 'array', '-', 'Array de opções do dropdown (obrigatório)'],
        ['<code>placeholder</code>', 'string', 'Selecione...', 'Texto placeholder'],
        ['<code>selected</code>', 'string', '-', 'Valor da opção selecionada'],
        ['<code>name</code>', 'string', '-', 'Nome do campo (para formulários)'],
        ['<code>id</code>', 'string', '-', 'ID do elemento'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o dropdown está desabilitado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>searchable</code>', 'boolean', 'false', 'Se permite busca nas opções'],
        ['<code>multiple</code>', 'boolean', 'false', 'Se permite seleção múltipla'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
    ]
}

# Dados consolidados do dropdown
DROPDOWN_DATA = {
    'states': dropdown_states,
    'colors': dropdown_colors,
    'basic': dropdown_basic,
    'countries': dropdown_countries,
    'sizes': dropdown_sizes,
    'params': dropdown_params,
} 