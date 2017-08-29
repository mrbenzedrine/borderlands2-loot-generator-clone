import general_weapon_functions
import random

def generate_launcher():
    # 5 launcher manufacturers

    body_random_integer = random.randint(0,4)
    barrel_random_integer = random.randint(0,4)
    grip_random_integer = random.randint(0,4)
    scope_random_integer = random.randint(0,4)
    exhaust_random_integer = random.randint(0,4)

    body_manufacturer = choose_launcher_part_manufacturer(body_random_integer)
    barrel_manufacturer = choose_launcher_part_manufacturer(barrel_random_integer)
    grip_manufacturer = choose_launcher_part_manufacturer(grip_random_integer)
    scope_manufacturer = choose_launcher_part_manufacturer(scope_random_integer)
    exhaust_manufacturer = choose_launcher_part_manufacturer(exhaust_random_integer)

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'exhaust': exhaust_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    # Now note that Torgue and Bandit launchers can be explosive only,
    # Maliwan CAN'T be explosive, and both Tediore and Vladof can be
    # any element

    if(weapon_overall_manufacturer == 'Torgue' or weapon_overall_manufacturer == 'Bandit'):
        weapon_element = 'Explosion'
    else:
        weapon_element_random_integer = random.randint(0, 5)
        weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('launcher', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Launcher is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Launcher is ", weapon_element)
            weapon_element_random_integer = random.randint(0, 5)
            weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    weapon_stuff = {

        'weapon_type': 'launcher',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title

    }

    return weapon_stuff

def choose_launcher_part_manufacturer(integer):
    switcher = {
        0: 'Bandit',
        1: 'Maliwan',
        2: 'Tediore',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Torgue and Bandit launchers can be explosive only,
    # Maliwan CAN'T be explosive, and both Tediore and Vladof can be
    # any element apart from non-elemental

    test_1 = True
    test_2 = True
    test_3 = True

    if(manufacturer == 'Torgue' or manufacturer == 'Bandit'):
        test_1 = (element == 'Explosion')
    elif(manufacturer == 'Maliwan'):
        test_2 = (element != 'Explosion' and element != 'None')
    elif(manufacturer == 'Tediore' or manufacturer == 'Tediore'):
        test_3 = (element != 'None')

    valid_combination = test_1 and test_2 and test_3

    return valid_combination

# Dictionary containing the different possibilities for the Prefix and
# Title of a launcher

weapon_names = {
    
    'prefix': {

    },

    'title': {

        'Bandit': {
            'Bandit': 'Launcher',
            'Maliwan': 'area efect',
            'Tediore': 'Launcher',
            'Torgue': 'Zooka!',
            'Vladof': 'bombabarbardeer',
            'E-Tech': 'PRAZMA CANON'
        },

        'Maliwan': {
            'Bandit': 'Projectile',
            'Maliwan': 'Panorama',
            'Tediore': 'Projectile',
            'Torgue': 'Punishment',
            'Vladof': 'Prowler',
            'E-Tech': 'PBFG'
        },

        'Tediore': {
            'Bandit': 'Launcher',
            'Maliwan': 'Spread',
            'Tediore': 'Launcher',
            'Torgue': 'Bazooka',
            'Vladof': 'Dispatch',
            'E-Tech': 'Launcher'
        },

        'Torgue': {
            'Bandit': 'boom',
            'Maliwan': 'Blaaa',
            'Tediore': 'boom',
            'Torgue': 'Duuurp!',
            'Vladof': 'Deee!',
            'E-Tech': 'Nothing'
        },

        'Vladof': {
            'Bandit': 'RPG',
            'Maliwan': 'Glory',
            'Tediore': 'RPG',
            'Torgue': 'Hero',
            'Vladof': 'Vanquisher',
            'E-Tech': 'Topneaa'
        }

    }

}