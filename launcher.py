import general_weapon_functions
import random

def generate_launcher(rarity):
    # 5 launcher manufacturers

    body_manufacturer = choose_launcher_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue':
                # Can't have a Torgue E-Tech launcher, roll again
                # to get another launcher manufacturer
                print("Torgue E-Tech launcher, roll again")
                body_manufacturer = choose_launcher_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_launcher_part_manufacturer()

    grip_manufacturer = choose_launcher_part_manufacturer()
    scope_manufacturer = choose_launcher_part_manufacturer()
    exhaust_manufacturer = choose_launcher_part_manufacturer()

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
        weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('launcher', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("Launcher is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Launcher is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the launcher should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_launcher_accessory()
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'launcher',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name

    }

    return weapon_stuff

def choose_launcher_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Maliwan',
        2: 'Tediore',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Torgue and Bandit launchers can be explosive only,
    # Maliwan CAN'T be explosive, and both Tediore and Vladof can be
    # any element apart from non-elemental

    test_1 = True
    test_2 = True
    test_3 = True
    test_4 = True

    if(rarity != 'E-Tech'):
        if(manufacturer == 'Torgue' or manufacturer == 'Bandit'):
            test_1 = (element == 'Explosion')
        elif(manufacturer == 'Maliwan'):
            test_2 = (element != 'Explosion' and element != 'None')
        elif(manufacturer == 'Tediore' or manufacturer == 'Tediore'):
            test_3 = (element != 'None')
    elif(rarity == 'E-Tech'):
        test_4 = (element != 'None' and element != 'Explosion')

    valid_combination = test_1 and test_2 and test_3 and test_4

    return valid_combination

def choose_launcher_accessory():
    random_integer = random.randint(0,7)
    switcher = {
        0: 'magazine_size',
        1: 'accuracy',
        2: 'melee',
        3: 'reload_speed',
        4: 'weapon_swap_speed',
        5: 'rocket_speed',
        6: 'fire_rate',
        7: 'damage'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of a launcher

weapon_names = {
    
    'prefix': {

        'Bandit': {
            'magazine_size': 'Roket Pawket',
            'accuracy': 'Snyper',
            'melee': 'gratuitius',
            'reload_speed': 'fast actions',
            'weapon_swap_speed': 'Quick Drawler',
            'rocket_speed': 'Speeedee',
            'fire_rate': 'Rappid',
            'damage': 'Big'
        },

        'Maliwan': {
            'magazine_size': 'Plenteous',
            'accuracy': 'Pertinenet',
            'melee': 'Proximate',
            'reload_speed': 'Prudential',
            'weapon_swap_speed': 'Parataxis',
            'rocket_speed': 'Punitory',
            'fire_rate': 'Predacious',
            'damage': 'Puissant'
        },

        'Tediore': {
            'magazine_size': 'Bonus',
            'accuracy': 'Ultraprecise',
            'melee': 'Multi-Use',
            'reload_speed': 'Stocking',
            'weapon_swap_speed': 'Swapper\'s',
            'rocket_speed': 'Rocked Speed',
            'fire_rate': 'Bustling',
            'damage': 'Large'
        },

        'Torgue': {
            'magazine_size': 'Deep a',
            'accuracy': 'gaa dunk ga',
            'melee': 'pokee doke',
            'reload_speed': 'dippity',
            'weapon_swap_speed': 'twap a',
            'rocket_speed': 'fidle dee',
            'fire_rate': 'dum pa',
            'damage': 'derp'
        },

        'Vladof': {
            'magazine_size': 'Worker\'s',
            'accuracy': 'Victorious',
            'melee': 'Revolt',
            'reload_speed': 'Ruthless',
            'weapon_swap_speed': 'Moscovite\'s',
            'rocket_speed': 'Paritisan',
            'fire_rate': 'Turbulent',
            'damage': 'Rugged'
        }

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