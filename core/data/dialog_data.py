"""
Dados específicos para o componente Dialog
"""

DIALOG_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger</code>', 'HTML', '-', 'Elemento que abre o dialog (botão, link, etc.)'],
        ['<code>title</code>', 'string', '-', 'Título do dialog'],
        ['<code>description</code>', 'string', '-', 'Descrição/subtítulo do dialog'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo principal do dialog'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do rodapé (botões, ações)'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, full'],
        ['<code>show_close</code>', 'boolean', 'true', 'Mostrar botão X para fechar'],
        ['<code>close_on_outside</code>', 'boolean', 'true', 'Fechar ao clicar fora do dialog'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

DIALOG_DATA = {
    'params': DIALOG_PARAMS
} 