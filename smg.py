import general_weapon_functions
import random

def generate_smg(rarity):
    # There are 5 smg manuafcturers

    body_manufacturer = choose_smg_part_manufacturer()
    barrel_manufacturer = choose_smg_part_manufacturer()
    grip_manufacturer = choose_smg_part_manufacturer()
    scope_manufacturer = choose_smg_part_manufacturer()
    stock_manufacturer = choose_smg_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'stock': stock_manufacturer

    }

    weapon_overall_manufacturer = body_manufacturer

    # No Jakobs or Torgue smgs exist, so there are no manufacturer specific
    # elements that can be set prior to the random generation of an
    # element

    weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('smg', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("SMG is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("SMG is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    # There are different Maliwan Titles for the different elements, so 
    # have an if statement checking whether the barrel is manufactured
    # by Maliwan to then know to have a slightly different way of
    # assigning the Title of the weapon

    if(barrel_manufacturer == 'Maliwan'):
        weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer][weapon_element]
    else:
        weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the smg should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_smg_accessory()
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = '' # not sure what to put if there is no prefix,
        # so just put an empty string in for now

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'smg',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name

    }

    return weapon_stuff


def choose_smg_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Hyperion',
        3: 'Maliwan',
        4: 'Tediore'
    }
    return switcher.get(random_integer, 'nothing')


def is_manufacturer_element_combo_valid(manufacturer, element):
    # Maliwan smg's MUST be elemental

    valid_combination = True

    if(manufacturer == 'Maliwan'):
        valid_combination = (element != 'None')

    return valid_combination

def choose_smg_accessory():
    # The attribute values describe the stat of the gun that is increased
    # by the corresponding accessory
    random_integer = random.randint(0,5)
    switcher = {
        0: 'melee',
        1: 'accuracy',
        2: 'damage',
        3: 'bullet_speed',
        4: 'stability',
        5: 'reload_speed'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of an SMG

weapon_names = {
    
    'prefix': {

        'Bandit': {
            'melee': 'Cuting',
            'accuracy': 'Akurate',
            'damage': 'Murdering',
            'bullet_speed': 'Bulets Go Fasterified',
            'stability': 'Ballanced',
            'reload_speed': 'Agresive'
        },

        'Dahl': {
            'melee': 'Bladed',
            'accuracy': 'Deft',
            'damage': 'Stopping',
            'bullet_speed': 'Flying',
            'stability': 'Stoic',
            'reload_speed': 'Skirmish'
        },

        'Hyperion': {
            'melee': 'Cutting Edge',
            'accuracy': 'Analytical',
            'damage': 'Rightsizing',
            'bullet_speed': 'Proactive',
            'stability': 'Corporate',
            'reload_speed': 'Social'
        },

        'Maliwan': {
            'melee': 'Acuminious',
            'accuracy': 'Guieless',
            'damage': 'Consumate',
            'bullet_speed': 'Impetuous',
            'stability': 'Lucid',
            'reload_speed': 'Apt'
        },

        'Tediore': {
            'melee': 'Perma-Sharp',
            'accuracy': 'Guaranteed',
            'damage': 'Hefty',
            'bullet_speed': 'Brisk',
            'stability': 'Quality',
            'reload_speed': 'Refill'
        }
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