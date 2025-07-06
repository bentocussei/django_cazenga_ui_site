"""
Dados específicos para o componente Input
"""

INPUT_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>name</code>', 'string', '-', 'Nome do campo (obrigatório para formulários)'],
        ['<code>type</code>', 'string', 'text', 'Tipo do input: text, email, password, number, etc.'],
        ['<code>id</code>', 'string', 'name', 'ID do elemento'],
        ['<code>placeholder</code>', 'string', '-', 'Texto de placeholder'],
        ['<code>value</code>', 'string', '-', 'Valor inicial'],
        ['<code>required</code>', 'boolean', 'false', 'Se o campo é obrigatório'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o campo está desabilitado'],
        ['<code>readonly</code>', 'boolean', 'false', 'Se o campo é somente leitura'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para two-way binding'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>min</code>', 'number', '-', 'Valor mínimo (para type="number")'],
        ['<code>max</code>', 'number', '-', 'Valor máximo (para type="number")'],
        ['<code>step</code>', 'number', '-', 'Incremento (para type="number")'],
        ['<code>minlength</code>', 'number', '-', 'Comprimento mínimo do texto'],
        ['<code>maxlength</code>', 'number', '-', 'Comprimento máximo do texto'],
        ['<code>pattern</code>', 'string', '-', 'Padrão regex para validação'],
        ['<code>autocomplete</code>', 'string', '-', 'Controle de autocompletar'],
        ['<code>autofocus</code>', 'boolean', 'false', 'Focar automaticamente no campo'],
    ]
}

INPUT_DATA = {
    'params': INPUT_PARAMS
}
