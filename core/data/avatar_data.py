"""
Dados específicos para o componente Avatar
"""

AVATAR_EXAMPLES = [
    {
        'src': 'https://github.com/shadcn.png',
        'alt': 'shadcn',
        'fallback': 'CN'
    },
    {
        'src': 'https://github.com/vercel.png',
        'alt': 'Vercel',
        'fallback': 'VC'
    },
    {
        'src': 'https://github.com/nextjs.png',
        'alt': 'Next.js',
        'fallback': 'NX'
    },
]

AVATAR_PARAMS = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>src</code>', 'string', '-', 'URL da imagem'],
        ['<code>alt</code>', 'string', '-', 'Texto alternativo'],
        ['<code>fallback</code>', 'string', '-', 'Texto a ser exibido se a imagem não carregar'],
        ['<code>size</code>', 'string', 'md', 'Tamanho do avatar: sm, md, lg, xl'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

AVATAR_DATA = {
    'examples': AVATAR_EXAMPLES,
    'params': AVATAR_PARAMS
} 