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
from .textarea_data import TEXTAREA_DATA, TEXTAREA_PARAMS

# Novas importações dos componentes criados
from .label_data import LABEL_DATA, LABEL_EXAMPLES, LABEL_PARAMS
from .separator_data import SEPARATOR_DATA, SEPARATOR_EXAMPLES, SEPARATOR_PARAMS
from .skeleton_data import SKELETON_DATA, SKELETON_EXAMPLES, SKELETON_PARAMS
from .spinner_data import SPINNER_DATA, SPINNER_EXAMPLES, SPINNER_PARAMS
from .toggle_data import TOGGLE_DATA, TOGGLE_EXAMPLES, TOGGLE_PARAMS
from .tooltip_data import TOOLTIP_DATA, TOOLTIP_EXAMPLES, TOOLTIP_PARAMS

# Novos componentes do GRUPO 1
from .select_data import *
from .slider_data import *
from .toggle_group_data import *

# Componentes Sonner e Form
from .sonner_data import *
from .form_data import *

# Novos componentes corrigidos
from .carousel_data import CAROUSEL_DATA
from .drawer_data import DRAWER_DATA  
from .dropdown_data import DROPDOWN_DATA
from .chart_data import CHART_DATA
from .context_menu_data import CONTEXT_MENU_DATA
from .dropdown_menu_data import DROPDOWN_MENU_DATA
from .hover_card_data import HOVER_CARD_DATA
from .layout_data import LAYOUT_DATA
from .input_otp_data import INPUT_OTP_DATA
from .modal_data import MODAL_DATA
from .menubar_data import MENUBAR_DATA
from .sheet_data import SHEET_DATA
from .sidebar_data import SIDEBAR_DATA
from .navigation_menu_data import NAVIGATION_MENU_DATA
from .resizable_data import RESIZABLE_DATA
from .scroll_area_data import SCROLL_AREA_DATA

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
    'textarea': TEXTAREA_DATA,
    # Novos componentes do GRUPO 1
    'select': {
        'basic_options': select_basic_options,
        'countries': select_countries,
        'priority': select_priority,
        'status': select_status,
        'sizes': select_sizes,
        'params': select_params,
    },
    'slider': {
        'basic': slider_basic,
        'range': slider_range,
        'volume': slider_volume,
        'price': slider_price,
        'opacity': slider_opacity,
        'disabled': slider_disabled,
        'vertical': slider_vertical,
        'params': slider_params,
    },
    'toggle-group': {
        'alignment': toggle_group_alignment,
        'format': toggle_group_format,
        'size': toggle_group_size,
        'view': toggle_group_view,
        'priority': toggle_group_priority,
        'disabled': toggle_group_disabled,
        'params': toggle_group_params,
    },
    # Componentes Sonner e Form
    'sonner': {
        'basic': sonner_basic,
        'with_action': sonner_with_action,
        'permanent': sonner_permanent,
        'positions': sonner_positions,
        'special': sonner_special,
        'params': sonner_params,
    },
    'form': {
        'basic_contact': form_basic_contact,
        'register': form_register,
        'profile': form_profile,
        'settings': form_settings,
        'validation': form_validation,
        'field_types': form_field_types,
        'params': form_params,
    },
    # Novos componentes corrigidos com dados
    'carousel': {
        'basic': CAROUSEL_DATA['basic'],
        'autoplay': CAROUSEL_DATA['autoplay'],
        'simple': CAROUSEL_DATA['simple'],
        'params': CAROUSEL_DATA['params'],
    },
    'drawer': {
        'basic': DRAWER_DATA['basic'],
        'right': DRAWER_DATA['right'],
        'footer': DRAWER_DATA['footer'],
        'params': DRAWER_DATA['params'],
    },
    'dropdown': {
        'states': DROPDOWN_DATA['states'],
        'colors': DROPDOWN_DATA['colors'],
        'basic': DROPDOWN_DATA['basic'],
        'countries': DROPDOWN_DATA['countries'],
        'sizes': DROPDOWN_DATA['sizes'],
        'params': DROPDOWN_DATA['params'],
    },
    'chart': {
        'bar': CHART_DATA['bar'],
        'pie': CHART_DATA['pie'],
        'line': CHART_DATA['line'],
        'metrics': CHART_DATA['metrics'],
        'params': CHART_DATA['params'],
    },
    'context-menu': {
        'basic': CONTEXT_MENU_DATA['basic'],
        'submenu': CONTEXT_MENU_DATA['submenu'],
        'files': CONTEXT_MENU_DATA['files'],
        'params': CONTEXT_MENU_DATA['params'],
    },
    'dropdown-menu': {
        'basic': DROPDOWN_MENU_DATA['basic'],
        'user': DROPDOWN_MENU_DATA['user'],
        'submenu': DROPDOWN_MENU_DATA['submenu'],
        'notifications': DROPDOWN_MENU_DATA['notifications'],
        'params': DROPDOWN_MENU_DATA['params'],
    },
    'hover-card': {
        'basic': HOVER_CARD_DATA['basic'],
        'user': HOVER_CARD_DATA['user'],
        'product': HOVER_CARD_DATA['product'],
        'location': HOVER_CARD_DATA['location'],
        'params': HOVER_CARD_DATA['params'],
    },
    'layout': LAYOUT_DATA,
    'input-otp': INPUT_OTP_DATA,
    'modal': MODAL_DATA,
    'menubar': MENUBAR_DATA,
    'sheet': SHEET_DATA,
    'sidebar': SIDEBAR_DATA,
    'navigation-menu': NAVIGATION_MENU_DATA,
    'resizable': RESIZABLE_DATA,
    'scroll-area': SCROLL_AREA_DATA,
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
    'CAROUSEL_DATA', 'DRAWER_DATA', 'DROPDOWN_DATA', 'CHART_DATA',
    'CONTEXT_MENU_DATA', 'DROPDOWN_MENU_DATA', 'HOVER_CARD_DATA',
    'LAYOUT_DATA', 'INPUT_OTP_DATA', 'MODAL_DATA',
    'COMPONENT_DATA',
]

# Função para obter dados de um componente específico
def get_component_data(component_name):
    """Retorna os dados do componente especificado"""
    return COMPONENT_DATA.get(component_name, {})

# Função para obter parâmetros de um componente
def get_component_params(component_name):
    """Retorna os parâmetros do componente especificado"""
    data = get_component_data(component_name)
    return data.get('params', {})

# Função para obter dados de uma variação específica
def get_component_variant(component_name, variant_name):
    """Retorna os dados de uma variação específica do componente"""
    data = get_component_data(component_name)
    return data.get(variant_name, {})

# Lista de todos os componentes disponíveis
AVAILABLE_COMPONENTS = list(COMPONENT_DATA.keys()) 