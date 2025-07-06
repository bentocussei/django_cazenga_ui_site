"""
Dados específicos para o componente Alert Dialog
"""

ALERT_DIALOG_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do alert dialog'],
        ['<code>description</code>', 'string', '-', 'Descrição do alert dialog'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo adicional personalizado'],
        ['<code>variant</code>', 'string', 'default', 'Variante do alert (default, destructive)'],
        ['<code>x_show</code>', 'string', '-', 'Condição Alpine.js para mostrar/ocultar'],
        ['<code>confirm_text</code>', 'string', 'Confirmar', 'Texto do botão de confirmação'],
        ['<code>cancel_text</code>', 'string', 'Cancelar', 'Texto do botão de cancelamento'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

ALERT_DIALOG_DATA = {
    'params': ALERT_DIALOG_PARAMS
} 