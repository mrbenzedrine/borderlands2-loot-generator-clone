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
        spike_element = 'Explosion'
    else:
        spike_element = general_shield_functions.choose_element()

    # Check if the element and manufacturer are a valid combination

    valid_spike_element = general_shield_functions.get_valid_nova_spike_manufacturer_element_combo(manufacturer, spike_element, 'spike')

    return {
        'element': valid_spike_element,
        'spike_damage': 0
    }
