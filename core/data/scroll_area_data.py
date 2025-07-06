# Dados do componente Scroll Area

# Scroll area básico (vertical)
scroll_area_basic = {
    'height': 'h-64',
    'content': '''
    <div class="space-y-4 p-4">
        <h3 class="text-lg font-semibold">Lista de Itens</h3>
        <div class="space-y-2">
            {%for i in "123456789012345678901234567890"|make_list %}
            <div class="p-3 bg-gray-50 dark:bg-gray-800 rounded-lg border">
                <h4 class="font-medium">Item {{ forloop.counter }}</h4>
                <p class="text-sm text-gray-600 dark:text-gray-400">
                    Descrição do item {{ forloop.counter }}. Este conteúdo pode ser muito longo 
                    e vai fazer com que a área precise ser rolada para ver todo o conteúdo.
                </p>
            </div>
            {%endfor %}
        </div>
    </div>
    '''
}

# Scroll area horizontal
scroll_area_horizontal = {
    'width': 'w-96',
    'direction': 'horizontal',
    'content': '''
    <div class="flex space-x-4 p-4" style="width: 800px;">
        {%for i in "123456789012"|make_list %}
        <div class="flex-shrink-0 w-48 p-4 bg-gradient-to-br from-blue-500 to-purple-600 text-white rounded-lg">
            <h4 class="font-semibold mb-2">Card {{ forloop.counter }}</h4>
            <p class="text-sm opacity-90">
                Este é um card largo que requer scroll horizontal para ser visualizado completamente.
            </p>
        </div>
        {%endfor %}
    </div>
    '''
}

# Scroll area com conteúdo misto
scroll_area_mixed = {
    'height': 'h-80',
    'content': '''
    <div class="p-4 space-y-6">
        <div>
            <h3 class="text-lg font-semibold mb-4">Mensagens Recentes</h3>
            <div class="space-y-3">
                <div class="flex space-x-3 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                        JS
                    </div>
                    <div class="flex-1 min-w-0">
                        <p class="font-medium">João Silva</p>
                        <p class="text-sm text-gray-600 dark:text-gray-400">
                            Olá! Como está o projeto? Podemos marcar uma reunião para revisar o progresso?
                        </p>
                        <p class="text-xs text-gray-500 mt-1">há 5 minutos</p>
                    </div>
                </div>
                
                <div class="flex space-x-3 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg">
                    <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                        AS
                    </div>
                    <div class="flex-1 min-w-0">
                        <p class="font-medium">Ana Santos</p>
                        <p class="text-sm text-gray-600 dark:text-gray-400">
                            Ótima ideia! Estou disponível amanhã às 14h. O que acham?
                        </p>
                        <p class="text-xs text-gray-500 mt-1">há 3 minutos</p>
                    </div>
                </div>
                
                <div class="flex space-x-3 p-3 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
                    <div class="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center text-white text-sm font-medium">
                        MF
                    </div>
                    <div class="flex-1 min-w-0">
                        <p class="font-medium">Maria Fernanda</p>
                        <p class="text-sm text-gray-600 dark:text-gray-400">
                            Perfeito! Vou criar o convite no calendário. Até amanhã!
                        </p>
                        <p class="text-xs text-gray-500 mt-1">há 1 minuto</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold mb-4">Notificações</h3>
            <div class="space-y-2">
                {%for i in "123456789012"|make_list %}
                <div class="flex items-center space-x-3 p-3 border border-gray-200 dark:border-gray-700 rounded-lg">
                    <div class="w-2 h-2 bg-blue-500 rounded-full"></div>
                    <div class="flex-1">
                        <p class="text-sm">Nova atualização no projeto {{ forloop.counter }}</p>
                        <p class="text-xs text-gray-500">há {{ forloop.counter }} hora{{ forloop.counter|pluralize }}</p>
                    </div>
                </div>
                {%endfor %}
            </div>
        </div>
        
        <div>
            <h3 class="text-lg font-semibold mb-4">Atividades</h3>
            <div class="space-y-3">
                {%for i in "12345"|make_list %}
                <div class="border-l-2 border-gray-300 dark:border-gray-600 pl-4 pb-4">
                    <div class="flex items-center space-x-2 mb-1">
                        <div class="w-2 h-2 bg-gray-400 rounded-full -ml-5 bg-white dark:bg-gray-900 border-2 border-gray-300 dark:border-gray-600"></div>
                        <p class="font-medium text-sm">Atividade {{ forloop.counter }}</p>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-400">
                        Descrição da atividade {{ forloop.counter }} que foi executada no sistema.
                    </p>
                    <p class="text-xs text-gray-500 mt-1">{{ forloop.counter }} horas atrás</p>
                </div>
                {%endfor %}
            </div>
        </div>
    </div>
    '''
}

