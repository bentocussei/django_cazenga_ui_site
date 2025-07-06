# Dados do componente Layout

# Layout com sidebar esquerda
layout_sidebar_left = {
    'layout_type': 'sidebar-left',
    'sidebar_content': '''
    <nav class="space-y-1">
        <a href="#" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium bg-accent text-accent-foreground">
            Dashboard
        </a>
        <a href="#" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium hover:bg-accent transition-colors">
            Usuários
        </a>
        <a href="#" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium hover:bg-accent transition-colors">
            Relatórios
        </a>
        <a href="#" class="flex items-center gap-3 rounded-radius-md px-3 py-2 text-sm font-medium hover:bg-accent transition-colors">
            Configurações
        </a>
    </nav>
    ''',
    'header_content': '''
    <div class="flex items-center gap-4">
        <h1 class="text-xl font-bold">Dashboard</h1>
    </div>
    <div class="flex items-center gap-4">
        <button class="size-8 rounded-radius-md hover:bg-accent transition-colors flex items-center justify-center">
            <svg class="size-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-5 5M4 19l5-5M13 7h5l-5-5M4 5l5 5"/>
            </svg>
        </button>
        <div class="size-8 rounded-radius-full bg-primary text-primary-foreground flex items-center justify-center text-sm font-medium">
            U
        </div>
    </div>
    ''',
    'main_content': '''
    <div class="space-y-6">
        <h2 class="text-2xl font-bold">Bem-vindo ao Dashboard</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg border">
                <h3 class="text-lg font-semibold mb-2">Vendas</h3>
                <p class="text-3xl font-bold text-green-600">R$ 12.345</p>
                <p class="text-sm text-gray-500">+12% este mês</p>
            </div>
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg border">
                <h3 class="text-lg font-semibold mb-2">Usuários</h3>
                <p class="text-3xl font-bold text-blue-600">1.234</p>
                <p class="text-sm text-gray-500">+8% este mês</p>
            </div>
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg border">
                <h3 class="text-lg font-semibold mb-2">Pedidos</h3>
                <p class="text-3xl font-bold text-purple-600">456</p>
                <p class="text-sm text-gray-500">+15% este mês</p>
            </div>
            <div class="bg-white dark:bg-gray-800 p-6 rounded-lg border">
                <h3 class="text-lg font-semibold mb-2">Produtos</h3>
                <p class="text-3xl font-bold text-orange-600">89</p>
                <p class="text-sm text-gray-500">+3% este mês</p>
            </div>
        </div>
    </div>
    '''
}

# Layout com sidebar direita
layout_sidebar_right = {
    'layout_type': 'sidebar-right',
    'sidebar_content': '''
    <div class="space-y-4">
        <h4 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
            Atividade Recente
        </h4>
        <div class="space-y-3">
            <div class="flex items-start space-x-3">
                <div class="w-2 h-2 bg-green-500 rounded-full mt-2"></div>
                <div>
                    <p class="text-sm font-medium">Novo usuário registrado</p>
                    <p class="text-xs text-gray-500">Ana Silva - há 2 min</p>
                </div>
            </div>
            <div class="flex items-start space-x-3">
                <div class="w-2 h-2 bg-blue-500 rounded-full mt-2"></div>
                <div>
                    <p class="text-sm font-medium">Pedido #1234 criado</p>
                    <p class="text-xs text-gray-500">João Santos - há 5 min</p>
                </div>
            </div>
            <div class="flex items-start space-x-3">
                <div class="w-2 h-2 bg-purple-500 rounded-full mt-2"></div>
                <div>
                    <p class="text-sm font-medium">Relatório gerado</p>
                    <p class="text-xs text-gray-500">Sistema - há 10 min</p>
                </div>
            </div>
        </div>
    </div>
    ''',
    'main_content': '''
    <div class="space-y-6">
        <h2 class="text-2xl font-bold">Conteúdo Principal</h2>
        <p class="text-gray-600 dark:text-gray-400">Este layout tem a sidebar posicionada à direita.</p>
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg border">
            <h3 class="text-lg font-semibold mb-4">Gráfico de Vendas</h3>
            <div class="h-64 bg-gray-100 dark:bg-gray-700 rounded flex items-center justify-center">
                <p class="text-gray-500">Gráfico seria exibido aqui</p>
            </div>
        </div>
    </div>
    '''
}

