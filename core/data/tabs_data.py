"""
Dados específicos para o componente Tabs
"""

TABS_DATA = {
    'basic_tabs': [
        {'id': 'tab1', 'label': 'Overview', 'content': 'Conteúdo da aba Overview com informações gerais.'},
        {'id': 'tab2', 'label': 'Analytics', 'content': 'Dados analíticos e métricas importantes.'},
        {'id': 'tab3', 'label': 'Reports', 'content': 'Relatórios detalhados e estatísticas.'},
        {'id': 'tab4', 'label': 'Notifications', 'content': 'Central de notificações e alertas.'}
    ],
    'detailed_tabs': [
        {
            'id': 'profile',
            'label': 'Perfil',
            'content': '''
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold">Informações Pessoais</h3>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium mb-1">Nome</label>
                            <input type="text" value="João Silva" class="w-full px-3 py-2 border rounded">
                        </div>
                        <div>
                            <label class="block text-sm font-medium mb-1">Email</label>
                            <input type="email" value="joao@exemplo.com" class="w-full px-3 py-2 border rounded">
                        </div>
                    </div>
                </div>
            '''
        },
        {
            'id': 'security',
            'label': 'Segurança',
            'content': '''
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold">Configurações de Segurança</h3>
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span>Autenticação de dois fatores</span>
                            <button class="px-3 py-1 bg-green-500 text-white rounded text-sm">Ativada</button>
                        </div>
                        <div class="flex items-center justify-between">
                            <span>Sessões ativas</span>
                            <button class="px-3 py-1 bg-blue-500 text-white rounded text-sm">Gerenciar</button>
                        </div>
                    </div>
                </div>
            '''
        },
        {
            'id': 'preferences',
            'label': 'Preferências',
            'content': '''
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold">Preferências do Sistema</h3>
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span>Tema escuro</span>
                            <input type="checkbox" class="toggle">
                        </div>
                        <div class="flex items-center justify-between">
                            <span>Notificações por email</span>
                            <input type="checkbox" class="toggle" checked>
                        </div>
                    </div>
                </div>
            '''
        }
    ]
}

TABS_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>tabs</code>', 'array', '-', 'Lista de abas'],
        ['<code>tabs.id</code>', 'string', '-', 'ID único da aba'],
        ['<code>tabs.label</code>', 'string', '-', 'Título da aba'],
        ['<code>tabs.content</code>', 'HTML', '-', 'Conteúdo da aba'],
        ['<code>tabs.disabled</code>', 'boolean', 'false', 'Se a aba está desabilitada'],
        ['<code>default_tab</code>', 'string', '-', 'ID da aba ativa inicialmente'],
        ['<code>orientation</code>', 'string', 'horizontal', 'Orientação: horizontal, vertical'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
} 