# Scroll area com scroll personalizado
scroll_area_custom = {
    'height': 'h-64',
    'custom_scrollbar': True,
    'content': '''
    <div class="p-4">
        <h3 class="text-lg font-semibold mb-4">Código de Exemplo</h3>
        <div class="bg-gray-900 text-green-400 p-4 rounded font-mono text-sm">
            <div>import React from 'react';</div>
            <div>import { useState, useEffect } from 'react';</div>
            <div>&nbsp;</div>
            <div>&nbsp;&nbsp;function ScrollableComponent() {</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;const [data, setData] = useState([]);</div>
            <div>&nbsp;</div>
            <div>&nbsp;&nbsp;useEffect(() => {</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;// Buscar dados da API</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;fetchData().then(setData);</div>
            <div>&nbsp;&nbsp;}, []);</div>
            <div>&nbsp;</div>
            <div>&nbsp;&nbsp;return (</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&lt;div className="scroll-area"&gt;</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{data.map(item =&gt; (</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;div key={item.id}&gt;</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{item.name}</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;))}</div>
            <div>&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;</div>
            <div>&nbsp;&nbsp;);</div>
            <div>}</div>
            <div>&nbsp;</div>
            <div>export default ScrollableComponent;</div>
        </div>
    </div>
    '''
}

# Scroll area com tabela
scroll_area_table = {
    'height': 'h-80',
    'content': '''
    <div class="p-4">
        <h3 class="text-lg font-semibold mb-4">Relatório de Vendas</h3>
        <table class="w-full text-sm">
            <thead class="sticky top-0 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700">
                <tr>
                    <th class="text-left p-2">ID</th>
                    <th class="text-left p-2">Produto</th>
                    <th class="text-left p-2">Cliente</th>
                    <th class="text-left p-2">Data</th>
                    <th class="text-right p-2">Valor</th>
                </tr>
            </thead>
            <tbody>
                {%for i in "123456789012345678901234567890"|make_list %}
                <tr class="border-b border-gray-100 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800">
                    <td class="p-2">#{{ forloop.counter|stringformat:"04d" }}</td>
                    <td class="p-2">Produto {{ forloop.counter }}</td>
                    <td class="p-2">Cliente {{ forloop.counter }}</td>
                    <td class="p-2">15/01/2024</td>
                    <td class="p-2 text-right">R$ {{ forloop.counter }}99,90</td>
                </tr>
                {%endfor %}
            </tbody>
        </table>
    </div>
    '''
}

# Scroll area infinito (virtual)
scroll_area_infinite = {
    'height': 'h-96',
    'infinite': True,
    'content': '''
    <div class="p-4">
        <h3 class="text-lg font-semibold mb-4">Lista Infinita</h3>
        <div class="space-y-2" x-data="{ 
            items: Array.from({length: 50}, (_, i) => i + 1),
            loading: false,
            loadMore() {
                if (this.loading) return;
                this.loading = true;
                setTimeout(() => {
                    const start = this.items.length;
                    this.items.push(...Array.from({length: 20}, (_, i) => start + i + 1));
                    this.loading = false;
                }, 1000);
            }
        }" 
        @scroll.window="
            if ($el.scrollTop + $el.clientHeight >= $el.scrollHeight - 100) {
                loadMore();
            }
        ">
            <template x-for="item in items" :key="item">
                <div class="p-3 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg">
                    <div class="flex items-center justify-between">
                        <div>
                            <h4 class="font-medium" x-text="`Item ${item}`"></h4>
                            <p class="text-sm text-gray-600 dark:text-gray-400">
                                Este é o conteúdo do item. Scroll para carregar mais itens automaticamente.
                            </p>
                        </div>
                        <div class="text-xs text-gray-500" x-text="`#${item}`"></div>
                    </div>
                </div>
            </template>
            
            <div x-show="loading" class="text-center py-4">
                <div class="inline-flex items-center space-x-2">
                    <div class="animate-spin rounded-full h-4 w-4 border-b-2 border-blue-600"></div>
                    <span class="text-sm text-gray-600 dark:text-gray-400">Carregando mais itens...</span>
                </div>
            </div>
        </div>
    </div>
    '''
}

# Parâmetros do scroll area
scroll_area_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>height</code>', 'string', 'auto', 'Altura da área de scroll (classes CSS)'],
        ['<code>width</code>', 'string', 'auto', 'Largura da área de scroll (classes CSS)'],
        ['<code>max_height</code>', 'string', '-', 'Altura máxima (classes CSS)'],
        ['<code>direction</code>', 'string', 'vertical', 'Direção: vertical, horizontal, both'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo a ser exibido na área rolável'],
        ['<code>custom_scrollbar</code>', 'boolean', 'false', 'Se usa scrollbar personalizada'],
        ['<code>hide_scrollbar</code>', 'boolean', 'false', 'Se esconde a scrollbar'],
        ['<code>infinite</code>', 'boolean', 'false', 'Se ativa scroll infinito'],
        ['<code>load_more_threshold</code>', 'number', '100', 'Distância do fim para carregar mais (px)'],
        ['<code>on_scroll</code>', 'string', '-', 'Callback JavaScript para evento de scroll'],
        ['<code>on_reach_end</code>', 'string', '-', 'Callback quando atinge o fim'],
        ['<code>smooth_scroll</code>', 'boolean', 'true', 'Se usa scroll suave'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>scrollbar_class</code>', 'string', '-', 'Classes CSS para a scrollbar'],
    ]
}

# Dados consolidados do scroll area
SCROLL_AREA_DATA = {
    'basic': scroll_area_basic,
    'horizontal': scroll_area_horizontal,
    'mixed': scroll_area_mixed,
    'custom': scroll_area_custom,
    'table': scroll_area_table,
    'infinite': scroll_area_infinite,
    'params': scroll_area_params,
} 