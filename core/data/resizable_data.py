# Dados do componente Resizable

# Resizable horizontal (dois painéis)
resizable_horizontal = {
    'direction': 'horizontal',
    'panels': ['sidebar', 'main'],
    'sizes': [25, 75],
    'min_sizes': [200, 400],
    'contents': [
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-4">Sidebar</h4>
            <nav class="space-y-2">
                <a href="#" class="block px-3 py-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700">Dashboard</a>
                <a href="#" class="block px-3 py-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700">Usuários</a>
                <a href="#" class="block px-3 py-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700">Relatórios</a>
                <a href="#" class="block px-3 py-2 rounded hover:bg-gray-100 dark:hover:bg-gray-700">Configurações</a>
            </nav>
        </div>
        ''',
        '''
        <div class="p-6 h-full">
            <h2 class="text-2xl font-bold mb-4">Conteúdo Principal</h2>
            <p class="text-gray-600 dark:text-gray-400 mb-6">
                Este é o painel principal. Você pode redimensionar os painéis arrastando a barra de divisão.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 bg-gray-50 dark:bg-gray-800 rounded-lg">
                    <h3 class="font-semibold mb-2">Card 1</h3>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Conteúdo do primeiro card.</p>
                </div>
                <div class="p-4 bg-gray-50 dark:bg-gray-800 rounded-lg">
                    <h3 class="font-semibold mb-2">Card 2</h3>
                    <p class="text-sm text-gray-600 dark:text-gray-400">Conteúdo do segundo card.</p>
                </div>
            </div>
        </div>
        '''
    ]
}

# Resizable vertical (dois painéis)
resizable_vertical = {
    'direction': 'vertical',
    'panels': ['header', 'content'],
    'sizes': [30, 70],
    'min_sizes': [100, 200],
    'contents': [
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-2">Header</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                Área do cabeçalho com informações importantes.
            </p>
            <div class="flex space-x-2">
                <button class="px-3 py-1 bg-blue-500 text-white text-sm rounded">Ação 1</button>
                <button class="px-3 py-1 bg-gray-500 text-white text-sm rounded">Ação 2</button>
            </div>
        </div>
        ''',
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-4">Conteúdo</h4>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                Área principal do conteúdo. Redimensione arrastando a barra horizontal.
            </p>
            <div class="space-y-3">
                <div class="p-3 bg-gray-50 dark:bg-gray-800 rounded text-sm">Item 1</div>
                <div class="p-3 bg-gray-50 dark:bg-gray-800 rounded text-sm">Item 2</div>
                <div class="p-3 bg-gray-50 dark:bg-gray-800 rounded text-sm">Item 3</div>
                <div class="p-3 bg-gray-50 dark:bg-gray-800 rounded text-sm">Item 4</div>
            </div>
        </div>
        '''
    ]
}

# Resizable três painéis (layout de editor)
resizable_three_panels = {
    'direction': 'horizontal',
    'panels': ['explorer', 'editor', 'sidebar'],
    'sizes': [20, 60, 20],
    'min_sizes': [150, 300, 150],
    'contents': [
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-4">Explorer</h4>
            <div class="space-y-1 text-sm">
                <div class="flex items-center space-x-2">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <span>src</span>
                </div>
                <div class="pl-4 space-y-1">
                    <div class="flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M4 4a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2H4z"></path>
                        </svg>
                        <span>index.js</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M4 4a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2H4z"></path>
                        </svg>
                        <span>styles.css</span>
                    </div>
                </div>
            </div>
        </div>
        ''',
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-4">Editor</h4>
            <div class="bg-gray-900 text-green-400 p-4 rounded font-mono text-sm h-full overflow-auto">
                <div>function App() {</div>
                <div>&nbsp;&nbsp;return (</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;&lt;div className="app"&gt;</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;Hello World&lt;/h1&gt;</div>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;</div>
                <div>&nbsp;&nbsp;);</div>
                <div>}</div>
            </div>
        </div>
        ''',
        '''
        <div class="p-4 h-full">
            <h4 class="font-semibold mb-4">Propriedades</h4>
            <div class="space-y-3 text-sm">
                <div>
                    <label class="block font-medium mb-1">Width</label>
                    <input type="text" value="100%" class="w-full px-2 py-1 border rounded text-xs">
                </div>
                <div>
                    <label class="block font-medium mb-1">Height</label>
                    <input type="text" value="auto" class="w-full px-2 py-1 border rounded text-xs">
                </div>
                <div>
                    <label class="block font-medium mb-1">Background</label>
                    <input type="color" value="#ffffff" class="w-full h-8 border rounded">
                </div>
            </div>
        </div>
        '''
    ]
}

# Resizable aninhado (layout complexo)
resizable_nested = {
    'direction': 'horizontal',
    'panels': ['left', 'right'],
    'sizes': [50, 50],
    'min_sizes': [300, 300],
    'nested': True,
    'contents': [
        '''
        <div class="h-full">
            <div class="p-4 border-b">
                <h4 class="font-semibold">Painel Esquerdo</h4>
            </div>
            <div class="flex-1 p-4">
                <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">
                    Este é um painel que pode conter outro componente resizable aninhado.
                </p>
                <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded">
                    <h5 class="font-medium mb-2">Conteúdo aninhado</h5>
                    <p class="text-xs text-gray-500">
                        Aqui você poderia ter mais painéis redimensionáveis.
                    </p>
                </div>
            </div>
        </div>
        ''',
        '''
        <div class="h-full">
            <div class="p-4 border-b">
                <h4 class="font-semibold">Painel Direito</h4>
            </div>
            <div class="flex-1 p-4">
                <div class="space-y-3">
                    <div class="p-3 bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded">
                        <h5 class="font-medium text-blue-800 dark:text-blue-200">Informação</h5>
                        <p class="text-sm text-blue-600 dark:text-blue-300">
                            Layout complexo com painéis aninhados.
                        </p>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div class="p-2 bg-gray-100 dark:bg-gray-700 rounded text-center text-sm">A</div>
                        <div class="p-2 bg-gray-100 dark:bg-gray-700 rounded text-center text-sm">B</div>
                        <div class="p-2 bg-gray-100 dark:bg-gray-700 rounded text-center text-sm">C</div>
                        <div class="p-2 bg-gray-100 dark:bg-gray-700 rounded text-center text-sm">D</div>
                    </div>
                </div>
            </div>
        </div>
        '''
    ]
}

# Resizable com conteúdo dinâmico
resizable_dynamic = {
    'direction': 'horizontal',
    'panels': ['list', 'detail'],
    'sizes': [40, 60],
    'min_sizes': [250, 350],
    'contents': [
        '''
        <div class="h-full">
            <div class="p-4 border-b">
                <h4 class="font-semibold">Lista de Items</h4>
                <p class="text-xs text-gray-500">Clique em um item para ver detalhes</p>
            </div>
            <div class="flex-1 overflow-auto">
                <div class="space-y-1 p-2">
                    <div class="p-3 hover:bg-gray-50 dark:hover:bg-gray-700 rounded cursor-pointer border-l-2 border-blue-500">
                        <div class="font-medium">Projeto Alpha</div>
                        <div class="text-sm text-gray-500">Status: Ativo</div>
                    </div>
                    <div class="p-3 hover:bg-gray-50 dark:hover:bg-gray-700 rounded cursor-pointer">
                        <div class="font-medium">Projeto Beta</div>
                        <div class="text-sm text-gray-500">Status: Em desenvolvimento</div>
                    </div>
                    <div class="p-3 hover:bg-gray-50 dark:hover:bg-gray-700 rounded cursor-pointer">
                        <div class="font-medium">Projeto Gamma</div>
                        <div class="text-sm text-gray-500">Status: Pausado</div>
                    </div>
                </div>
            </div>
        </div>
        ''',
        '''
        <div class="h-full">
            <div class="p-4 border-b">
                <h4 class="font-semibold">Detalhes do Projeto</h4>
            </div>
            <div class="flex-1 p-4 overflow-auto">
                <div class="space-y-4">
                    <div>
                        <h5 class="font-semibold text-lg mb-2">Projeto Alpha</h5>
                        <div class="grid grid-cols-2 gap-4 text-sm">
                            <div>
                                <span class="text-gray-500">Status:</span>
                                <span class="ml-2 px-2 py-1 bg-green-100 text-green-800 rounded text-xs">Ativo</span>
                            </div>
                            <div>
                                <span class="text-gray-500">Progresso:</span>
                                <span class="ml-2 font-medium">75%</span>
                            </div>
                            <div>
                                <span class="text-gray-500">Prazo:</span>
                                <span class="ml-2">15/02/2024</span>
                            </div>
                            <div>
                                <span class="text-gray-500">Equipe:</span>
                                <span class="ml-2">8 membros</span>
                            </div>
                        </div>
                    </div>
                    <div>
                        <h6 class="font-medium mb-2">Descrição</h6>
                        <p class="text-sm text-gray-600 dark:text-gray-400">
                            Desenvolvimento de nova aplicação web utilizando tecnologias modernas
                            como React, TypeScript e GraphQL.
                        </p>
                    </div>
                    <div>
                        <h6 class="font-medium mb-2">Tarefas Recentes</h6>
                        <div class="space-y-2">
                            <div class="flex items-center justify-between text-sm">
                                <span>Implementar autenticação</span>
                                <span class="px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs">Em andamento</span>
                            </div>
                            <div class="flex items-center justify-between text-sm">
                                <span>Criar componentes base</span>
                                <span class="px-2 py-1 bg-green-100 text-green-800 rounded text-xs">Concluído</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
    ]
}

