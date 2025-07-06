# Dados do componente Content Manager

# Content manager básico para blog posts
content_manager_blog = {
    'title': 'Nova Postagem do Blog',
    'content_type': 'blog_post',
    'fields': {
        'title': {
            'type': 'text',
            'label': 'Título da Postagem',
            'placeholder': 'Digite o título da sua postagem...',
            'required': True,
            'value': 'Como Criar Conteúdo Engajante'
        },
        'slug': {
            'type': 'text',
            'label': 'URL (Slug)',
            'placeholder': 'como-criar-conteudo-engajante',
            'help': 'URL amigável gerada automaticamente',
            'value': 'como-criar-conteudo-engajante'
        },
        'excerpt': {
            'type': 'textarea',
            'label': 'Resumo',
            'placeholder': 'Breve descrição da postagem...',
            'max_length': 160,
            'value': 'Descubra as melhores práticas para criar conteúdo que realmente engaja sua audiência.'
        },
        'content': {
            'type': 'rich_text',
            'label': 'Conteúdo Principal',
            'toolbar': ['bold', 'italic', 'underline', 'heading1', 'heading2', 'heading3', 'bulletList', 'orderedList', 'link', 'image', 'blockquote', 'codeBlock'],
            'value': '''
            <h1>Como Criar Conteúdo Engajante</h1>
            <p>Criar conteúdo que realmente conecta com sua audiência é uma arte que combina estratégia, criatividade e conhecimento do seu público.</p>
            
            <h2>1. Conheça Sua Audiência</h2>
            <p>Antes de escrever qualquer coisa, você precisa entender profundamente quem são as pessoas que vão consumir seu conteúdo.</p>
            
            <h2>2. Use Storytelling</h2>
            <p>Histórias são uma forma poderosa de conectar emocionalmente com as pessoas.</p>
            
            <blockquote>
                <p>"As pessoas não compram produtos, elas compram histórias." - Seth Godin</p>
            </blockquote>
            '''
        },
        'featured_image': {
            'type': 'image',
            'label': 'Imagem de Destaque',
            'accept': 'image/*',
            'help': 'Imagem principal que aparecerá no topo da postagem',
            'value': 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=800&h=400&fit=crop'
        },
        'category': {
            'type': 'select',
            'label': 'Categoria',
            'options': [
                {'value': 'marketing', 'label': 'Marketing'},
                {'value': 'tecnologia', 'label': 'Tecnologia'},
                {'value': 'negocios', 'label': 'Negócios'},
                {'value': 'design', 'label': 'Design'}
            ],
            'value': 'marketing'
        },
        'tags': {
            'type': 'tags',
            'label': 'Tags',
            'placeholder': 'Digite uma tag e pressione Enter',
            'value': ['conteúdo', 'marketing', 'engajamento', 'audiência']
        },
        'status': {
            'type': 'select',
            'label': 'Status',
            'options': [
                {'value': 'draft', 'label': 'Rascunho'},
                {'value': 'published', 'label': 'Publicado'},
                {'value': 'scheduled', 'label': 'Agendado'}
            ],
            'value': 'draft'
        },
        'publish_date': {
            'type': 'datetime',
            'label': 'Data de Publicação',
            'value': '2024-01-15T10:00'
        },
        'author': {
            'type': 'select',
            'label': 'Autor',
            'options': [
                {'value': '1', 'label': 'João Silva'},
                {'value': '2', 'label': 'Ana Santos'},
                {'value': '3', 'label': 'Carlos Oliveira'}
            ],
            'value': '1'
        }
    },
    'seo': {
        'meta_title': 'Como Criar Conteúdo Engajante - Blog',
        'meta_description': 'Descubra as melhores práticas para criar conteúdo que realmente engaja sua audiência e gera resultados.',
        'keywords': 'conteúdo, marketing, engajamento, audiência, blog',
        'og_image': 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1200&h=630&fit=crop'
    },
    'preview_url': '/blog/como-criar-conteudo-engajante'
}

