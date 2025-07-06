"""
Dados específicos para o componente Switch
"""

SWITCH_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>label</code>', 'string', '-', 'Texto do label'],
        ['<code>checked</code>', 'boolean', 'false', 'Se o switch está ativo'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o switch está desabilitado'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: sm, default, lg'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

SWITCH_DATA = {
    'params': SWITCH_PARAMS
}
