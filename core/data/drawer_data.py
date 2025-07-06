# Dados do componente Drawer

# Drawer básico
drawer_basic = {
    'content': '''
    <nav class="space-y-2">
        <a href="#" class="flex items-center px-3 py-2 text-sm text-gray-700 dark:text-gray-300 rounded-radius-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            Início
        </a>
        <a href="#" class="flex items-center px-3 py-2 text-sm text-gray-700 dark:text-gray-300 rounded-radius-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            Perfil
        </a>
        <a href="#" class="flex items-center px-3 py-2 text-sm text-gray-700 dark:text-gray-300 rounded-radius-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            Configurações
        </a>
        <a href="#" class="flex items-center px-3 py-2 text-sm text-gray-700 dark:text-gray-300 rounded-radius-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            Notificações
        </a>
        <a href="#" class="flex items-center px-3 py-2 text-sm text-gray-700 dark:text-gray-300 rounded-radius-md hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors">
            Ajuda
        </a>
    </nav>
    '''
}

# Drawer da direita (configurações)
drawer_right = {
    'content': '''
    <div class="space-y-4">
        <div class="space-y-2">
            <h4 class="text-sm font-medium">Preferências</h4>
            <div class="space-y-3">
                <div class="flex items-center justify-between">
                    <label class="text-sm">Modo escuro</label>
                    <input type="checkbox" class="rounded">
                </div>
                <div class="flex items-center justify-between">
                    <label class="text-sm">Notificações</label>
                    <input type="checkbox" class="rounded" checked>
                </div>
                <div class="flex items-center justify-between">
                    <label class="text-sm">Sons</label>
                    <input type="checkbox" class="rounded">
                </div>
            </div>
        </div>
        <div class="space-y-2">
            <h4 class="text-sm font-medium">Idioma</h4>
            <select class="w-full rounded border p-2 text-sm">
                <option>Português</option>
                <option>English</option>
                <option>Español</option>
            </select>
        </div>
    </div>
    '''
}

# Drawer com footer
drawer_footer = {
    'content': '''
    <div class="space-y-4">
        <div>
            <h4 class="text-lg font-medium mb-2">Detalhes do Item</h4>
            <div class="space-y-3">
                <div>
                    <label class="text-sm font-medium text-gray-500">Nome</label>
                    <p class="text-sm">Produto Exemplo</p>
                </div>
                <div>
                    <label class="text-sm font-medium text-gray-500">Categoria</label>
                    <p class="text-sm">Eletrônicos</p>
                </div>
                <div>
                    <label class="text-sm font-medium text-gray-500">Preço</label>
                    <p class="text-sm font-semibold">R$ 299,90</p>
                </div>
                <div>
                    <label class="text-sm font-medium text-gray-500">Descrição</label>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
            </div>
        </div>
    </div>
    ''',
    'footer': '''
    <div class="flex justify-between space-x-2">
        <button class="flex-1 inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2">
            Cancelar
        </button>
        <button class="flex-1 inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
            Confirmar
        </button>
    </div>
    '''
}

# Parâmetros do drawer
drawer_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', 'Abrir', 'Texto do botão que abre o drawer'],
        ['<code>title</code>', 'string', '-', 'Título do drawer'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo principal do drawer'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer (opcional)'],
        ['<code>position</code>', 'string', 'left', 'Posição do drawer: left, right, top, bottom'],
        ['<code>size</code>', 'string', 'w-80', 'Tamanho do drawer (classes Tailwind)'],
        ['<code>overlay</code>', 'boolean', 'true', 'Se deve mostrar overlay escuro'],
        ['<code>close_button</code>', 'boolean', 'true', 'Se deve mostrar botão de fechar'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do drawer
DRAWER_DATA = {
    'basic': drawer_basic,
    'right': drawer_right,
    'footer': drawer_footer,
    'params': drawer_params,
} 