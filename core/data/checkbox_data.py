"""
Dados específicos para o componente Checkbox
"""

CHECKBOX_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>checked</code>', 'boolean', 'false', 'Se o checkbox está marcado'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o checkbox está desabilitado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>value</code>', 'string', 'on', 'Valor do checkbox'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

CHECKBOX_DATA = {
    'params': CHECKBOX_PARAMS
}