# Content manager para notícias
content_manager_news = {
    'title': 'Nova Notícia',
    'content_type': 'news',
    'fields': {
        'headline': {
            'type': 'text',
            'label': 'Manchete',
            'placeholder': 'Digite a manchete da notícia...',
            'required': True,
            'value': 'Nova Tecnologia Revoluciona Setor de Energia'
        },
        'subheadline': {
            'type': 'text',
            'label': 'Subtítulo',
            'placeholder': 'Subtítulo ou linha de apoio...',
            'value': 'Inovação promete reduzir custos em até 40% e aumentar eficiência energética'
        },
        'lead': {
            'type': 'textarea',
            'label': 'Lead',
            'placeholder': 'Primeiro parágrafo com as informações principais...',
            'max_length': 200,
            'value': 'Uma nova tecnologia desenvolvida por pesquisadores brasileiros promete revolucionar o setor energético, oferecendo soluções mais sustentáveis e econômicas.'
        },
        'content': {
            'type': 'rich_text',
            'label': 'Corpo da Notícia',
            'toolbar': ['bold', 'italic', 'underline', 'bulletList', 'orderedList', 'link', 'image', 'blockquote', 'quote'],
            'value': '''
            <p>SÃO PAULO - Uma equipe de pesquisadores da Universidade de São Paulo desenvolveu uma tecnologia inovadora que pode transformar completamente o setor de energia renovável no país.</p>
            
            <p>A nova solução, que ainda está em fase de testes, utiliza materiais nanoestruturados para aumentar significativamente a eficiência de painéis solares.</p>
            
            <blockquote>
                <p>"Os resultados iniciais são extremamente promissores. Conseguimos um aumento de 40% na eficiência energética", afirma Dr. Maria Silva, líder da pesquisa.</p>
            </blockquote>
            
            <p>A tecnologia deverá estar disponível comercialmente dentro de dois anos, segundo os pesquisadores.</p>
            '''
        },
        'location': {
            'type': 'text',
            'label': 'Local',
            'placeholder': 'São Paulo, Rio de Janeiro...',
            'value': 'São Paulo'
        },
        'source': {
            'type': 'text',
            'label': 'Fonte',
            'placeholder': 'Fonte da informação...',
            'value': 'Universidade de São Paulo'
        },
        'urgency': {
            'type': 'select',
            'label': 'Urgência',
            'options': [
                {'value': 'low', 'label': 'Baixa'},
                {'value': 'normal', 'label': 'Normal'},
                {'value': 'high', 'label': 'Alta'},
                {'value': 'breaking', 'label': 'Última Hora'}
            ],
            'value': 'normal'
        },
        'featured_image': {
            'type': 'image',
            'label': 'Imagem Principal',
            'accept': 'image/*',
            'value': 'https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=800&h=400&fit=crop'
        },
        'gallery': {
            'type': 'image_gallery',
            'label': 'Galeria de Imagens',
            'multiple': True,
            'value': [
                'https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=400&h=300&fit=crop',
                'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400&h=300&fit=crop'
            ]
        }
    },
    'publishing': {
        'status': 'published',
        'publish_immediately': True,
        'featured': True,
        'breaking_news': False
    }
}

