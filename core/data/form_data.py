# Dados do componente Form
form_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['fields', 'array', '[]', 'Lista de campos do formulário (obrigatório)'],
        ['action', 'string', '-', 'URL de ação do formulário'],
        ['method', 'string', 'POST', 'Método HTTP: GET, POST'],
        ['enctype', 'string', '-', 'Tipo de codificação: multipart/form-data, application/x-www-form-urlencoded'],
        ['novalidate', 'boolean', 'false', 'Desabilitar validação HTML5'],
        ['class', 'string', '-', 'Classes CSS adicionais'],
        ['x_data', 'string', '-', 'Dados Alpine.js adicionais'],
        ['on_submit', 'string', '-', 'Função JavaScript no submit'],
        ['submit_button', 'object', '{}', 'Configurações do botão submit'],
        ['cancel_button', 'object', '-', 'Configurações do botão cancelar'],
    ]
}

# Campos disponíveis para formulários
form_field_types = {
    'headers': ['Tipo', 'Parâmetros', 'Descrição'],
    'data': [
        ['text', 'name, label, placeholder, value, required, disabled, readonly', 'Campo de texto simples'],
        ['email', 'name, label, placeholder, value, required, disabled', 'Campo de email com validação'],
        ['password', 'name, label, placeholder, required, disabled', 'Campo de senha'],
        ['textarea', 'name, label, placeholder, value, rows, required, disabled', 'Área de texto multi-linha'],
        ['select', 'name, label, options, value, searchable, disabled', 'Campo de seleção'],
        ['checkbox', 'name, label, checked, disabled', 'Caixa de seleção'],
        ['radio', 'name, label, options, value, orientation, disabled', 'Botões de opção'],
        ['switch', 'name, label, checked, disabled', 'Interruptor'],
        ['number', 'name, label, placeholder, value, min, max, step', 'Campo numérico'],
        ['date', 'name, label, value, min, max, disabled', 'Campo de data'],
        ['file', 'name, label, accept, multiple, disabled', 'Campo de arquivo'],
    ]
}

# Formulário básico de contato
form_basic_contact = {
    'action': '#',
    'method': 'POST',
    'fields': [
        {
            'type': 'text',
            'name': 'name',
            'label': 'Nome',
            'placeholder': 'Digite seu nome',
            'required': True,
            'description': 'Nome completo'
        },
        {
            'type': 'email',
            'name': 'email',
            'label': 'Email',
            'placeholder': 'seu@email.com',
            'required': True,
            'description': 'Endereço de email válido'
        },
        {
            'type': 'textarea',
            'name': 'message',
            'label': 'Mensagem',
            'placeholder': 'Digite sua mensagem...',
            'rows': 4,
            'required': True,
            'description': 'Descreva sua solicitação'
        }
    ],
    'submit_button': {
        'text': 'Enviar Mensagem',
        'variant': 'default'
    },
    'cancel_button': {
        'text': 'Limpar',
        'onclick': 'document.forms[0].reset()'
    }
}

# Formulário de registro
form_register = {
    'action': '/register',
    'method': 'POST',
    'fields': [
        {
            'type': 'text',
            'name': 'first_name',
            'label': 'Nome',
            'placeholder': 'Primeiro nome',
            'required': True
        },
        {
            'type': 'text',
            'name': 'last_name',
            'label': 'Sobrenome',
            'placeholder': 'Último nome',
            'required': True
        },
        {
            'type': 'email',
            'name': 'email',
            'label': 'Email',
            'placeholder': 'seu@email.com',
            'required': True
        },
        {
            'type': 'password',
            'name': 'password',
            'label': 'Senha',
            'placeholder': '••••••••',
            'required': True,
            'description': 'Mínimo 8 caracteres'
        },
        {
            'type': 'password',
            'name': 'confirm_password',
            'label': 'Confirmar Senha',
            'placeholder': '••••••••',
            'required': True
        },
        {
            'type': 'checkbox',
            'name': 'terms',
            'label': 'Aceito os termos e condições',
            'required': True
        }
    ],
    'submit_button': {
        'text': 'Criar Conta',
        'variant': 'default'
    }
}

