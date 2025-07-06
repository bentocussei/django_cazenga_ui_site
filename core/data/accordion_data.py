"""
Dados específicos para o componente Accordion
"""

ACCORDION_ITEMS = [
    {
        'id': 'item-1',
        'title': 'O que é um componente?',
        'content': 'Um componente é uma parte reutilizável de interface que pode ser configurada através de parâmetros. Ele encapsula funcionalidades e estilos específicos.'
    },
    {
        'id': 'item-2',
        'title': 'Como personalizar estilos?',
        'content': 'Você pode personalizar estilos utilizando as classes CSS do Tailwind CSS ou definindo suas próprias classes customizadas através do parâmetro class.'
    },
    {
        'id': 'item-3',
        'title': 'Posso usar Alpine.js?',
        'content': 'Sim! Todos os componentes são compatíveis com Alpine.js. Você pode adicionar reatividade e interatividade usando as diretivas x-data, x-show, x-model, etc.'
    },
]

ACCORDION_DATA = {
    'basic_items': [
        {
            'title': 'O que é React?',
            'content': 'React é uma biblioteca JavaScript para construção de interfaces de usuário, especialmente para aplicações web de página única onde você precisa de uma experiência de usuário rápida e interativa.'
        },
        {
            'title': 'Como instalar o React?',
            'content': 'Você pode instalar o React usando npm ou yarn. O comando mais comum é: <code>npx create-react-app meu-app</code> para criar um novo projeto React.'
        },
        {
            'title': 'Quais são os principais conceitos?',
            'content': 'Os principais conceitos do React incluem: Components, JSX, Props, State, Hooks, Virtual DOM, e Context. Cada um desses conceitos é fundamental para entender como o React funciona.'
        }
    ],
    'advanced_items': [
        {
            'title': 'Configurações de Conta',
            'content': '<div class="space-y-4"><p>Gerencie suas configurações de conta:</p><ul class="list-disc pl-6"><li>Alterar senha</li><li>Configurações de privacidade</li><li>Notificações</li><li>Preferências de idioma</li></ul></div>'
        },
        {
            'title': 'Configurações de Pagamento',
            'content': '<div class="space-y-4"><p>Métodos de pagamento aceitos:</p><div class="grid grid-cols-2 gap-4"><div class="p-3 border rounded">💳 Cartão de Crédito</div><div class="p-3 border rounded">🏦 PIX</div></div></div>'
        },
        {
            'title': 'Suporte Técnico',
            'content': '<div class="space-y-4"><p>Precisa de ajuda? Entre em contato:</p><div class="flex gap-4"><button class="px-4 py-2 bg-blue-500 text-white rounded">Chat ao Vivo</button><button class="px-4 py-2 border rounded">Email</button></div></div>'
        }
    ]
}

ACCORDION_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Lista de itens do accordion'],
        ['<code>items.title</code>', 'string', '-', 'Título do item'],
        ['<code>items.content</code>', 'HTML', '-', 'Conteúdo do item'],
        ['<code>items.open</code>', 'boolean', 'false', 'Se o item inicia aberto'],
        ['<code>multiple</code>', 'boolean', 'false', 'Permite múltiplos itens abertos'],
        ['<code>collapsible</code>', 'boolean', 'true', 'Permite fechar item aberto'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
} 