# Parâmetros do resizable
resizable_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>direction</code>', 'string', 'horizontal', 'Direção: horizontal, vertical'],
        ['<code>panels</code>', 'array', '[]', 'Array com IDs/nomes dos painéis'],
        ['<code>sizes</code>', 'array', '[]', 'Array com tamanhos iniciais (%)'],
        ['<code>min_sizes</code>', 'array', '[]', 'Array com tamanhos mínimos (px)'],
        ['<code>max_sizes</code>', 'array', '[]', 'Array com tamanhos máximos (px)'],
        ['<code>contents</code>', 'array', '[]', 'Array com conteúdo HTML de cada painel'],
        ['<code>resizable</code>', 'array', '[]', 'Array indicando quais divisores são redimensionáveis'],
        ['<code>snap</code>', 'boolean', 'false', 'Se deve "encaixar" em tamanhos específicos'],
        ['<code>snap_offset</code>', 'number', '30', 'Distância para ativar o snap (px)'],
        ['<code>collapse_size</code>', 'number', '50', 'Tamanho mínimo antes de colapsar (px)'],
        ['<code>expand_to_min</code>', 'boolean', 'true', 'Se deve expandir para tamanho mínimo ao soltar'],
        ['<code>on_resize</code>', 'string', '-', 'Callback JavaScript para redimensionamento'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>handle_class</code>', 'string', '-', 'Classes CSS para as barras de redimensionamento'],
    ]
}

# Dados consolidados do resizable
RESIZABLE_DATA = {
    'horizontal': resizable_horizontal,
    'vertical': resizable_vertical,
    'three_panels': resizable_three_panels,
    'nested': resizable_nested,
    'dynamic': resizable_dynamic,
    'params': resizable_params,
} 