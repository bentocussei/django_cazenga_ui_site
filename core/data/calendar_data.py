"""
Dados específicos para o componente Calendar
"""

CALENDAR_EVENTS = [
    {
        'date': '2025-01-15',
        'title': 'Reunião de equipe',
        'time': '10:00'
    },
    {
        'date': '2025-01-20',
        'title': 'Apresentação do projeto',
        'time': '14:30'
    },
    {
        'date': '2025-01-25',
        'title': 'Revisão de código',
        'time': '09:00'
    },
]

# Formato correto: YYYY-MM-DD (para compatibilidade com o componente)
CALENDAR_MULTIPLE_DATES = "2025-01-15,2025-01-20,2025-01-25"
CALENDAR_MIN_DATE = "2025-01-01"
CALENDAR_MAX_DATE = "2025-01-31"
CALENDAR_HIGHLIGHT_DATES = [
    {"date": "2025-01-25", "type": "holiday", "title": "Natal"},
    {"date": "2025-01-01", "type": "holiday", "title": "Ano Novo"},
    {"date": "2025-01-15", "type": "event", "title": "Reunião de Equipe"}
]

CALENDAR_PARAMS = {
    "headers": ["Parâmetro", "Tipo", "Padrão", "Descrição"],
    "data": [
        ["selected_date", "String", "-", "Data pré-selecionada (formato YYYY-MM-DD)"],
        ["mode", "String", "single", "Modo de seleção: single, multiple, range"],
        ["selected_dates", "String", "-", "Múltiplas datas separadas por vírgula"],
        ["min_date", "String", "-", "Data mínima selecionável"],
        ["max_date", "String", "-", "Data máxima selecionável"],
        ["highlight_dates", "List", "-", "Lista de datas para destacar"],
        ["x_model", "String", "-", "Variável Alpine.js para binding"],
        ["locale", "String", "pt-BR", "Localização do calendário"]
    ]
}

CALENDAR_DATA = {
    'events': CALENDAR_EVENTS,
    'multiple_dates': CALENDAR_MULTIPLE_DATES,
    'min_date': CALENDAR_MIN_DATE,
    'max_date': CALENDAR_MAX_DATE,
    'highlight_dates': CALENDAR_HIGHLIGHT_DATES,
    'params': CALENDAR_PARAMS
} 