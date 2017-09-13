import general_weapon_functions
import random

def generate_sniper_rifle(rarity):
    # 5 sniper rifle manufacturers

    body_manufacturer = choose_sniper_rifle_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Jakobs':
                # Can't have a Jakobs E-Tech sniper rifle, roll again
                print("Jakobs E-Tech sniper rifle, roll again")
                body_manufacturer = choose_sniper_rifle_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_sniper_rifle_part_manufacturer()

    grip_manufacturer = choose_sniper_rifle_part_manufacturer()
    scope_manufacturer = choose_sniper_rifle_part_manufacturer()
    stock_manufacturer = choose_sniper_rifle_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'stock': stock_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    if(weapon_overall_manufacturer == 'Jakobs'):
        weapon_element = 'None'
    else:
        weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('sniper_rifle', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("Sniper rifle is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Sniper rifle is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the sniper rifle should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_sniper_rifle_accessory()
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'sniper_rifle',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name

    }

    return weapon_stuff

def choose_sniper_rifle_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Dahl',
        1: 'Hyperion',
        2: 'Jakobs',
        3: 'Maliwan',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Jakobs must be non-elemental, and also Maliwan must be elemental,
    # but not explosive

    test_1 = True
    test_2 = True
    test_3 = True

    if(rarity != 'E-Tech'):
        if(manufacturer == 'Jakobs'):
            test_1 = (element == 'None')
        elif(manufacturer == 'Maliwan'):
            test_2 = (element != 'None')
    elif(rarity == 'E-Tech'):
        # No need to check for explosive sniper rifles, the check in
        # general_weapon_functions.py takes care of that
        test_3 = (element != 'None')

    valid_combination = test_1 and test_2 and test_3

    return valid_combination

def choose_sniper_rifle_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'melee',
        1: 'accuracy',
        2: 'critical_damage',
        3: 'stability',
        4: 'magazine_size',
        5: 'fire_rate',
        6: 'damage'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of a sniper rifle

weapon_names = {
    
    'prefix': {

        'Dahl': {
            'melee': 'Cartel',
            'accuracy': 'Surgical',
            'critical_damage': 'Night',
            'stability': 'Liquid',
            'magazine_size': 'Operational',
            'fire_rate': 'Suppressive',
            'damage': 'Pacifying'
        },

        'Hyperion': {
            'melee': 'Contingent',
            'accuracy': 'Longitudinal',
            'critical_damage': 'Venture',
            'stability': 'Cohesion',
            'magazine_size': 'Resource',
            'fire_rate': 'Operational',
            'damage': 'Auditing'
        },

        'Jakobs': {
            'melee': 'Ti\'kope',
            'accuracy': 'Siah-Siah',
            'critical_damage': 'Tumtum',
            'stability': 'Chikamin',
            'magazine_size': 'Hyiu',
            'fire_rate': 'Klook',
            'damage': 'Skookum'
        },

        'Maliwan': {
            'melee': 'Sublime',
            'accuracy': 'Dandy',
            'critical_damage': 'Gentleman\'s',
            'stability': 'Fashionable',
            'magazine_size': 'Monstrous',
            'fire_rate': 'Banbury',
            'damage': 'Barking'
        },

        'Vladof': {
            'melee': 'Britva',
            'accuracy': 'Zammerchat',
            'critical_damage': 'Razrez',
            'stability': 'Dobby',
            'magazine_size': 'Bolshy',
            'fire_rate': 'Skorry',
            'damage': 'Gromky'
        }

    },

    'title': {

        'Dahl': {
            'Dahl': 'Sniper',
            'Hyperion': 'Strike',
            'Jakobs': 'Terror',
            'Maliwan': 'Sniper',
            'Vladof': 'Scout',
            'E-Tech': 'Railer'
        },

        'Hyperion': {
            'Dahl': 'Sniper Rifle',
            'Hyperion': 'Transaction',
            'Jakobs': 'Policy',
            'Maliwan': 'Sniper Rifle',
            'Vladof': 'Competition',
            'E-Tech': 'Hybridification'
        },

        'Jakobs': {
            'Dahl': 'Callipeen',
            'Hyperion': 'Chinook',
            'Jakobs': 'Muckamuck',
            'Maliwan': 'Callipeen',
            'Vladof': 'Diaub',
            'E-Tech': 'Nothing'
        },

        'Maliwan': {
            'Dahl': 'Snider',
            'Hyperion': 'Jericho',
            'Jakobs': 'Corinthian',
            'Maliwan': 'Snider',
            'Vladof': 'Rakehell',
            'E-Tech': 'Railer'
        },

        'Vladof': {
            'Dahl': 'Pooshka',
            'Hyperion': 'Bratchny',
            'Jakobs': 'Horroshow',
            'Maliwan': 'Pooshka',
            'Vladof': 'Droog',
            'E-Tech': 'Moloko'        
        }
    }
}