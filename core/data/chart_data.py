# Dados do componente Chart

# Dados para gráfico de barras
chart_bar = {
    'data': [
        {'month': 'Jan', 'value': 45, 'color': 'bg-blue-500'},
        {'month': 'Fev', 'value': 52, 'color': 'bg-blue-500'},
        {'month': 'Mar', 'value': 38, 'color': 'bg-blue-500'},
        {'month': 'Abr', 'value': 61, 'color': 'bg-blue-500'},
        {'month': 'Mai', 'value': 73, 'color': 'bg-blue-500'},
        {'month': 'Jun', 'value': 69, 'color': 'bg-blue-500'},
        {'month': 'Jul', 'value': 82, 'color': 'bg-blue-500'},
        {'month': 'Ago', 'value': 78, 'color': 'bg-blue-500'},
        {'month': 'Set', 'value': 65, 'color': 'bg-blue-500'},
        {'month': 'Out', 'value': 71, 'color': 'bg-blue-500'},
        {'month': 'Nov', 'value': 85, 'color': 'bg-blue-500'},
        {'month': 'Dez', 'value': 92, 'color': 'bg-blue-500'}
    ],
    'title': 'Vendas Mensais',
    'subtitle': '2024'
}

# Dados para gráfico de pizza
chart_pie = {
    'segments': [
        {'label': 'Desktop', 'value': 45, 'color': 'bg-blue-500', 'description': '45% • 2.4K vendas'},
        {'label': 'Mobile', 'value': 35, 'color': 'bg-emerald-500', 'description': '35% • 1.9K vendas'},
        {'label': 'Tablet', 'value': 20, 'color': 'bg-amber-500', 'description': '20% • 1.1K vendas'}
    ],
    'title': 'Distribuição de Vendas',
    'subtitle': 'Q4 2024'
}

# Dados para gráfico de linha
chart_line = {
    'points': [
        {'x': 50, 'y': 200, 'label': 'Jan', 'value': '1K'},
        {'x': 110, 'y': 180, 'label': 'Fev', 'value': '1.2K'},
        {'x': 170, 'y': 150, 'label': 'Mar', 'value': '1.5K'},
        {'x': 230, 'y': 120, 'label': 'Abr', 'value': '1.8K'},
        {'x': 290, 'y': 100, 'label': 'Mai', 'value': '2.1K'},
        {'x': 350, 'y': 85, 'label': 'Jun', 'value': '2.3K'},
        {'x': 410, 'y': 70, 'label': 'Jul', 'value': '2.6K'},
        {'x': 470, 'y': 60, 'label': 'Ago', 'value': '2.8K'},
        {'x': 530, 'y': 45, 'label': 'Set', 'value': '3.2K'}
    ],
    'title': 'Crescimento de Usuários',
    'subtitle': 'Últimos 9 meses'
}

# Dados para cards de métricas
chart_metrics = [
    {
        'title': 'Vendas Totais',
        'value': 'R$ 12.345',
        'change': '+12%',
        'change_label': 'vs mês anterior',
        'icon': 'arrow-up',
        'icon_color': 'text-green-600 dark:text-green-400',
        'bg_color': 'bg-green-100 dark:bg-green-900'
    },
    {
        'title': 'Novos Usuários',
        'value': '1.234',
        'change': '+8%',
        'change_label': 'vs mês anterior',
        'icon': 'person',
        'icon_color': 'text-blue-600 dark:text-blue-400',
        'bg_color': 'bg-blue-100 dark:bg-blue-900'
    },
    {
        'title': 'Taxa de Conversão',
        'value': '3.24%',
        'change': '+2%',
        'change_label': 'vs mês anterior',
        'icon': 'target',
        'icon_color': 'text-purple-600 dark:text-purple-400',
        'bg_color': 'bg-purple-100 dark:bg-purple-900'
    },
    {
        'title': 'Receita Média',
        'value': 'R$ 156',
        'change': '-3%',
        'change_label': 'vs mês anterior',
        'icon': 'currency-dollar',
        'icon_color': 'text-amber-600 dark:text-amber-400',
        'bg_color': 'bg-amber-100 dark:bg-amber-900'
    }
]

# Parâmetros do chart
chart_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>type</code>', 'string', 'bar', 'Tipo do gráfico: bar, pie, line, metric'],
        ['<code>data</code>', 'array', '-', 'Dados do gráfico (obrigatório)'],
        ['<code>title</code>', 'string', '-', 'Título do gráfico'],
        ['<code>subtitle</code>', 'string', '-', 'Subtítulo ou período'],
        ['<code>height</code>', 'string', 'h-64', 'Altura do gráfico (classes Tailwind)'],
        ['<code>width</code>', 'string', 'w-full', 'Largura do gráfico (classes Tailwind)'],
        ['<code>colors</code>', 'array', '-', 'Array de cores personalizadas'],
        ['<code>animated</code>', 'boolean', 'true', 'Se deve ter animações'],
        ['<code>legend</code>', 'boolean', 'true', 'Se deve mostrar legenda'],
        ['<code>tooltip</code>', 'boolean', 'true', 'Se deve mostrar tooltips'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do chart
CHART_DATA = {
    'bar': chart_bar,
    'pie': chart_pie,
    'line': chart_line,
    'metrics': chart_metrics,
    'params': chart_params,
} 