import general_weapon_functions
import random

def generate_smg():
    # There are 5 smg manuafcturers

    body_random_integer = random.randint(0,4)
    barrel_random_integer = random.randint(0,4)
    grip_random_integer = random.randint(0,4)
    scope_random_integer = random.randint(0,4)

    body_manufacturer = choose_smg_part_manufacturer(body_random_integer)
    barrel_manufacturer = choose_smg_part_manufacturer(barrel_random_integer)
    grip_manufacturer = choose_smg_part_manufacturer(grip_random_integer)
    scope_manufacturer = choose_smg_part_manufacturer(scope_random_integer)

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    # No Jakobs or Torgue smgs exist, so there are no manufacturer specific
    # elements that can be set prior to the random generation of an
    # element

    weapon_element_random_integer = random.randint(0, 5)
    weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('smg', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("SMG is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("SMG is ", weapon_element)
            weapon_element_random_integer = random.randint(0, 5)
            weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    # There are different Maliwan Titles for the different elements, so 
    # have an if statement checking whether the barrel is manufactured
    # by Maliwan to then know to have a slightly different way of
    # assigning the Title of the weapon

    if(barrel_manufacturer == 'Maliwan'):
        weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer][weapon_element]
    else:
        weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    weapon_stuff = {

        'weapon_type': 'smg',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title

    }

    return weapon_stuff


def choose_smg_part_manufacturer(integer):
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Hyperion',
        3: 'Maliwan',
        4: 'Tediore'
    }
    return switcher.get(integer, 'nothing')


def is_manufacturer_element_combo_valid(manufacturer, element):
    # Maliwan smg's MUST be elemental

    valid_combination = True

    if(manufacturer == 'Maliwan'):
        valid_combination = (element != 'None')

    return valid_combination

# Dictionary containing the different possibilities for the Prefix and
# Title of an SMG

weapon_names = {
    
    'prefix': {

    },

    'title': {

        'Bandit': {
            'Bandit': 'smig',
            'Dahl': 'rokgun',
            'Hyperion': 'Acurate smgg',
            'Maliwan': {
                'None': 'smig',
                'Incendiary': 'Burny',
                'Shock': 'Shoky',
                'Corrosion': 'Barfy',
                'Slag': 'Slagy'
            },
            'Tediore': 'smig',
            'E-Tech': 'Plasma Caster'
        },

        'Dahl': {
            'Bandit': 'SMG',
            'Dahl': 'Fox',
            'Hyperion': 'Falcon',
            'Maliwan': {
                'None': 'SMG',
                'Incendiary': 'Beetle',
                'Shock': 'Eel',
                'Corrosion': 'Scorpion',
                'Slag': 'Jackal'
            },
            'Tediore': 'SMG',
            'E-Tech': 'Plasma Caster'
        },

        'Hyperion': {
            'Bandit': 'Projectile Comvergence',
            'Dahl': 'Presence',
            'Hyperion': 'Transmurdera',
            'Maliwan': {
                'None': 'Projectile Convergence',
                'Incendiary': 'Backburner',
                'Shock': 'Storm',
                'Corrosion': 'Weisenheimer',
                'Slag': 'Wellness'
            },
            'Tediore': 'Projectile Convergence',
            'E-Tech': 'Plasma Caster'
        },

        'Maliwan': {
            'Bandit': 'SubMalevolent Grace',
            'Dahl': 'Trance',
            'Hyperion': 'Gospel',
            'Maliwan': {
                'None': '',
                'Incendiary': 'Provacateur',
                'Shock': 'Vexation',
                'Corrosion': 'Venom',
                'Slag': 'Revenant'
            },
            'Tediore': 'SubMalevolent Grace',
            'E-Tech': 'Plasma Caster'
        },

        'Tediore': {
            'Bandit': 'Subcompact MG',
            'Dahl': 'Special',
            'Hyperion': 'Ace',
            'Maliwan': {
                'None': 'Subcompact MG',
                'Incendiary': 'Kindle',
                'Shock': 'Spark',
                'Corrosion': 'Green',
                'Slag': 'Chaff'
            },
            'Tediore': 'Subcompact MG',
            'E-Tech': 'Plasma Caster'       
        }

    }

}