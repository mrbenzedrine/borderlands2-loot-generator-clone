from . import general_shield_functions

def calculate_main_stats(level, rarity):

    main_stats = {
        'capacity': 0,
        'recharge_rate': 0,
        'recharge_delay': 0
    }

    return main_stats

def calculate_type_specific_stats(level, rarity):

    return {
        'element': general_shield_functions.choose_element(),
        'spike_damage': 0
    }
