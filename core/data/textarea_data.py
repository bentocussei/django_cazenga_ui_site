"""
Dados específicos para o componente Textarea
"""

TEXTAREA_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>placeholder</code>', 'string', '-', 'Texto de placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor inicial'],
        ['<code>rows</code>', 'number', '4', 'Número de linhas'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>readonly</code>', 'boolean', 'false', 'Se o campo é somente leitura'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>resize</code>', 'string', 'vertical', 'Redimensionamento: none, vertical, horizontal, both'],
        ['<code>maxlength</code>', 'number', '-', 'Limite máximo de caracteres'],
        ['<code>minlength</code>', 'number', '-', 'Limite mínimo de caracteres'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

TEXTAREA_DATA = {
    'params': TEXTAREA_PARAMS
} 