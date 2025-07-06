"""
Dados específicos para o componente Aspect Ratio
"""

ASPECT_RATIO_DATA = {
    'common_ratios': [
        {'ratio': '16:9', 'description': 'Padrão widescreen', 'percentage': '56.25%', 'usage': 'Vídeos HD, monitores'},
        {'ratio': '4:3', 'description': 'Padrão tradicional', 'percentage': '75%', 'usage': 'Monitores antigos, fotos'},
        {'ratio': '1:1', 'description': 'Quadrado', 'percentage': '100%', 'usage': 'Instagram, avatares'},
        {'ratio': '3:2', 'description': 'Fotografia clássica', 'percentage': '66.67%', 'usage': 'Câmeras, impressão'},
        {'ratio': '21:9', 'description': 'Ultra-widescreen', 'percentage': '42.86%', 'usage': 'Cinema, ultrawide'},
        {'ratio': '9:16', 'description': 'Vertical (Stories)', 'percentage': '177.78%', 'usage': 'Instagram Stories, TikTok'},
    ],
    # Imagens de alta qualidade com fallbacks
    'sample_images': [
        'https://picsum.photos/800/600?random=1',
        'https://picsum.photos/800/600?random=2', 
        'https://picsum.photos/800/600?random=3',
        'https://picsum.photos/800/600?random=4',
    ],
    'sample_videos': [
        {'title': 'Apresentação do Produto', 'id': 'video1'},
        {'title': 'Tutorial de Uso', 'id': 'video2'},
        {'title': 'Depoimentos', 'id': 'video3'},
        {'title': 'Demo Interativa', 'id': 'video4'}
    ],
    # Exemplo básico funcional
    'basic_example': {
        'ratio': '16:9',
        'content': '<img src="https://picsum.photos/800/450?random=10" alt="Paisagem" class="w-full h-full object-cover rounded" onerror="this.src=\'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODAiIGhlaWdodD0iNDUiIHZpZXdCb3g9IjAgMCA4MCA0NSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjgwIiBoZWlnaHQ9IjQ1IiBmaWxsPSIjRjFGNUY5Ii8+CjxwYXRoIGQ9Ik0yNSAyMUwyOSAyNUwzNSAxOUw0NSAyOUg1NVYzN0gxNVYyMUgyNVoiIGZpbGw9IiM5Q0EzQUYiLz4KPC9zdmc+Cg==\'">'
    }
}

# URLs mais confiáveis para imagens
ASPECT_RATIO_SAMPLE_IMAGES = [
    "https://picsum.photos/800/600?random=1",
    "https://picsum.photos/800/600?random=2",
    "https://picsum.photos/800/600?random=3",
    "https://picsum.photos/800/600?random=4"
]

ASPECT_RATIO_SAMPLE_VIDEOS = [
    {"title": "Apresentação do Produto", "id": "video1"},
    {"title": "Tutorial de Uso", "id": "video2"},
    {"title": "Depoimentos", "id": "video3"},
    {"title": "Demo Interativa", "id": "video4"}
]

ASPECT_RATIO_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>ratio</code>', 'string', '16:9', 'Proporção desejada (largura:altura)'],
        ['<code>content</code>', 'HTML', '-', 'Conteúdo interno (imagem, vídeo, etc.)'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais para o container'],
        ['<code>content_class</code>', 'string', '-', 'Classes CSS adicionais para o conteúdo'],
    ]
} 