# Dados do componente Sonner
sonner_params = {
    'headers': ['Parâmetro', 'Tipo', 'Padrão', 'Descrição'],
    'data': [
        ['position', 'string', 'bottom-right', 'Posição do toast: top-left, top-center, top-right, bottom-left, bottom-center, bottom-right'],
        ['duration', 'number', '4000', 'Duração em milissegundos (0 = permanente)'],
        ['max_toasts', 'number', '5', 'Número máximo de toasts visíveis simultaneamente'],
        ['class', 'string', '-', 'Classes CSS adicionais'],
    ]
}

# Exemplos básicos de toast
sonner_basic = {
    'position': 'top-right',
    'duration': 4000,
    'max_toasts': 5,
    'examples': [
        {
            'type': 'success',
            'title': 'Sucesso!',
            'description': 'Operação concluída com sucesso.'
        },
        {
            'type': 'error',
            'title': 'Erro!',
            'description': 'Ocorreu um erro ao processar a solicitação.'
        },
        {
            'type': 'warning',
            'title': 'Atenção!',
            'description': 'Verifique os dados antes de continuar.'
        },
        {
            'type': 'info',
            'title': 'Informação',
            'description': 'Nova atualização disponível.'
        }
    ]
}

# Toast com ações
sonner_with_action = {
    'position': 'bottom-right',
    'duration': 8000,
    'examples': [
        {
            'type': 'success',
            'title': 'Upload Concluído',
            'description': 'Arquivo enviado com sucesso!',
            'action': 'Visualizar'
        },
        {
            'type': 'info',
            'title': 'Nova Mensagem',
            'description': 'Você tem uma nova mensagem.',
            'action': 'Ler Agora'
        }
    ]
}

# Toast permanente
sonner_permanent = {
    'position': 'top-center',
    'duration': 0,
    'examples': [
        {
            'type': 'warning',
            'title': 'Sessão Expirando',
            'description': 'Sua sessão expirará em 5 minutos.',
            'action': 'Renovar'
        },
        {
            'type': 'info',
            'title': 'Atualização Disponível',
            'description': 'Nova versão do sistema disponível.',
            'action': 'Atualizar'
        }
    ]
}

# Toast com posições diferentes
sonner_positions = {
    'examples': [
        {
            'position': 'top-left',
            'type': 'info',
            'title': 'Superior Esquerda',
            'description': 'Toast na posição superior esquerda.'
        },
        {
            'position': 'top-center',
            'type': 'success',
            'title': 'Superior Centro',
            'description': 'Toast na posição superior centro.'
        },
        {
            'position': 'top-right',
            'type': 'warning',
            'title': 'Superior Direita',
            'description': 'Toast na posição superior direita.'
        },
        {
            'position': 'bottom-left',
            'type': 'error',
            'title': 'Inferior Esquerda',
            'description': 'Toast na posição inferior esquerda.'
        },
        {
            'position': 'bottom-center',
            'type': 'info',
            'title': 'Inferior Centro',
            'description': 'Toast na posição inferior centro.'
        },
        {
            'position': 'bottom-right',
            'type': 'success',
            'title': 'Inferior Direita',
            'description': 'Toast na posição inferior direita.'
        }
    ]
}

# Toast com configurações especiais
sonner_special = {
    'examples': [
        {
            'type': 'info',
            'title': 'Backup Iniciado',
            'description': 'Fazendo backup dos dados...',
            'duration': 8000,
            'closable': False
        },
        {
            'type': 'error',
            'title': 'Falha na Conexão',
            'description': 'Não foi possível conectar ao servidor.',
            'duration': 10000,
            'action': 'Tentar Novamente'
        },
        {
            'type': 'success',
            'title': 'Processo Completo',
            'description': 'Todos os itens foram processados.',
            'duration': 3000
        }
    ]
} 