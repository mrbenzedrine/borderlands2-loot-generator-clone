from . import general_shield_functions

def calculate_main_stats(level, rarity):

    main_stats = {
        'capacity': 0,
        'recharge_rate': 0,
        'recharge_delay': 0
    }

    return main_stats

def calculate_type_specific_stats(level, rarity, manufacturer):

    if(manufacturer == 'Torgue'):
        nova_element = 'Explosion'
    else:
        nova_element = general_shield_functions.choose_element()

    # Check if the element and the manufacturer are a valid combination

    valid_nova_element = general_shield_functions.get_valid_nova_spike_manufacturer_element_combo(manufacturer, nova_element, 'nova')

    return {
        'element': valid_nova_element,
        'nova_radius': 0,
        'nova_damage': 0
    }
