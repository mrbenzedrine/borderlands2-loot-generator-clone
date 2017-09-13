import general_weapon_functions
import random

def generate_shotgun(rarity):
    # 5 shotgun manufacturers

    body_manufacturer = choose_shotgun_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a NON-UNIQUE Torgue or Jakobs E-Tech shotgun, 
                # roll again
                print("Torgue or Jakobs E-Tech shotgun, roll again")
                body_manufacturer = choose_shotgun_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
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
        if (general_weapon_functions.is_general_weapon_element_combo_valid('shotgun', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
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
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'shotgun',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name

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

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Only Torgue shotguns can be explosive

    test_1 = True
    test_2 = True

    if(rarity != 'E-Tech'):
        if(element == 'Explosion'):
            test_1 = (manufacturer == 'Torgue')
    elif(rarity == 'E-Tech'):
        # Not allowed non-elemental or explosive E-Tech shotguns
        test_2 = (element != 'None' and element != 'Explosion')

    return test_1 and test_2

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

        'Bandit': {
            'melee': 'Slising',
            'magazine_size': 'Drumed',
            'projectile_count': 'Redy Stedy',
            'bullet_speed': 'Sketer',
            'critical_damage': 'Critikal Hit',
            'reload_speed': 'Quick Loadeder',
            'stability': 'Assssult'
        },

        'Hyperion': {
            'melee': 'Restructuring',
            'magazine_size': 'Scalable',
            'projectile_count': 'Social',
            'bullet_speed': 'Potential',
            'critical_damage': 'Critical',
            'reload_speed': 'Reactive',
            'stability': 'Practicable'
        },

        'Jakobs': {
            'melee': 'Barbed',
            'magazine_size': 'Sidewinder',
            'projectile_count': 'Well Kept',
            'bullet_speed': 'Huntin\'',
            'critical_damage': 'Doc\'s',
            'reload_speed': 'Texas',
            'stability': 'Rustler\'s'
        },

        'Tediore': {
            'melee': 'Swiss',
            'magazine_size': 'Extra Large',
            'projectile_count': 'New and Improved',
            'bullet_speed': 'Original',
            'critical_damage': 'Royal',
            'reload_speed': 'Basic',
            'stability': 'Gentle'
        },

        'Torgue': {
            'melee': 'Bad Touch',
            'magazine_size': 'Desperate',
            'projectile_count': 'Sinewy',
            'bullet_speed': 'Potent',
            'critical_damage': 'Juicy',
            'reload_speed': 'Impetuous',
            'stability': 'Casual'
        }

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