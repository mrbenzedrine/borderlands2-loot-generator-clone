import general_weapon_functions
import random

def generate_pistol():
    # Still need to generate:

    # 4 manufacturers; 1 for each different part of the weapon
    # The element of the gun

    # There are 8 pistol manufacturers, hence a random integer ebwteen
    # 0 and 7

    body_random_integer = random.randint(0,7)
    barrel_random_integer = random.randint(0,7)
    grip_random_integer = random.randint(0,7)
    scope_random_integer = random.randint(0,7)

    body_manufacturer =  choose_pistol_part_manufacturer(body_random_integer)
    barrel_manufacturer = choose_pistol_part_manufacturer(barrel_random_integer)
    grip_manufacturer = choose_pistol_part_manufacturer(grip_random_integer)
    scope_manufacturer = choose_pistol_part_manufacturer(scope_random_integer)

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    if(weapon_overall_manufacturer == 'Jakobs'):
        weapon_element = 'None'
    elif(weapon_overall_manufacturer == 'Torgue'):
        weapon_element = 'Explosion'
    else:
        weapon_element_random_integer = random.randint(0, 5)
        weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('pistol', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Pistol is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Pistol is ", weapon_element)
            weapon_element_random_integer = random.randint(0, 5)
            weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)


    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    weapon_stuff = {

        'weapon_type': 'pistol',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title

    }

    return weapon_stuff

def choose_pistol_part_manufacturer(integer):
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Hyperion',
        3: 'Jakobs',
        4: 'Maliwan',
        5: 'Tediore',
        6: 'Torgue',
        7: 'Vladof'
    }
    return switcher.get(integer, "nothing") 
    # return the string "nothing" as the default option

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Note that only Torgue pistols can be explosive, none of the
    # others can be

    valid_combination = True

    if(element == 'Explosion'):
        valid_combination = (manufacturer == 'Torgue')

    return valid_combination

# Dictionary containing the different possibilities for the Prefix and
# Title of a pistol

weapon_names = {
    
    'prefix': {

    },

    'title': {
        # At this nested level, the attribute names are the overall
        # Manufacturer, and the key value is a dictionary cntaining
        # the different manufacturers for the BARREL and then the
        # corresponding Title of the gun, so we basically have pairings
        # of OVERALL manufacturer and BARREL manufacturer here

        'Bandit':{
            'Bandit': 'Pistal',
            'Dahl': 'Pistal',
            'Hyperion': 'Hed Shoter!',
            'Jakobs': 'Ass Beeter!',
            'Maliwan': 'Pistal',
            'Tediore': 'Pistal',
            'Torgue': 'Magamum!',
            'Vladof': 'Ratatater!',
            'E-Tech': 'Spiker'
        },

        'Dahl':{
            'Bandit': 'Repeater',
            'Dahl': 'Repeater',
            'Hyperion': 'Anaconda',
            'Jakobs': 'Peacemaker',
            'Maliwan': 'Repeater',
            'Tediore': 'Repeater',
            'Torgue': 'Magnum',
            'Vladof': 'Negotiator',
            # Had 2 titles for e-tech
            'E-Tech': 'Dart / Spiker'
        },

        'Hyperion': {
            'Bandit': 'Apparatus',
            'Dahl': 'Apparatus',
            'Hyperion': 'Vision',
            'Jakobs': 'Leverage',
            'Maliwan': 'Apparatus',
            'Tediore': 'Apparatus',
            'Torgue': 'Impact',
            'Vladof': 'Synergy',
            'E-Tech': 'Dart / Spiker'
        },

        'Jakobs': {
            'Bandit': 'Revolver / Wheelgun',
            'Dahl': 'Revolver / Wheelgun',
            'Hyperion': 'Longarm',
            'Jakobs': 'Iron',
            'Maliwan': 'Revolver / Wheelgun',
            'Tediore': 'Revolver / Wheelgun',
            'Torgue': 'Widowmaker',
            'Vladof': 'Pepperbox',
            # Had 2 titles for e-tech
            'E-Tech': 'Nothing'
        },

        'Maliwan': {
            'Bandit': 'Aegis',
            'Dahl': 'Aegis',
            'Hyperion': 'Phobia',
            'Jakobs': 'Torment',
            'Maliwan': 'Aegis',
            'Tediore': 'Aegis',
            'Torgue': 'Animosity',
            'Vladof': 'Umbrage',
            'E-Tech': 'Dart / Spiker'
        },

        'Tediore': {
            'Bandit': 'Handgun',
            'Dahl': 'Handgun',
            'Hyperion': 'Aimshot',
            'Jakobs': 'Power Shot',
            'Maliwan': 'Handgun',
            'Tediore': 'Handgun',
            'Torgue': 'Biggun',
            'Vladof': 'Quickshot',
            'E-Tech': 'Dart / Spiker'
        },

        'Torgue': {
            'Bandit': 'Hand Cannon',
            'Dahl': 'Hand Cannon',
            'Hyperion': 'Hole Puncher',
            'Jakobs': 'Rod',
            'Maliwan': 'Hand Cannon',
            'Tediore': 'Hand Cannon',
            'Torgue': 'Slapper',
            'Vladof': 'Injector',
            # Had 2 titles for e-tech
            'E-Tech': 'Nothing'
        },

        'Vladof': {
            'Bandit': 'TMP',
            'Dahl': 'TMP',
            'Hyperion': 'Assassin',
            'Jakobs': 'Fighter',
            'Maliwan': 'TMP',
            'Tediore': 'TMP',
            'Torgue': 'Troublemaker',
            'Vladof': 'Anarchist',
            'E-Tech': 'Dart / Spiker'
        }
    }
}