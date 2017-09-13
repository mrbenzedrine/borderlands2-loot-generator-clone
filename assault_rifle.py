import general_weapon_functions
import random

def generate_assault_rifle(rarity):
    # 5 assault rifle manufacturers

    body_manufacturer = choose_assault_rifle_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a Torgue or Jakobs E-Tech assault rifle, 
                # roll again
                print("Torgue or Jakobs E-Tech assault rifle, roll again")
                body_manufacturer = choose_assault_rifle_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_assault_rifle_part_manufacturer()

    grip_manufacturer = choose_assault_rifle_part_manufacturer()
    scope_manufacturer = choose_assault_rifle_part_manufacturer()
    stock_manufacturer = choose_assault_rifle_part_manufacturer()

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
    elif(weapon_overall_manufacturer == 'Torgue'):
        weapon_element = 'Explosion'
    else:
        weapon_element = general_weapon_functions.choose_weapon_element()
 
    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('assault_rifle', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("Assualt rifle is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Assault rifle is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the assault rifle should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_assault_rifle_accessory()
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'assault_rifle',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name
        
    }

    return weapon_stuff    



def choose_assault_rifle_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Jakobs',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Only Torgue assault rifles can be explosive

    test_1 = True
    test_2 = True

    if(rarity != 'E-Tech'):
        if(element == 'Explosion'):
            test_1 = (manufacturer == 'Torgue')
    elif(rarity == 'E-Tech'):
        test_2 = (element != 'None' and element != 'Explosion')

    return test_1 and test_2    

def choose_assault_rifle_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'damage',
        1: 'fire_rate',
        2: 'melee',
        3: 'bullet_speed',
        4: 'stability',
        5: 'magazine_size',
        6: 'accuracy'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of an assualt rifle

weapon_names = {
    
    'prefix': {

        'Bandit': {
            'damage': 'Nassty',
            'fire_rate': 'Wyld Asss',
            'melee': 'Nifed',
            'bullet_speed': 'Fast Bulets',
            'stability': 'Taktikal',
            'magazine_size': 'Expandifide',
            'accuracy': 'Akurate'
        },

        'Dahl': {
            'damage': 'Attack',
            'fire_rate': 'Feral',
            'melee': 'Breach',
            'bullet_speed': 'Deep',
            'stability': 'Patrol',
            'magazine_size': 'Onslaught',
            'accuracy': 'Scout'
        },

        'Jakobs': {
            'damage': 'Boss',
            'fire_rate': 'Wild',
            'melee': 'Razor',
            'bullet_speed': 'Cowboy',
            'stability': 'Horse',
            'magazine_size': 'Flush',
            'accuracy': 'Deadshot'
        },

        'Torgue': {
            'damage': 'Nasty',
            'fire_rate': 'Wild',
            'melee': 'Stabbing',
            'bullet_speed': 'Slipper',
            'stability': 'Rhythmic',
            'magazine_size': 'Plump',
            'accuracy': 'Rigorous'
        },

        'Vladof': {
            'damage': 'Ferocious',
            'fire_rate': 'Rabid',
            'melee': 'Skewering',
            'bullet_speed': 'Swift',
            'stability': 'Resolute',
            'magazine_size': 'Expansive',
            'accuracy': 'Severe'
        }
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