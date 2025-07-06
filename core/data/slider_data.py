# Dados para o componente Slider

# Parâmetros do componente
slider_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>min</code>', 'number', '0', 'Valor mínimo'],
        ['<code>max</code>', 'number', '100', 'Valor máximo'],
        ['<code>value</code>', 'number|string', 'min', 'Valor inicial ou "val1,val2" para range'],
        ['<code>step</code>', 'number', '1', 'Incremento do slider'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o slider está desabilitado'],
        ['<code>name</code>', 'string', '-', 'Nome do input hidden (obrigatório para formulários)'],
        ['<code>label</code>', 'string', '-', 'Label do slider'],
        ['<code>show_value</code>', 'boolean', 'false', 'Se mostra valor atual'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>onchange</code>', 'string', '-', 'Função JavaScript para mudança'],
    ]
}

# Dados para as demos
slider_basic = {
    'min': 0,
    'max': 100,
    'value': 50,
    'step': 1,
    'name': 'basic_slider',
    'label': 'Slider Básico',
    'show_value': True
}

slider_range = {
    'min': 0,
    'max': 1000,
    'value': '200,800',
    'step': 50,
    'name': 'range_slider',
    'label': 'Faixa de Valores',
    'show_value': True
}

slider_volume = {
    'min': 0,
    'max': 100,
    'value': 75,
    'step': 5,
    'name': 'volume',
    'label': 'Volume',
    'show_value': True
}

slider_price = {
    'min': 0,
    'max': 5000,
    'value': '1000,3000',
    'step': 100,
    'name': 'price_range',
    'label': 'Faixa de Preço (R$)',
    'show_value': True
}

slider_opacity = {
    'min': 0,
    'max': 1,
    'value': 0.5,
    'step': 0.1,
    'name': 'opacity',
    'label': 'Opacidade',
    'show_value': True
}

slider_disabled = {
    'min': 0,
    'max': 100,
    'value': 30,
    'step': 1,
    'name': 'disabled_slider',
    'label': 'Slider Desabilitado',
    'show_value': True,
    'disabled': True
}

slider_vertical = {
    'min': 0,
    'max': 100,
    'value': 60,
    'step': 1,
    'name': 'vertical_slider',
    'label': 'Slider Vertical',
    'show_value': True,
    'orientation': 'vertical'
} 