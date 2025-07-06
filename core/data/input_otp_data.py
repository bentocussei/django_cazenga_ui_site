# Dados do componente Input OTP

# Input OTP básico (6 dígitos)
input_otp_basic = {
    'length': 6,
    'placeholder': '●',
    'label': 'Código de Verificação',
    'description': 'Insira o código de 6 dígitos enviado para seu email.',
    'auto_focus': True
}

# Input OTP de 4 dígitos (PIN)
input_otp_pin = {
    'length': 4,
    'type': 'password',
    'placeholder': '●',
    'label': 'PIN de Segurança',
    'description': 'Digite seu PIN de 4 dígitos.',
    'auto_focus': True,
    'numeric_only': True
}

# Input OTP de 8 dígitos (código longo)
input_otp_long = {
    'length': 8,
    'placeholder': '-',
    'label': 'Código de Autenticação',
    'description': 'Insira o código de 8 caracteres do seu aplicativo autenticador.',
    'auto_focus': True,
    'separator': '-'
}

# Input OTP com validação
input_otp_validation = {
    'length': 6,
    'placeholder': '0',
    'label': 'Código SMS',
    'description': 'Código enviado via SMS para +55 (11) 9****-1234',
    'auto_focus': True,
    'validation': True,
    'error_message': 'Código inválido. Tente novamente.',
    'success_message': 'Código verificado com sucesso!'
}

# Input OTP customizado
input_otp_custom = {
    'length': 5,
    'placeholder': '?',
    'label': 'Código Personalizado',
    'description': 'Exemplo de OTP com estilo customizado.',
    'auto_focus': True,
    'custom_style': True,
    'border_color': 'border-blue-300',
    'focus_color': 'focus:border-blue-500'
}

# Variações de tamanho
input_otp_sizes = {
    'small': {
        'length': 4,
        'size': 'sm',
        'label': 'OTP Pequeno',
        'class': 'h-8 w-8 text-sm'
    },
    'medium': {
        'length': 4,
        'size': 'md',
        'label': 'OTP Médio',
        'class': 'h-10 w-10 text-base'
    },
    'large': {
        'length': 4,
        'size': 'lg',
        'label': 'OTP Grande',
        'class': 'h-12 w-12 text-lg'
    }
}

# Estados do componente
input_otp_states = {
    'normal': {
        'length': 4,
        'label': 'Estado Normal',
        'placeholder': '0'
    },
    'error': {
        'length': 4,
        'label': 'Estado de Erro',
        'placeholder': '0',
        'error': True,
        'error_message': 'Código incorreto'
    },
    'success': {
        'length': 4,
        'label': 'Estado de Sucesso',
        'placeholder': '0',
        'success': True,
        'success_message': 'Código válido'
    },
    'disabled': {
        'length': 4,
        'label': 'Estado Desabilitado',
        'placeholder': '0',
        'disabled': True
    }
}

# Parâmetros do input OTP
input_otp_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['<code>length</code>', 'number', '6', 'Número de campos de entrada (obrigatório)'],
        ['<code>type</code>', 'string', 'text', 'Tipo de input: text, password, number'],
        ['<code>placeholder</code>', 'string', '●', 'Placeholder para cada campo'],
        ['<code>label</code>', 'string', '-', 'Label do grupo de campos'],
        ['<code>description</code>', 'string', '-', 'Texto de ajuda/descrição'],
        ['<code>auto_focus</code>', 'boolean', 'true', 'Se deve focar automaticamente no primeiro campo'],
        ['<code>numeric_only</code>', 'boolean', 'false', 'Se aceita apenas números'],
        ['<code>separator</code>', 'string', '-', 'Caractere separador entre campos'],
        ['<code>size</code>', 'string', 'md', 'Tamanho dos campos: sm, md, lg'],
        ['<code>validation</code>', 'boolean', 'false', 'Se deve validar em tempo real'],
        ['<code>error</code>', 'boolean', 'false', 'Estado de erro'],
        ['<code>error_message</code>', 'string', '-', 'Mensagem de erro'],
        ['<code>success</code>', 'boolean', 'false', 'Estado de sucesso'],
        ['<code>success_message</code>', 'string', '-', 'Mensagem de sucesso'],
        ['<code>disabled</code>', 'boolean', 'false', 'Se os campos estão desabilitados'],
        ['<code>class</code>', 'string', '-', 'Classes CSS adicionais'],
        ['<code>x_model</code>', 'string', '-', 'Modelo Alpine.js para binding'],
    ]
}

# Dados consolidados do input OTP
INPUT_OTP_DATA = {
    'basic': input_otp_basic,
    'pin': input_otp_pin,
    'long': input_otp_long,
    'validation': input_otp_validation,
    'custom': input_otp_custom,
    'sizes': input_otp_sizes,
    'states': input_otp_states,
    'params': input_otp_params,
} 