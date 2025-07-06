"""
Dados específicos para o componente Button
"""

BUTTON_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>text</code>', 'string', '-', 'Texto do botão'],
        ['<code>variant</code>', 'string', 'default', 'Variante: default, destructive, outline, secondary, ghost, link'],
        ['<code>size</code>', 'string', 'default', 'Tamanho: default, sm, lg, icon'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se o botão está desabilitado'],
        ['<code>type</code>', 'string', 'button', 'Tipo: button, submit, reset'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

BUTTON_DATA = {
    'params': BUTTON_PARAMS
}