# Content manager para produtos/anúncios
content_manager_product = {
    'title': 'Novo Produto',
    'content_type': 'product',
    'fields': {
        'name': {
            'type': 'text',
            'label': 'Nome do Produto',
            'required': True,
            'value': 'Smartphone XR Pro Max'
        },
        'short_description': {
            'type': 'textarea',
            'label': 'Descrição Curta',
            'max_length': 120,
            'value': 'O smartphone mais avançado da nossa linha, com câmera profissional e performance excepcional.'
        },
        'description': {
            'type': 'rich_text',
            'label': 'Descrição Completa',
            'toolbar': ['bold', 'italic', 'underline', 'heading2', 'heading3', 'bulletList', 'orderedList', 'link', 'image', 'table'],
            'value': '''
            <h2>Características Principais</h2>
            <ul>
                <li><strong>Tela</strong>: 6.7" OLED Super Retina</li>
                <li><strong>Processador</strong>: Chip A17 Pro</li>
                <li><strong>Câmera</strong>: Sistema triplo 48MP</li>
                <li><strong>Bateria</strong>: Até 29 horas de reprodução de vídeo</li>
            </ul>
            
            <h3>Design Premium</h3>
            <p>Construído com materiais de alta qualidade, incluindo titânio aeroespacial e vidro Ceramic Shield.</p>
            '''
        },
        'price': {
            'type': 'number',
            'label': 'Preço (R$)',
            'value': 8999.00,
            'step': 0.01
        },
        'sale_price': {
            'type': 'number',
            'label': 'Preço Promocional (R$)',
            'value': 7999.00,
            'step': 0.01
        },
        'images': {
            'type': 'image_gallery',
            'label': 'Imagens do Produto',
            'multiple': True,
            'required': True,
            'value': [
                'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600&h=600&fit=crop',
                'https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=600&h=600&fit=crop'
            ]
        },
        'category': {
            'type': 'select',
            'label': 'Categoria',
            'options': [
                {'value': 'smartphones', 'label': 'Smartphones'},
                {'value': 'tablets', 'label': 'Tablets'},
                {'value': 'laptops', 'label': 'Laptops'},
                {'value': 'acessorios', 'label': 'Acessórios'}
            ],
            'value': 'smartphones'
        },
        'brand': {
            'type': 'text',
            'label': 'Marca',
            'value': 'TechBrand'
        },
        'sku': {
            'type': 'text',
            'label': 'SKU',
            'value': 'SMART-XR-PRO-001'
        },
        'stock': {
            'type': 'number',
            'label': 'Estoque',
            'value': 150
        },
        'specifications': {
            'type': 'key_value',
            'label': 'Especificações',
            'value': {
                'Tela': '6.7" OLED',
                'Processador': 'A17 Pro',
                'RAM': '8GB',
                'Armazenamento': '256GB',
                'Peso': '221g'
            }
        }
    },
    'seo': {
        'meta_title': 'Smartphone XR Pro Max - TechBrand',
        'meta_description': 'O smartphone mais avançado com câmera profissional, chip A17 Pro e design premium. Compre agora com desconto especial.',
        'keywords': 'smartphone, celular, A17 Pro, câmera profissional, TechBrand'
    }
}

# Content manager para páginas estáticas
content_manager_page = {
    'title': 'Nova Página',
    'content_type': 'page',
    'fields': {
        'title': {
            'type': 'text',
            'label': 'Título da Página',
            'required': True,
            'value': 'Sobre Nós'
        },
        'content': {
            'type': 'rich_text',
            'label': 'Conteúdo',
            'toolbar': ['bold', 'italic', 'underline', 'heading1', 'heading2', 'heading3', 'bulletList', 'orderedList', 'link', 'image', 'blockquote', 'table', 'codeBlock'],
            'value': '''
            <h1>Sobre Nossa Empresa</h1>
            <p>Somos uma empresa inovadora dedicada a criar soluções tecnológicas que transformam negócios e melhoram a vida das pessoas.</p>
            
            <h2>Nossa Missão</h2>
            <p>Democratizar o acesso à tecnologia através de soluções simples, eficientes e acessíveis.</p>
            
            <h2>Nossa Equipe</h2>
            <p>Contamos com mais de 100 profissionais especializados em diversas áreas da tecnologia.</p>
            '''
        },
        'template': {
            'type': 'select',
            'label': 'Template',
            'options': [
                {'value': 'default', 'label': 'Padrão'},
                {'value': 'full-width', 'label': 'Largura Completa'},
                {'value': 'sidebar', 'label': 'Com Sidebar'},
                {'value': 'landing', 'label': 'Landing Page'}
            ],
            'value': 'default'
        },
        'show_in_menu': {
            'type': 'checkbox',
            'label': 'Mostrar no Menu',
            'value': True
        },
        'menu_order': {
            'type': 'number',
            'label': 'Ordem no Menu',
            'value': 1
        }
    }
}

