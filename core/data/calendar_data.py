"""
Dados específicos para o componente Calendar
"""

CALENDAR_EVENTS = [
    {
        'date': '2024-01-15',
        'title': 'Reunião de equipe',
        'time': '10:00'
    },
    {
        'date': '2024-01-20',
        'title': 'Apresentação do projeto',
        'time': '14:30'
    },
    {
        'date': '2024-01-25',
        'title': 'Revisão de código',
        'time': '09:00'
    },
]

CALENDAR_MULTIPLE_DATES = ["15/12/2024", "20/12/2024", "25/12/2024"]
CALENDAR_MIN_DATE = "01/12/2024"
CALENDAR_MAX_DATE = "31/12/2024"
CALENDAR_HIGHLIGHT_DATES = [
    {"date": "25/12/2024", "type": "holiday", "title": "Natal"},
    {"date": "01/01/2025", "type": "holiday", "title": "Ano Novo"},
    {"date": "15/12/2024", "type": "event", "title": "Reunião de Equipe"}
]

CALENDAR_PARAMS = {
    "headers": ["Parâmetro", "Tipo", "Padrão", "Descrição"],
    "data": [
        ["selected_date", "String", "-", "Data pré-selecionada (formato DD/MM/YYYY)"],
        ["multiple", "Boolean", "False", "Permite seleção múltipla de datas"],
        ["selected_dates", "List", "-", "Lista de datas selecionadas"],
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