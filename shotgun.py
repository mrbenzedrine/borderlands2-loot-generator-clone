import general_weapon_functions
import random

def generate_shotgun(rarity):
    # 5 shotgun manufacturers

    body_manufacturer = choose_shotgun_part_manufacturer()
    barrel_manufacturer = choose_shotgun_part_manufacturer()
    grip_manufacturer = choose_shotgun_part_manufacturer()
    scope_manufacturer = choose_shotgun_part_manufacturer()
    stock_manufacturer = choose_shotgun_part_manufacturer()

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
        if (general_weapon_functions.is_general_weapon_element_combo_valid('shotgun', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Shotgun is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Shotgun is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the shotgun should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_shotgun_accessory()
    else:
        weapon_accessory = 'none'

    weapon_stuff = {

        'weapon_type': 'shotgun',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory

    }

    return weapon_stuff

def choose_shotgun_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Hyperion',
        2: 'Jakobs',
        3: 'Tediore',
        4: 'Torgue'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Only Torgue shotguns can be explosive

    valid_combination = True

    if(element == 'Explosion'):
        valid_combination = (manufacturer == 'Torgue')

    return valid_combination    

def choose_shotgun_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'melee',
        1: 'magazine_size',
        2: 'projectile_count',
        3: 'bullet_speed',
        4: 'critical_damage',
        5: 'reload_speed',
        6: 'stability'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of a shotgun

weapon_names = {
    
    'prefix': {

    },

    'title': {

        'Bandit': {
            'Bandit': 'Room Clener',
            'Hyperion': 'longer ragne killer',
            'Jakobs': 'Stret Sweper',
            'Tediore': 'Skatergun',
            'Torgue': 'oberkil!',
            'E-Tech': 'SPlasher Blashter'
        },

        'Hyperion': {
            'Bandit': 'Crowdsourcing',
            'Hyperion': 'Thinking',
            'Jakobs': 'Face Time',
            'Tediore': 'Projectile Diversification',
            'Torgue': 'Development',
            'E-Tech': 'Splatgun'
        },

        'Jakobs': {
            'Bandit': 'Bushwack',
            'Hyperion': 'Longrider',
            'Jakobs': 'Coach Gun',
            'Tediore': 'Scattergun',
            'Torgue': 'Quad',
            'E-Tech': 'Nothing'
        },

        'Tediore': {
            'Bandit': 'Triple Barrels!',
            'Hyperion': 'Sportsman',
            'Jakobs': 'Double Barrels!',
            'Tediore': 'Home Security',
            'Torgue': 'Shotgun Supreme!!',
            'E-Tech': 'Splatgun'
        },

        'Torgue': {
            'Bandit': 'Hulk',
            'Hyperion': 'Stalker',
            'Jakobs': 'Pounder',
            'Tediore': 'Bangstick',
            'Torgue': 'Ravager',
            'E-Tech': 'Nothing'
        }

    }

}