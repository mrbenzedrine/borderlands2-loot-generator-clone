import general_weapon_functions
import random

def generate_sniper_rifle():
    # 5 sniper rifle manufacturers

    body_random_integer = random.randint(0,4)
    barrel_random_integer = random.randint(0,4)
    grip_random_integer = random.randint(0,4)
    scope_random_integer = random.randint(0,4)

    body_manufacturer = choose_sniper_rifle_part_manufacturer(body_random_integer)
    barrel_manufacturer = choose_sniper_rifle_part_manufacturer(barrel_random_integer)
    grip_manufacturer = choose_sniper_rifle_part_manufacturer(grip_random_integer)
    scope_manufacturer = choose_sniper_rifle_part_manufacturer(scope_random_integer)

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    if(weapon_overall_manufacturer == 'Jakobs'):
        weapon_element = 'None'
    else:
        weapon_element_random_integer = random.randint(0, 5)
        weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('sniper_rifle', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Sniper rifle is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Sniper rifle is ", weapon_element)
            weapon_element_random_integer = random.randint(0, 5)
            weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    weapon_stuff = {

        'weapon_type': 'sniper_rifle',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title

    }

    return weapon_stuff

def choose_sniper_rifle_part_manufacturer(integer):
    switcher = {
        0: 'Dahl',
        1: 'Hyperion',
        2: 'Jakobs',
        3: 'Maliwan',
        4: 'Vladof'
    }
    return switcher.get(integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Jakobs must be non-elemental, and also Maliwan must be elemental,
    # but not explosive

    test_1 = True
    test_2 = True

    if(manufacturer == 'Jakobs'):
        test_1 = (element == 'None')
    elif(manufacturer == 'Maliwan'):
        test_2 = (element != 'None')

    valid_combination = test_1 and test_2

    return valid_combination

# Dictionary containing the different possibilities for the Prefix and
# Title of a sniper rifle

weapon_names = {
    
    'prefix': {

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