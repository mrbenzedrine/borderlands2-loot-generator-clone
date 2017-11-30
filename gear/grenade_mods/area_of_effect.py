from . import general_grenade_mod_functions 

def calculate_main_stats(level, rarity):
    
    main_stats = {
        'damage': 0,
        'blast_radius': 0,
        'fuse_time': 0
    }

    return main_stats

def generate_other_stats():

    grenade_mod_element = general_grenade_mod_functions.choose_element()

    while True:
        print("AoE grenade has element %s" % grenade_mod_element)
        if(check_valid_element(grenade_mod_element) is True):
            print("Valid AoE grenade element")
            break
        else:
            print("Invalid AoE grenade element")
            grenade_mod_element = general_grenade_mod_functions.choose_element()

    other_stats = {
        'element': grenade_mod_element,
        'delivery_mechanism': general_grenade_mod_functions.choose_delivery_mechanism()
    }

    return other_stats

def calculate_type_specific_stats(level, rarity):

    return {
        'damage_per_sec': 0
    }

def check_valid_element(element):

    # AoE grenades can't be slag or explosive

    test = (element != 'Slag' and element != 'Explosion')

    return test
