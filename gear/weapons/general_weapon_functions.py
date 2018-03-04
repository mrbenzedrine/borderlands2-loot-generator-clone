import random

def choose_weapon_element():
    elements = [
        'None',
        'Incendiary',
        'Corrosion',
        'Explosion',
        'Shock',
        'Slag'
    ]
    return random.choice(elements)

def is_general_weapon_element_combo_valid(weapon_type, weapon_element):

    # The only universal limitations on weapon-element combos for all
    # manufacturers is that smg's and sniper rifle can't be explosive, and
    # a launcher can't be non elemental

    test_1 = True
    test_2 = True

    if weapon_element == "Explosion":
        test_1 = (weapon_type == "launcher" or weapon_type == 'shotgun' or weapon_type == 'pistol' or weapon_type == 'assault_rifle')
    
    if weapon_type == 'launcher':
        test_2 = (weapon_element != "None")

    return test_1 and test_2

def green_blue_rarity_spawn_with_accessory():
    # Green and blue rarity weapons have a chance to spawn with an
    # accessory; don't know the exact probability currently so just
    # set it to 1/3 for now

    spawn_with_accesory_chance = random.randint(0,2)

    if spawn_with_accesory_chance == 0:
        spawn_with_accesory = True
    else:
        spawn_with_accesory = False

    return spawn_with_accesory

def is_rarity_element_combo_valid(rarity, element):

    # E-Tech rarity weapons cannot be non-elemental or explosive

    if rarity != 'E-Tech':
        is_valid = True
    else:
        is_valid = (element != 'None' and element != 'Explosion')

    return is_valid

def is_general_manufacturer_element_combo_valid(manufacturer, element):

    if manufacturer == 'Torgue':
        is_valid = element == 'Explosion'
    elif manufacturer == 'Maliwan':
        is_valid = (element != 'None' and element != 'Explosion')
    elif manufacturer == 'Jakobs':
        is_valid = element == 'None'
    else:
        is_valid = element != 'Explosion'

    return is_valid
