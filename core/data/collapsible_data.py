"""
Dados específicos para o componente Collapsible
"""

COLLAPSIBLE_BASIC_CONTENT = "Conteúdo colapsável..."

COLLAPSIBLE_ADVANCED_CONTENT = """
<div class="space-y-4">
    <h4 class="font-medium">Configurações Avançadas</h4>
    <div class="grid grid-cols-1 gap-4">
        <div class="p-3 border rounded">
            <h5 class="font-medium mb-2">Opção 1</h5>
            <p class="text-sm text-muted-foreground">Configuração para a primeira opção</p>
        </div>
        <div class="p-3 border rounded">
            <h5 class="font-medium mb-2">Opção 2</h5>
            <p class="text-sm text-muted-foreground">Configuração para a segunda opção</p>
        </div>
    </div>
</div>
"""

COLLAPSIBLE_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do collapsible'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo do collapsible'],
        ['<code>open</code>', 'boolean', 'false', 'Se inicia aberto'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se está desabilitado'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

COLLAPSIBLE_DATA = {
    'basic_content': COLLAPSIBLE_BASIC_CONTENT,
    'advanced_content': COLLAPSIBLE_ADVANCED_CONTENT,
    'params': COLLAPSIBLE_PARAMS
} 