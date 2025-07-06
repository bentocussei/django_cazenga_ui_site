# Dados do componente Sheet

# Sheet básico (lado)
sheet_basic = {
    'trigger_text': 'Abrir Sheet',
    'title': 'Configurações',
    'description': 'Ajuste suas preferências aqui.',
    'side': 'right',
    'content': '''
    <div class="space-y-6">
        <div class="space-y-2">
            <label class="text-sm font-medium">Nome de usuário</label>
            <input type="text" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Seu nome">
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Email</label>
            <input type="email" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="seu@email.com">
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Tema</label>
            <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                <option>Claro</option>
                <option>Escuro</option>
                <option>Automático</option>
            </select>
        </div>
        <div class="flex items-center space-x-2">
            <input type="checkbox" id="notifications" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
            <label for="notifications" class="text-sm">Receber notificações</label>
        </div>
    </div>
    ''',
    'footer': '''
    <div class="flex justify-between">
        <button class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-md">
            Cancelar
        </button>
        <button class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md">
            Salvar
        </button>
    </div>
    '''
}

# Sheet com formulário (esquerda)
sheet_form = {
    'trigger_text': 'Adicionar Produto',
    'title': 'Novo Produto',
    'description': 'Preencha os dados do produto.',
    'side': 'left',
    'size': 'lg',
    'content': '''
    <form class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-2">
                <label class="text-sm font-medium">Nome do Produto</label>
                <input type="text" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Ex: Tênis Esportivo">
            </div>
            <div class="space-y-2">
                <label class="text-sm font-medium">Categoria</label>
                <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                    <option>Selecione uma categoria</option>
                    <option>Calçados</option>
                    <option>Roupas</option>
                    <option>Acessórios</option>
                </select>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-2">
                <label class="text-sm font-medium">Preço</label>
                <div class="relative">
                    <span class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500">R$</span>
                    <input type="number" class="w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="0,00">
                </div>
            </div>
            <div class="space-y-2">
                <label class="text-sm font-medium">Estoque</label>
                <input type="number" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="0">
            </div>
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Descrição</label>
            <textarea rows="4" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Descrição detalhada do produto..."></textarea>
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Imagem</label>
            <div class="border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg p-8 text-center">
                <svg class="w-12 h-12 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                </svg>
                <p class="text-gray-500">Clique para adicionar uma imagem</p>
            </div>
        </div>
        <div class="flex items-center space-x-2">
            <input type="checkbox" id="featured" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
            <label for="featured" class="text-sm">Produto em destaque</label>
        </div>
    </form>
    ''',
    'footer': '''
    <div class="flex justify-between">
        <button class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-md">
            Cancelar
        </button>
        <button class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md">
            Criar Produto
        </button>
    </div>
    '''
}

# Sheet de detalhes (bottom)
sheet_details = {
    'trigger_text': 'Ver Detalhes',
    'title': 'Detalhes do Pedido #1234',
    'side': 'bottom',
    'content': '''
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="space-y-4">
            <h4 class="font-semibold text-lg">Informações do Pedido</h4>
            <div class="space-y-3">
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Número:</span>
                    <span class="font-medium">#1234</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Data:</span>
                    <span class="font-medium">15 de Janeiro, 2024</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Status:</span>
                    <span class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                        Entregue
                    </span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Total:</span>
                    <span class="font-semibold text-lg">R$ 299,90</span>
                </div>
            </div>
        </div>
        <div class="space-y-4">
            <h4 class="font-semibold text-lg">Dados do Cliente</h4>
            <div class="space-y-3">
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Nome:</span>
                    <span class="font-medium">Ana Silva</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Email:</span>
                    <span class="font-medium">ana@exemplo.com</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Telefone:</span>
                    <span class="font-medium">(11) 99999-9999</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-gray-600 dark:text-gray-400">Cidade:</span>
                    <span class="font-medium">São Paulo, SP</span>
                </div>
            </div>
        </div>
    </div>
    <div class="mt-6 space-y-4">
        <h4 class="font-semibold text-lg">Itens do Pedido</h4>
        <div class="space-y-3">
            <div class="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-800 rounded-lg">
                <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-gray-200 dark:bg-gray-700 rounded-lg"></div>
                    <div>
                        <p class="font-medium">Tênis Esportivo</p>
                        <p class="text-sm text-gray-500">Tamanho: 42</p>
                    </div>
                </div>
                <div class="text-right">
                    <p class="font-medium">R$ 299,90</p>
                    <p class="text-sm text-gray-500">Qtd: 1</p>
                </div>
            </div>
        </div>
    </div>
    ''',
    'footer': '''
    <div class="flex justify-between">
        <button class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-md">
            Imprimir
        </button>
        <div class="space-x-2">
            <button class="px-4 py-2 text-sm font-medium text-blue-600 bg-blue-100 hover:bg-blue-200 rounded-md">
                Reenviar
            </button>
            <button class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md">
                Editar
            </button>
        </div>
    </div>
    '''
}

