import random

from gear.grenade_mods.grenade_mod import *

def generate(rarity, level):

    # rarity: string, requested rarity of grenade

    # level: integer representing either the level of the enemy that
    # dropped the grenade, or level of the area in which the chest 
    # that the grenade was found in

    grenade_mod_type = choose_grenade_mod_type()
    grenade_mod_manufacturer = get_grenade_mod_manufacturer(grenade_mod_type)
    grenade_mod_delivery_mechanism = choose_delivery_mechanism()

    # Generate element of grenade

    if(grenade_mod_type == 'mirv'):
        # All MIRV grenades can only be explosive
        grenade_mod_element = 'Explosive'
    else:
        grenade_mod_element = choose_element()

        # Now check if grenade type and element combo is valid

        while True:
            print("%s is %s" % (grenade_mod_type, grenade_mod_element))
            if(check_valid_type_element_combo(grenade_mod_type, grenade_mod_element) is True):
                print("Valid grenade type element combo")
                break
            else:
                print("Invalid grenade type element combo")
                grenade_mod_element = choose_element()

    GrenadeModClass = get_grenade_mod_type_class(grenade_mod_type)

    return GrenadeModClass(level, rarity, grenade_mod_manufacturer, grenade_mod_element, grenade_mod_delivery_mechanism)


def choose_grenade_mod_type():
    random_integer = random.randint(0, 5)
    switcher = {
        0: 'standard',
        1: 'area_of_effect',
        2: 'bouncing_betty',
        3: 'transfusion',
        4: 'mirv',
        5: 'singularity'
    }
    return switcher.get(random_integer, 'nothing')

def get_grenade_mod_manufacturer(grenade_mod_type):
    switcher = {
        'standard': choose_standard_manufacturer(),
        'area_of_effect': 'Vladof',
        'bouncing_betty': choose_bouncing_betty_manufacturer(),
        'transfusion': 'Maliwan',
        'mirv': choose_mirv_manufacturer(),
        'singularity': 'Hyperion'
    }
    return switcher.get(grenade_mod_type, 'nothing')

def choose_standard_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Tediore'
    }
    return switcher.get(random_integer, 'nothing')

def choose_bouncing_betty_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Dahl'
    }
    return switcher.get(random_integer, 'nothing')

def choose_mirv_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Torgue'
    }
    return switcher.get(random_integer, 'nothing')

def get_grenade_mod_type_class(grenade_mod_type):
    switcher = {
        'standard': GrenadeMod,
        'area_of_effect': AreaOfEffect,
        'bouncing_betty': BouncingBetty,
        'transfusion': Transfusion,
        'mirv': MIRV,
        'singularity': Singularity
    }
    return switcher.get(grenade_mod_type, 'nothing')

def choose_delivery_mechanism():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'Lobbed',
        1: 'Lobbed Sticky',
        2: 'Homing',
        3: 'Homing Sticky',
        4: 'Longbow',
        5: 'Longbow Sticky',
        6: 'Rubberised'
    }
    return switcher.get(random_integer, 'nothing')

def choose_element():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Incendiary',
        1: 'Corrosion',
        2: 'Explosion',
        3: 'Shock',
        4: 'Slag'
    }
    return switcher.get(random_integer, "nothing")

def check_valid_type_element_combo(grenade_mod_type, element):

    test_1 = True

    if(grenade_mod_type == 'area_of_effect'):
        test_1 = (element != 'Slag' and element != 'Explosion')

    return test_1