# Layout apenas com header
layout_header_only = {
    'layout_type': 'header-only',
    'header_content': '''
    <div class="flex items-center gap-4">
        <h1 class="text-xl font-bold">Aplicação</h1>
        <nav class="hidden md:flex space-x-4">
            <a href="#" class="text-sm font-medium hover:text-primary transition-colors">Início</a>
            <a href="#" class="text-sm font-medium text-primary">Produtos</a>
            <a href="#" class="text-sm font-medium hover:text-primary transition-colors">Sobre</a>
        </nav>
    </div>
    <div class="flex items-center gap-4">
        <button class="text-sm font-medium hover:text-primary transition-colors">Login</button>
        <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
            Registrar
        </button>
    </div>
    ''',
    'main_content': '''
    <div class="max-w-4xl mx-auto space-y-8">
        <div class="text-center py-16">
            <h1 class="text-4xl font-bold mb-4">Layout com Header Apenas</h1>
            <p class="text-xl text-gray-600 dark:text-gray-400 mb-8">Interface limpa com apenas o header superior</p>
            <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-11 px-8">
                Começar
            </button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="text-center p-6">
                <div class="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center mx-auto mb-4">
                    <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                    </svg>
                </div>
                <h3 class="text-lg font-semibold mb-2">Rápido</h3>
                <p class="text-sm text-gray-600 dark:text-gray-400">Performance otimizada</p>
            </div>
            <div class="text-center p-6">
                <div class="w-12 h-12 bg-green-100 dark:bg-green-900 rounded-lg flex items-center justify-center mx-auto mb-4">
                    <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                </div>
                <h3 class="text-lg font-semibold mb-2">Confiável</h3>
                <p class="text-sm text-gray-600 dark:text-gray-400">Alta disponibilidade</p>
            </div>
            <div class="text-center p-6">
                <div class="w-12 h-12 bg-purple-100 dark:bg-purple-900 rounded-lg flex items-center justify-center mx-auto mb-4">
                    <svg class="w-6 h-6 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                    </svg>
                </div>
                <h3 class="text-lg font-semibold mb-2">Seguro</h3>
                <p class="text-sm text-gray-600 dark:text-gray-400">Proteção de dados</p>
            </div>
        </div>
    </div>
    '''
}

# Layout full (sem sidebar nem header)
layout_full = {
    'layout_type': 'full',
    'main_content': '''
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-purple-100 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center">
        <div class="max-w-md w-full bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
            <div class="text-center mb-8">
                <h1 class="text-2xl font-bold mb-2">Layout Full</h1>
                <p class="text-gray-600 dark:text-gray-400">Interface sem header nem sidebar</p>
            </div>
            <form class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-2">Email</label>
                    <input type="email" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="seu@email.com">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2">Senha</label>
                    <input type="password" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="••••••••">
                </div>
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors">
                    Entrar
                </button>
            </form>
        </div>
    </div>
    '''
}

# Parâmetros do layout (baseado no existente no views.py mas melhorado)
layout_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>layout_type</code>', 'string', 'sidebar-left', 'Tipo de layout: sidebar-left, sidebar-right, header-only, sidebar-only, full'],
        ['<code>sidebar_collapsible</code>', 'boolean', 'true', 'Se a sidebar pode ser recolhida'],
        ['<code>sidebar_width</code>', 'string', 'w-64', 'Largura da sidebar (classes Tailwind)'],
        ['<code>sidebar_collapsed_width</code>', 'string', 'w-16', 'Largura da sidebar quando recolhida'],
        ['<code>header_height</code>', 'string', 'h-16', 'Altura do header (classes Tailwind)'],
        ['<code>footer_height</code>', 'string', 'h-16', 'Altura do footer (classes Tailwind)'],
        ['<code>sidebar_content</code>', 'HTML', '-', 'Conteúdo personalizado da sidebar'],
        ['<code>header_content</code>', 'HTML', '-', 'Conteúdo personalizado do header'],
        ['<code>main_content</code>', 'HTML', '-', 'Conteúdo principal da página'],
        ['<code>footer_content</code>', 'HTML', '-', 'Conteúdo personalizado do footer'],
        ['<code>sidebar_class</code>', 'string', '-', 'Classes CSS adicionais para a sidebar'],
        ['<code>header_class</code>', 'string', '-', 'Classes CSS adicionais para o header'],
        ['<code>main_class</code>', 'string', '-', 'Classes CSS adicionais para o main'],
        ['<code>footer_class</code>', 'string', '-', 'Classes CSS adicionais para o footer'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais para o container principal'],
        ['<code>spa_enabled</code>', 'boolean', 'true', 'Ativar funcionalidades SPA'],
    ]
}

# Dados consolidados do layout
LAYOUT_DATA = {
    'sidebar_left': layout_sidebar_left,
    'sidebar_right': layout_sidebar_right,
    'header_only': layout_header_only,
    'full': layout_full,
    'params': layout_params,
} 