# Dados do componente Hover Card

# Hover card básico
hover_card_basic = {
    'trigger_text': 'Passe o mouse aqui',
    'title': 'Hover Card',
    'subtitle': '@hovercard',
    'description': 'Este é um exemplo de hover card. Ele aparece quando você passa o mouse sobre um elemento específico.',
    'avatar': '/static/images/avatar-example.jpg',
    'stats': [
        {'label': 'seguidores', 'value': '1.2K', 'icon': 'person'},
        {'label': 'likes', 'value': '348', 'icon': 'heart'}
    ]
}

# Hover card de perfil de usuário
hover_card_user = {
    'trigger_text': 'Ana Silva',
    'trigger_link': True,
    'title': 'Ana Silva',
    'subtitle': '@ana.silva',
    'description': 'Desenvolvedora Full-Stack especializada em React e Django. Apaixonada por criar experiências de usuário incríveis.',
    'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=80&h=80&fit=crop&crop=face',
    'verified': True,
    'stats': [
        {'label': 'seguidores', 'value': '2.1K', 'icon': 'person'},
        {'label': 'seguindo', 'value': '180', 'icon': 'person'},
        {'label': 'repositórios', 'value': '47', 'icon': 'github-logo'}
    ],
    'actions': [
        {'label': 'Seguir', 'variant': 'primary'},
        {'label': 'Mensagem', 'variant': 'outline'}
    ]
}

# Hover card de produto
hover_card_product = {
    'trigger_text': 'MacBook Pro',
    'trigger_link': True,
    'title': 'MacBook Pro 14"',
    'subtitle': 'Apple M3 Pro',
    'description': 'Desempenho excepcional para profissionais criativos. Chip M3 Pro, tela Liquid Retina XDR de 14 polegadas.',
    'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=200&h=150&fit=crop',
    'price': 'R$ 18.999,00',
    'rating': 4.8,
    'reviews_count': 124,
    'features': [
        'Chip Apple M3 Pro',
        '18GB RAM unificada',
        '512GB SSD',
        'Tela Liquid Retina XDR'
    ]
}

# Hover card de local
hover_card_location = {
    'trigger_text': 'São Paulo, Brasil',
    'trigger_link': True,
    'title': 'São Paulo',
    'subtitle': 'Brasil',
    'description': 'A maior cidade do Brasil e principal centro financeiro, corporativo e mercantil da América do Sul.',
    'image': 'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=200&h=120&fit=crop',
    'stats': [
        {'label': 'População', 'value': '12.3M', 'icon': 'person'},
        {'label': 'Área', 'value': '1.521 km²', 'icon': 'globe'},
        {'label': 'Timezone', 'value': 'UTC-3', 'icon': 'clock'}
    ]
}

# Parâmetros do hover card
hover_card_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>trigger_text</code>', 'string', '-', 'Texto do elemento trigger (obrigatório)'],
        ['<code>trigger_link</code>', 'boolean', 'false', 'Se o trigger deve parecer um link'],
        ['<code>title</code>', 'string', '-', 'Título principal do card'],
        ['<code>subtitle</code>', 'string', '-', 'Subtítulo ou descrição secundária'],
        ['<code>description</code>', 'string', '-', 'Descrição principal do conteúdo'],
        ['<code>avatar</code>', 'string', '-', 'URL do avatar/imagem circular'],
        ['<code>image</code>', 'string', '-', 'URL da imagem principal'],
        ['<code>stats</code>', 'array', '-', 'Array de estatísticas {label, value, icon}'],
        ['<code>actions</code>', 'array', '-', 'Array de botões de ação'],
        ['<code>delay</code>', 'number', '500', 'Delay para aparecer/desaparecer (ms)'],
        ['<code>position</code>', 'string', 'top', 'Posição: top, bottom, left, right'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do hover card
HOVER_CARD_DATA = {
    'basic': hover_card_basic,
    'user': hover_card_user,
    'product': hover_card_product,
    'location': hover_card_location,
    'params': hover_card_params,
} 