# Formulário de perfil
form_profile = {
    'action': '/profile',
    'method': 'POST',
    'enctype': 'multipart/form-data',
    'fields': [
        {
            'type': 'file',
            'name': 'avatar',
            'label': 'Foto de Perfil',
            'accept': 'image/*',
            'description': 'Formatos aceitos: JPG, PNG, GIF (máx. 2MB)'
        },
        {
            'type': 'text',
            'name': 'display_name',
            'label': 'Nome de Exibição',
            'placeholder': 'Como você quer ser chamado',
            'required': True
        },
        {
            'type': 'textarea',
            'name': 'bio',
            'label': 'Biografia',
            'placeholder': 'Conte um pouco sobre você...',
            'rows': 3,
            'description': 'Máximo 500 caracteres'
        },
        {
            'type': 'text',
            'name': 'website',
            'label': 'Website',
            'placeholder': 'https://seusite.com'
        },
        {
            'type': 'select',
            'name': 'country',
            'label': 'País',
            'options': [
                {'value': 'BR', 'label': 'Brasil'},
                {'value': 'US', 'label': 'Estados Unidos'},
                {'value': 'CA', 'label': 'Canadá'},
                {'value': 'UK', 'label': 'Reino Unido'}
            ],
            'placeholder': 'Selecione seu país'
        }
    ],
    'submit_button': {
        'text': 'Salvar Perfil',
        'variant': 'default'
    },
    'cancel_button': {
        'text': 'Cancelar',
        'href': '/profile'
    }
}

# Formulário de configurações
form_settings = {
    'action': '/settings',
    'method': 'POST',
    'fields': [
        {
            'type': 'switch',
            'name': 'notifications',
            'label': 'Receber Notificações',
            'checked': True,
            'description': 'Receber notificações por email'
        },
        {
            'type': 'switch',
            'name': 'newsletter',
            'label': 'Newsletter',
            'checked': False,
            'description': 'Receber newsletter semanal'
        },
        {
            'type': 'radio',
            'name': 'theme',
            'label': 'Tema',
            'options': [
                {'value': 'light', 'label': 'Claro'},
                {'value': 'dark', 'label': 'Escuro'},
                {'value': 'system', 'label': 'Sistema'}
            ],
            'value': 'system',
            'orientation': 'horizontal'
        },
        {
            'type': 'select',
            'name': 'language',
            'label': 'Idioma',
            'options': [
                {'value': 'pt-BR', 'label': 'Português (Brasil)'},
                {'value': 'en-US', 'label': 'English (US)'},
                {'value': 'es-ES', 'label': 'Español'}
            ],
            'value': 'pt-BR',
            'searchable': True
        },
        {
            'type': 'select',
            'name': 'timezone',
            'label': 'Fuso Horário',
            'options': [
                {'value': 'America/Sao_Paulo', 'label': 'Brasília (GMT-3)'},
                {'value': 'America/New_York', 'label': 'Nova York (GMT-5)'},
                {'value': 'Europe/London', 'label': 'Londres (GMT+0)'},
                {'value': 'Asia/Tokyo', 'label': 'Tóquio (GMT+9)'}
            ],
            'value': 'America/Sao_Paulo',
            'searchable': True
        }
    ],
    'submit_button': {
        'text': 'Salvar Configurações',
        'variant': 'default'
    }
}

# Formulário com validação
form_validation = {
    'action': '#',
    'method': 'POST',
    'x_data': '{ formData: {}, errors: {} }',
    'fields': [
        {
            'type': 'email',
            'name': 'email',
            'label': 'Email',
            'placeholder': 'seu@email.com',
            'required': True,
            'error': 'Email inválido'
        },
        {
            'type': 'password',
            'name': 'password',
            'label': 'Senha',
            'placeholder': '••••••••',
            'required': True,
            'error': 'Senha deve ter pelo menos 8 caracteres'
        },
        {
            'type': 'number',
            'name': 'age',
            'label': 'Idade',
            'placeholder': '18',
            'min': 18,
            'max': 120,
            'required': True,
            'error': 'Idade deve ser entre 18 e 120 anos'
        },
        {
            'type': 'date',
            'name': 'birth_date',
            'label': 'Data de Nascimento',
            'required': True,
            'error': 'Data de nascimento é obrigatória'
        }
    ],
    'submit_button': {
        'text': 'Validar',
        'variant': 'default'
    }
} 