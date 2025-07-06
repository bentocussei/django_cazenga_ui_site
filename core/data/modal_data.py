# Dados do componente Modal

# Modal básico
modal_basic = {
    'trigger_text': 'Abrir Modal',
    'title': 'Modal Básico',
    'content': '''
    <p class="text-gray-600 dark:text-gray-400">
        Este é um exemplo de modal básico. Os modais são úteis para exibir conteúdo 
        importante que requer atenção do usuário sem navegar para uma nova página.
    </p>
    <p class="text-gray-600 dark:text-gray-400 mt-4">
        Você pode incluir qualquer conteúdo HTML aqui, como formulários, 
        imagens, vídeos ou outros componentes.
    </p>
    ''',
    'footer': '''
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 mr-3">
        Cancelar
    </button>
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Confirmar
    </button>
    '''
}

# Modal de confirmação
modal_confirmation = {
    'trigger_text': 'Excluir Item',
    'trigger_variant': 'destructive',
    'title': 'Confirmar Exclusão',
    'icon': 'exclamation-triangle',
    'icon_color': 'text-red-500',
    'content': '''
    <p class="text-gray-600 dark:text-gray-400">
        Tem certeza de que deseja excluir este item? Esta ação não pode ser desfeita.
    </p>
    <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-4 mt-4">
        <div class="flex">
            <svg class="w-5 h-5 text-red-400 mr-3 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.732 15.5c-.77.833.192 2.5 1.732 2.5z"/>
            </svg>
            <div>
                <h4 class="text-sm font-medium text-red-800 dark:text-red-200">Atenção</h4>
                <p class="text-sm text-red-700 dark:text-red-300 mt-1">
                    Todos os dados relacionados também serão removidos permanentemente.
                </p>
            </div>
        </div>
    </div>
    ''',
    'footer': '''
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 mr-3">
        Cancelar
    </button>
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-red-600 text-white hover:bg-red-700 h-9 px-4 py-2">
        Excluir
    </button>
    '''
}

# Modal com formulário
modal_form = {
    'trigger_text': 'Novo Usuário',
    'title': 'Adicionar Usuário',
    'size': 'lg',
    'content': '''
    <form class="space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium mb-2">Nome</label>
                <input type="text" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="João Silva">
            </div>
            <div>
                <label class="block text-sm font-medium mb-2">Email</label>
                <input type="email" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="joao@exemplo.com">
            </div>
        </div>
        <div>
            <label class="block text-sm font-medium mb-2">Cargo</label>
            <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                <option>Selecione um cargo</option>
                <option>Desenvolvedor</option>
                <option>Designer</option>
                <option>Gerente</option>
                <option>Analista</option>
            </select>
        </div>
        <div>
            <label class="block text-sm font-medium mb-2">Biografia</label>
            <textarea rows="3" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Breve descrição sobre o usuário..."></textarea>
        </div>
        <div class="flex items-center">
            <input type="checkbox" id="admin" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
            <label for="admin" class="ml-2 text-sm text-gray-600 dark:text-gray-400">
                Conceder privilégios de administrador
            </label>
        </div>
    </form>
    ''',
    'footer': '''
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 mr-3">
        Cancelar
    </button>
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Adicionar Usuário
    </button>
    '''
}

# Modal de informação
modal_info = {
    'trigger_text': 'Ver Detalhes',
    'trigger_variant': 'outline',
    'title': 'Informações do Produto',
    'icon': 'info-circled',
    'icon_color': 'text-blue-500',
    'content': '''
    <div class="space-y-4">
        <div class="flex items-start space-x-4">
            <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=120&h=120&fit=crop" 
                 alt="Produto" class="w-20 h-20 rounded-lg object-cover">
            <div class="flex-1">
                <h4 class="font-semibold text-lg">Tênis Esportivo Premium</h4>
                <p class="text-gray-500 text-sm">SKU: #TEN-001</p>
                <p class="text-green-600 font-semibold text-xl mt-2">R$ 299,90</p>
            </div>
        </div>
        
        <div class="grid grid-cols-2 gap-4 text-sm">
            <div>
                <span class="font-medium text-gray-700 dark:text-gray-300">Categoria:</span>
                <span class="text-gray-600 dark:text-gray-400 ml-2">Calçados</span>
            </div>
            <div>
                <span class="font-medium text-gray-700 dark:text-gray-300">Marca:</span>
                <span class="text-gray-600 dark:text-gray-400 ml-2">SportMax</span>
            </div>
            <div>
                <span class="font-medium text-gray-700 dark:text-gray-300">Estoque:</span>
                <span class="text-gray-600 dark:text-gray-400 ml-2">25 unidades</span>
            </div>
            <div>
                <span class="font-medium text-gray-700 dark:text-gray-300">Status:</span>
                <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800 ml-2">
                    Disponível
                </span>
            </div>
        </div>
        
        <div>
            <h5 class="font-medium text-gray-700 dark:text-gray-300 mb-2">Descrição:</h5>
            <p class="text-gray-600 dark:text-gray-400 text-sm">
                Tênis esportivo de alta qualidade, desenvolvido com tecnologia avançada 
                para proporcionar máximo conforto e performance durante atividades físicas.
            </p>
        </div>
    </div>
    ''',
    'footer': '''
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 mr-3">
        Fechar
    </button>
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Editar Produto
    </button>
    '''
}

# Modal fullscreen
modal_fullscreen = {
    'trigger_text': 'Modo Fullscreen',
    'title': 'Editor Fullscreen',
    'size': 'fullscreen',
    'content': '''
    <div class="h-full flex flex-col">
        <div class="flex-1 bg-gray-50 dark:bg-gray-900 rounded-lg p-4">
            <div class="h-full border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg flex items-center justify-center">
                <div class="text-center">
                    <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                    </svg>
                    <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">Área de Edição</h3>
                    <p class="text-gray-500 dark:text-gray-400">
                        Este é um modal em modo fullscreen, ideal para editores, 
                        visualizadores de imagens ou qualquer conteúdo que precise 
                        de mais espaço na tela.
                    </p>
                </div>
            </div>
        </div>
    </div>
    ''',
    'footer': '''
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium border border-input bg-background hover:bg-accent hover:text-accent-foreground h-9 px-4 py-2 mr-3">
        Cancelar
    </button>
    <button class="inline-flex items-center justify-center rounded-radius-md text-sm font-medium bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2">
        Salvar
    </button>
    '''
}

# Parâmetros do modal
modal_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', 'Abrir Modal', 'Texto do botão que abre o modal'],
        ['<code>trigger_variant</code>', 'string', 'default', 'Variante do botão: default, primary, destructive, outline'],
        ['<code>title</code>', 'string', '-', 'Título do modal'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo principal do modal'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer com botões'],
        ['<code>icon</code>', 'string', '-', 'Ícone no header (opcional)'],
        ['<code>icon_color</code>', 'string', '-', 'Cor do ícone (classes CSS)'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, fullscreen'],
        ['<code>closable</code>', 'boolean', 'true', 'Se pode ser fechado com X ou ESC'],
        ['<code>backdrop_close</code>', 'boolean', 'true', 'Se fecha ao clicar no fundo'],
        ['<code>animation</code>', 'boolean', 'true', 'Se deve ter animação'],
        ['<code>persistent</code>', 'boolean', 'false', 'Se o modal não fecha automaticamente'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do modal
MODAL_DATA = {
    'basic': modal_basic,
    'confirmation': modal_confirmation,
    'form': modal_form,
    'info': modal_info,
    'fullscreen': modal_fullscreen,
    'params': modal_params,
} 