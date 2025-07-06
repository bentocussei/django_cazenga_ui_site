"""
Dados centralizados para todos os componentes
"""

# Importações dos dados dos componentes
from .button_data import BUTTON_PARAMS, BUTTON_DATA
from .alert_data import ALERT_EXAMPLES, ALERT_PARAMS, ALERT_DATA
from .input_data import INPUT_PARAMS, INPUT_DATA
from .table_data import TABLE_BASIC_DATA, TABLE_RESPONSIVE_DATA, TABLE_PARAMS, TABLE_DATA
from .card_data import CARD_PARAMS, CARD_DATA
from .accordion_data import ACCORDION_DATA, ACCORDION_ITEMS, ACCORDION_PARAMS
from .aspect_ratio_data import ASPECT_RATIO_DATA, ASPECT_RATIO_SAMPLE_IMAGES, ASPECT_RATIO_SAMPLE_VIDEOS, ASPECT_RATIO_PARAMS
from .avatar_data import AVATAR_DATA, AVATAR_EXAMPLES, AVATAR_PARAMS
from .badge_data import BADGE_DATA, BADGE_EXAMPLES, BADGE_PARAMS
from .breadcrumb_data import BREADCRUMB_DATA, BREADCRUMB_ITEMS, BREADCRUMB_PARAMS
from .calendar_data import CALENDAR_DATA, CALENDAR_EVENTS, CALENDAR_PARAMS
from .checkbox_data import CHECKBOX_DATA, CHECKBOX_PARAMS
from .progress_data import PROGRESS_DATA, PROGRESS_PARAMS
from .radio_group_data import RADIO_GROUP_OPTIONS, RADIO_GROUP_DATA, RADIO_GROUP_PARAMS
from .switch_data import SWITCH_DATA, SWITCH_PARAMS
from .tabs_data import TABS_DATA, TABS_PARAMS
from .collapsible_data import COLLAPSIBLE_DATA, COLLAPSIBLE_PARAMS
from .alert_dialog_data import ALERT_DIALOG_DATA
from .dialog_data import DIALOG_DATA, DIALOG_PARAMS

# Novas importações dos componentes criados
from .label_data import LABEL_DATA, LABEL_EXAMPLES, LABEL_PARAMS
from .separator_data import SEPARATOR_DATA, SEPARATOR_EXAMPLES, SEPARATOR_PARAMS
from .skeleton_data import SKELETON_DATA, SKELETON_EXAMPLES, SKELETON_PARAMS
from .spinner_data import SPINNER_DATA, SPINNER_EXAMPLES, SPINNER_PARAMS
from .toggle_data import TOGGLE_DATA, TOGGLE_EXAMPLES, TOGGLE_PARAMS
from .tooltip_data import TOOLTIP_DATA, TOOLTIP_EXAMPLES, TOOLTIP_PARAMS