# Sheet de filtros (top)
sheet_filters = {
    'trigger_text': 'Filtros',
    'title': 'Filtrar Resultados',
    'side': 'top',
    'content': '''
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div class="space-y-2">
            <label class="text-sm font-medium">Categoria</label>
            <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                <option>Todas</option>
                <option>Eletrônicos</option>
                <option>Roupas</option>
                <option>Casa</option>
            </select>
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Preço</label>
            <div class="flex space-x-2">
                <input type="number" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Min">
                <input type="number" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700" placeholder="Max">
            </div>
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Marca</label>
            <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                <option>Todas</option>
                <option>Samsung</option>
                <option>Apple</option>
                <option>Sony</option>
            </select>
        </div>
        <div class="space-y-2">
            <label class="text-sm font-medium">Avaliação</label>
            <select class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700">
                <option>Todas</option>
                <option>5 estrelas</option>
                <option>4+ estrelas</option>
                <option>3+ estrelas</option>
            </select>
        </div>
    </div>
    <div class="mt-4 space-y-3">
        <div class="flex items-center space-x-2">
            <input type="checkbox" id="inStock" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
            <label for="inStock" class="text-sm">Apenas produtos em estoque</label>
        </div>
        <div class="flex items-center space-x-2">
            <input type="checkbox" id="onSale" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
            <label for="onSale" class="text-sm">Apenas produtos em promoção</label>
        </div>
    </div>
    ''',
    'footer': '''
    <div class="flex justify-between">
        <button class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-md">
            Limpar Filtros
        </button>
        <button class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-md">
            Aplicar Filtros
        </button>
    </div>
    '''
}

# Parâmetros do sheet
sheet_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', 'Abrir Sheet', 'Texto do botão que abre o sheet'],
        ['<code>title</code>', 'string', '-', 'Título do sheet'],
        ['<code>description</code>', 'string', '-', 'Descrição/subtítulo do sheet'],
        ['<code>side</code>', 'string', 'right', 'Lado de origem: top, right, bottom, left'],
        ['<code>size</code>', 'string', 'md', 'Tamanho: sm, md, lg, xl, full'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo principal do sheet'],
        ['<code>footer</code>', 'HTML', '-', 'Conteúdo do footer com botões'],
        ['<code>closable</code>', 'boolean', 'true', 'Se pode ser fechado com X ou ESC'],
        ['<code>backdrop_close</code>', 'boolean', 'true', 'Se fecha ao clicar no fundo'],
        ['<code>persistent</code>', 'boolean', 'false', 'Se o sheet não fecha automaticamente'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do sheet
SHEET_DATA = {
    'basic': sheet_basic,
    'form': sheet_form,
    'details': sheet_details,
    'filters': sheet_filters,
    'params': sheet_params,
} 