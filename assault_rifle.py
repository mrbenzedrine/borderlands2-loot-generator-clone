import general_weapon_functions
import random

def generate_assault_rifle():
    # 5 assault rifle manufacturers

    body_random_integer = random.randint(0,4)
    barrel_random_integer = random.randint(0,4)
    grip_random_integer = random.randint(0,4)
    scope_random_integer = random.randint(0,4)

    body_manufacturer = choose_assault_rifle_part_manufacturer(body_random_integer)
    barrel_manufacturer = choose_assault_rifle_part_manufacturer(barrel_random_integer)
    grip_manufacturer = choose_assault_rifle_part_manufacturer(grip_random_integer)
    scope_manufacturer = choose_assault_rifle_part_manufacturer(scope_random_integer)

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
        if (general_weapon_functions.is_general_weapon_element_combo_valid('assault_rifle', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Assualt rifle is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Assault rifle is ", weapon_element)
            weapon_element_random_integer = random.randint(0, 5)
            weapon_element = general_weapon_functions.choose_weapon_element(weapon_element_random_integer)

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    weapon_stuff = {

        'weapon_type': 'assault_rifle',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title

    }

    return weapon_stuff    



def choose_assault_rifle_part_manufacturer(integer):
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Jakobs',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Only Torgue assault rifles can be explosive

    valid_combination = True

    if(element == 'Explosion'):
        valid_combination = (manufacturer == 'Torgue')

    return valid_combination    

# Dictionary containing the different possibilities for the Prefix and
# Title of an assualt rifle

weapon_names = {
    
    'prefix': {

    },

    'title': {

        'Bandit': {
            'Bandit': 'Mashine Gun',
            'Dahl': 'Carbene',
            'Jakobs': 'Ass Beeter!',
            'Torgue': 'Rokets!',
            # Seems to be 2 Vladof ones, dunno what to do, put both in
            # for now...
            'Vladof': 'Mashine Gun / Spinigun',
            'E-Tech': 'BlASSter'
        },

        'Dahl': {
            'Bandit': 'Rifle',
            'Dahl': 'Carbine',
            'Jakobs': 'Defender',
            'Torgue': 'Grenadier',
            # Seems to be 2 Vladof ones, dunno what to do, put both in
            # for now...
            'Vladof': 'Rifle / Minigun',
            'E-Tech': 'Blaster'
        },

        'Jakobs': {
            'Bandit': 'Rifle',
            'Dahl': 'Scarab',
            'Jakobs': 'Rifle',
            'Torgue': 'Cannon',
            # Seems to be 2 Vladof ones, dunno what to do, put both in
            # for now...
            'Vladof': 'Rifle / Gatling Gun',
            'E-Tech': 'Nothing'
        },

        'Torgue': {
            'Bandit': 'Rifle',
            'Dahl': 'Root',
            'Jakobs': 'Lance',
            'Torgue': 'Torpedo',
            # Seems to be 2 Vladof ones, dunno what to do, put both in
            # for now...
            'Vladof': 'Rifle / Spitter',
            'E-Tech': 'Nothing'
        },

        'Vladof': {
            'Bandit': 'Rifle',
            'Dahl': 'Renegade',
            'Jakobs': 'Guerrilla',
            'Torgue': 'Rocketeer',
            # Seems to be 2 Vladof ones, dunno what to do, put both in
            # for now...
            'Vladof': 'Rifle / Spinigun',
            'E-Tech': 'Blaster'
        }

    }

}