# Mapeamento para facilitar o acesso
COMPONENT_DATA = {
    'button': {
        'data': BUTTON_DATA,
        'params': BUTTON_PARAMS,
    },
    'alert': {
        'examples': ALERT_EXAMPLES,
        'data': ALERT_DATA,
        'params': ALERT_PARAMS,
    },
    'input': {
        'data': INPUT_DATA,
        'params': INPUT_PARAMS,
    },
    'table': TABLE_DATA,
    'card': {
        'data': CARD_DATA,
        'params': CARD_PARAMS,
    },
    'accordion': {
        'items': ACCORDION_ITEMS,
        'data': ACCORDION_DATA,
        'params': ACCORDION_PARAMS,
    },
    'aspect-ratio': {
        'data': ASPECT_RATIO_DATA,
        'sample_images': ASPECT_RATIO_SAMPLE_IMAGES,
        'sample_videos': ASPECT_RATIO_SAMPLE_VIDEOS,
        'params': ASPECT_RATIO_PARAMS,
    },
    'avatar': {
        'examples': AVATAR_EXAMPLES,
        'data': AVATAR_DATA,
        'params': AVATAR_PARAMS,
    },
    'badge': {
        'examples': BADGE_EXAMPLES,
        'data': BADGE_DATA,
        'params': BADGE_PARAMS,
    },
    'breadcrumb': {
        'items': BREADCRUMB_ITEMS,
        'data': BREADCRUMB_DATA,
        'with_icons': BREADCRUMB_DATA['with_icons'],
        'params': BREADCRUMB_PARAMS,
    },
    'calendar': {
        'events': CALENDAR_EVENTS,
        'data': CALENDAR_DATA,
        'multiple_dates': CALENDAR_DATA['multiple_dates'],
        'min_date': CALENDAR_DATA['min_date'],
        'max_date': CALENDAR_DATA['max_date'],
        'highlight_dates': CALENDAR_DATA['highlight_dates'],
        'params': CALENDAR_PARAMS,
    },
    'checkbox': {
        'data': CHECKBOX_DATA,
        'params': CHECKBOX_PARAMS,
    },
    'progress': {
        'data': PROGRESS_DATA,
        'params': PROGRESS_PARAMS,
    },
    'radio-group': {
        'options': RADIO_GROUP_OPTIONS,
        'data': RADIO_GROUP_DATA,
        'params': RADIO_GROUP_PARAMS,
    },
    'switch': {
        'data': SWITCH_DATA,
        'params': SWITCH_PARAMS,
    },
    'tabs': TABS_DATA,
    'collapsible': {
        'data': COLLAPSIBLE_DATA,
        'params': COLLAPSIBLE_PARAMS,
    },
    'alert-dialog': {
        'data': ALERT_DIALOG_DATA,
        'params': ALERT_DIALOG_DATA['params'],
    },
    'dialog': {
        'data': DIALOG_DATA,
        'params': DIALOG_PARAMS,
    },
    # Novos componentes adicionados
    'label': {
        'examples': LABEL_EXAMPLES,
        'data': LABEL_DATA,
        'params': LABEL_PARAMS,
    },
    'separator': {
        'examples': SEPARATOR_EXAMPLES,
        'data': SEPARATOR_DATA,
        'params': SEPARATOR_PARAMS,
    },
    'skeleton': {
        'examples': SKELETON_EXAMPLES,
        'data': SKELETON_DATA,
        'params': SKELETON_PARAMS,
    },
    'spinner': {
        'examples': SPINNER_EXAMPLES,
        'data': SPINNER_DATA,
        'params': SPINNER_PARAMS,
    },
    'toggle': {
        'examples': TOGGLE_EXAMPLES,
        'data': TOGGLE_DATA,
        'params': TOGGLE_PARAMS,
    },
    'tooltip': {
        'examples': TOOLTIP_EXAMPLES,
        'data': TOOLTIP_DATA,
        'params': TOOLTIP_PARAMS,
    },
}

# Facilitar importação direta
__all__ = [
    'BUTTON_PARAMS', 'BUTTON_DATA',
    'ALERT_EXAMPLES', 'ALERT_PARAMS', 'ALERT_DATA',
    'INPUT_DATA', 'INPUT_PARAMS',
    'TABLE_BASIC_DATA', 'TABLE_RESPONSIVE_DATA', 'TABLE_PARAMS', 'TABLE_DATA',
    'CARD_DATA', 'CARD_PARAMS',
    'ACCORDION_DATA', 'ACCORDION_ITEMS', 'ACCORDION_PARAMS',
    'ASPECT_RATIO_DATA', 'ASPECT_RATIO_SAMPLE_IMAGES', 'ASPECT_RATIO_SAMPLE_VIDEOS', 'ASPECT_RATIO_PARAMS',
    'AVATAR_DATA', 'AVATAR_EXAMPLES', 'AVATAR_PARAMS',
    'BADGE_DATA', 'BADGE_EXAMPLES', 'BADGE_PARAMS',
    'BREADCRUMB_DATA', 'BREADCRUMB_ITEMS', 'BREADCRUMB_PARAMS',
    'CALENDAR_DATA', 'CALENDAR_EVENTS', 'CALENDAR_PARAMS',
    'CHECKBOX_DATA', 'CHECKBOX_PARAMS',
    'PROGRESS_DATA', 'PROGRESS_PARAMS',
    'RADIO_GROUP_OPTIONS', 'RADIO_GROUP_DATA', 'RADIO_GROUP_PARAMS',
    'SWITCH_DATA', 'SWITCH_PARAMS',
    'TABS_DATA', 'TABS_PARAMS',
    'COLLAPSIBLE_DATA', 'COLLAPSIBLE_PARAMS',
    'ALERT_DIALOG_DATA',
    'LABEL_DATA', 'LABEL_EXAMPLES', 'LABEL_PARAMS',
    'SEPARATOR_DATA', 'SEPARATOR_EXAMPLES', 'SEPARATOR_PARAMS',
    'SKELETON_DATA', 'SKELETON_EXAMPLES', 'SKELETON_PARAMS',
    'SPINNER_DATA', 'SPINNER_EXAMPLES', 'SPINNER_PARAMS',
    'TOGGLE_DATA', 'TOGGLE_EXAMPLES', 'TOGGLE_PARAMS',
    'TOOLTIP_DATA', 'TOOLTIP_EXAMPLES', 'TOOLTIP_PARAMS',
    'COMPONENT_DATA',
] 