# Configurações de campos disponíveis
field_types = {
    'text': {
        'label': 'Texto',
        'description': 'Campo de texto simples',
        'attributes': ['placeholder', 'max_length', 'required', 'pattern']
    },
    'textarea': {
        'label': 'Área de Texto',
        'description': 'Campo de texto multilinha',
        'attributes': ['placeholder', 'max_length', 'rows', 'required']
    },
    'rich_text': {
        'label': 'Editor de Texto Rico',
        'description': 'Editor com formatação avançada',
        'attributes': ['toolbar', 'height', 'placeholder', 'image_upload']
    },
    'select': {
        'label': 'Lista Suspensa',
        'description': 'Campo de seleção única',
        'attributes': ['options', 'required', 'searchable']
    },
    'checkbox': {
        'label': 'Caixa de Seleção',
        'description': 'Campo verdadeiro/falso',
        'attributes': ['checked']
    },
    'image': {
        'label': 'Imagem',
        'description': 'Upload de imagem única',
        'attributes': ['accept', 'max_size', 'required', 'dimensions']
    },
    'image_gallery': {
        'label': 'Galeria de Imagens',
        'description': 'Upload múltiplo de imagens',
        'attributes': ['max_files', 'accept', 'required']
    },
    'number': {
        'label': 'Número',
        'description': 'Campo numérico',
        'attributes': ['min', 'max', 'step', 'required']
    },
    'datetime': {
        'label': 'Data e Hora',
        'description': 'Campo de data e hora',
        'attributes': ['min', 'max', 'required']
    },
    'tags': {
        'label': 'Tags',
        'description': 'Campo de múltiplas tags',
        'attributes': ['separator', 'max_tags', 'autocomplete']
    },
    'key_value': {
        'label': 'Chave-Valor',
        'description': 'Pares de chave e valor',
        'attributes': ['max_pairs', 'key_placeholder', 'value_placeholder']
    }
}

# Parâmetros do content manager
content_manager_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>title</code>', 'string', '-', 'Título do formulário de conteúdo'],
        ['<code>content_type</code>', 'string', 'post', 'Tipo de conteúdo: post, page, product, news'],
        ['<code>fields</code>', 'object', '{}', 'Configuração dos campos do formulário'],
        ['<code>auto_save</code>', 'boolean', 'true', 'Se salva automaticamente como rascunho'],
        ['<code>auto_save_interval</code>', 'number', '30', 'Intervalo de auto-save em segundos'],
        ['<code>word_count</code>', 'boolean', 'true', 'Se mostra contador de palavras'],
        ['<code>character_count</code>', 'boolean', 'false', 'Se mostra contador de caracteres'],
        ['<code>preview_mode</code>', 'boolean', 'true', 'Se permite visualização'],
        ['<code>publish_options</code>', 'boolean', 'true', 'Se mostra opções de publicação'],
        ['<code>seo_fields</code>', 'boolean', 'true', 'Se inclui campos de SEO'],
        ['<code>media_library</code>', 'boolean', 'true', 'Se ativa biblioteca de mídia'],
        ['<code>version_control</code>', 'boolean', 'false', 'Se mantém histórico de versões'],
        ['<code>collaborative</code>', 'boolean', 'false', 'Se permite edição colaborativa'],
        ['<code>workflow</code>', 'boolean', 'false', 'Se ativa fluxo de aprovação'],
        ['<code>on_save</code>', 'string', '-', 'Callback para salvamento'],
        ['<code>on_publish</code>', 'string', '-', 'Callback para publicação'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Dados consolidados do content manager
CONTENT_MANAGER_DATA = {
    'blog': content_manager_blog,
    'news': content_manager_news,
    'product': content_manager_product,
    'page': content_manager_page,
    'field_types': field_types,
    'params': content_manager_params,
} 