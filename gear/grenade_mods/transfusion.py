from . import general_grenade_mod_functions 

def calculate_main_stats(level, rarity):
    
    main_stats = {
        'damage': 0,
        'blast_radius': 0,
        'fuse_time': 0
    }

    return main_stats

def generate_other_stats():

    return {
        'element': general_grenade_mod_functions.choose_element(),
        'delivery_mechanism': general_grenade_mod_functions.choose_delivery_mechanism()
    }

def calculate_type_specific_stats(level, rarity):

    return {
        'no_of_child_grenades': 0,
        'healing_percentage': 0
    }
