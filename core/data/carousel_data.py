# Dados do componente Carousel

# Dados básicos do carousel
carousel_basic = {
    'items': [
        {
            'image': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=400&fit=crop',
            'title': 'Paisagem 1',
            'description': 'Uma bela vista montanhosa ao amanhecer'
        },
        {
            'image': 'https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800&h=400&fit=crop',
            'title': 'Paisagem 2', 
            'description': 'Floresta densa com névoa matinal'
        },
        {
            'image': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=400&fit=crop',
            'title': 'Paisagem 3',
            'description': 'Campo aberto sob céu estrelado'
        }
    ]
}

# Carousel com autoplay
carousel_autoplay = {
    'items': [
        {
            'image': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800&h=400&fit=crop',
            'title': 'Tecnologia',
            'description': 'Inovação em cada detalhe'
        },
        {
            'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=400&fit=crop',
            'title': 'Negócios',
            'description': 'Soluções para o seu crescimento'
        },
        {
            'image': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&h=400&fit=crop',
            'title': 'Criatividade',
            'description': 'Transformando ideias em realidade'
        }
    ]
}

# Carousel simples
carousel_simple = {
    'items': [
        {
            'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&h=400&fit=crop',
            'title': 'Produto 1',
            'description': 'Descrição do produto 1'
        },
        {
            'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=400&fit=crop',
            'title': 'Produto 2',
            'description': 'Descrição do produto 2'  
        }
    ]
}

# Parâmetros do carousel
carousel_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>items</code>', 'array', '-', 'Array de itens do carousel (obrigatório)'],
        ['<code>autoplay</code>', 'boolean', 'false', 'Se o carousel deve avançar automaticamente'],
        ['<code>controls</code>', 'boolean', 'true', 'Se deve mostrar botões de navegação'],
        ['<code>indicators</code>', 'boolean', 'true', 'Se deve mostrar indicadores de posição'],
        ['<code>interval</code>', 'number', '5000', 'Intervalo entre slides em autoplay (ms)'],
        ['<code>height</code>', 'string', 'h-64', 'Altura do carousel (classes Tailwind)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>transition</code>', 'string', 'slide', 'Tipo de transição: slide, fade'],
    ]
}

# Dados consolidados do carousel
CAROUSEL_DATA = {
    'basic': carousel_basic,
    'autoplay': carousel_autoplay,
    'simple': carousel_simple,
    'params': carousel_params,
} 