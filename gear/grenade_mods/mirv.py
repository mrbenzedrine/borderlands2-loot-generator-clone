from . import general_grenade_mod_functions 

def generate(level, rarity):

    main_stats = calculate_main_stats(level, rarity)

    other_stats = {
        'element': 'Explosion',
        'delivery_mechanism': general_grenade_mod_functions.choose_delivery_mechanism()
    }

    type_specific_stats = calculate_type_specific_stats(level, rarity)

    stats = {
        'main_stats': main_stats,
        'other_stats': other_stats,
        'type_specific_stats': type_specific_stats
    }

    return stats

def calculate_main_stats(level, rarity):
    
    main_stats = {
        'damage': 0,
        'blast_radius': 0,
        'fuse_time': 0
    }

    return main_stats

def calculate_type_specific_stats(level, rarity):

    return {
        'no_of_child_grenades': 0
    }
