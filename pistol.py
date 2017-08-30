import general_weapon_functions
import random

def generate_pistol(rarity):
    # Still need to generate:

    # 4 manufacturers; 1 for each different part of the weapon
    # The element of the gun

    body_manufacturer =  choose_pistol_part_manufacturer()
    barrel_manufacturer = choose_pistol_part_manufacturer()
    grip_manufacturer = choose_pistol_part_manufacturer()
    scope_manufacturer = choose_pistol_part_manufacturer()

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
        weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('pistol', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element)) is True:
            print("Valid weapon element combo")
            print("Pistol is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Pistol is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()


    weapon_title = weapon_names['title'][weapon_overall_manufacturer][barrel_manufacturer]

    # Now check to see if the pistol should spawn with an accessory

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = choose_pistol_accessory()
    else:
        weapon_accessory = 'none'

    if(spawn_with_accessory is True):
        weapon_accessory = choose_pistol_accessory()
        weapon_prefix = weapon_names['prefix'][weapon_overall_manufacturer][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_stuff = {

        'weapon_type': 'pistol',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts,
        'weapon_title': weapon_title,
        'weapon_accessory': weapon_accessory,
        'weapon_prefix': weapon_prefix,
        'weapon_full_name': weapon_full_name

    }

    return weapon_stuff

def choose_pistol_part_manufacturer():
    random_integer = random.randint(0,7)
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
    return switcher.get(random_integer, "nothing") 
    # return the string "nothing" as the default option

def is_manufacturer_element_combo_valid(manufacturer, element):
    # Note that only Torgue pistols can be explosive, none of the
    # others can be

    valid_combination = True

    if(element == 'Explosion'):
        valid_combination = (manufacturer == 'Torgue')

    return valid_combination

def choose_pistol_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'melee',
        1: 'accuracy',
        2: 'double_bullets',
        3: 'stability',
        4: 'magazine_size',
        5: 'damage',
        6: 'fire_rate'
    }
    return switcher.get(random_integer, 'none')

# Dictionary containing the different possibilities for the Prefix and
# Title of a pistol

weapon_names = {
    
    'prefix': {

        'Bandit': {
            'melee': 'Baynaneted',
            'accuracy': 'misles',
            'double_bullets': 'Dubble',
            'stability': 'Marxmans',
            'magazine_size': 'Extendified',
            'damage': 'murduerer\'s',
            'fire_rate': 'rapider'
        },

        'Dahl': {
            'melee': 'Close Quarters',
            'accuracy': 'Floated',
            'double_bullets': 'Twin',
            'stability': 'Tactical',
            'magazine_size': 'Loaded',
            'damage': 'Neutralizing',
            'fire_rate': 'React'
        },

        'Hyperion': {
            'melee': 'Action',
            'accuracy': 'Earnest',
            'double_bullets': 'Redundant',
            'stability': 'Core',
            'magazine_size': 'Maximized',
            'damage': 'Win-Win',
            'fire_rate': 'Dynamic'
        },

        'Jakobs': {
            'melee': 'Bowie',
            'accuracy': 'Straight Shootin\'',
            'double_bullets': 'Two Fer',
            'stability': 'Gunstock',
            'magazine_size': 'Loaded',
            'damage': 'Dastardly',
            'fire_rate': 'Trick Shot'
        },

        'Maliwan': {
            'melee': 'Evisceration',
            'accuracy': 'Punctillious',
            'double_bullets': 'Binary',
            'stability': 'Elegant',
            'magazine_size': 'Surfeit',
            'damage': 'Potent',
            'fire_rate': 'Expeditious'
        },

        'Tediore': {
            'melee': 'Perma-Sharp',
            'accuracy': 'Dependable',
            'double_bullets': 'Two for One',
            'stability': 'Clean',
            'magazine_size': 'Jam Packed',
            'damage': 'Super',
            'fire_rate': 'Peppy'
        },

        'Torgue': {
            'melee': 'Thrusting',
            'accuracy': 'Explicit',
            'double_bullets': 'Double Penetrating',
            'stability': 'Stiff',
            'magazine_size': 'Crammed',
            'damage': 'Hard',
            'fire_rate': 'Intense'
        },

        'Vladof': {
            'melee': 'Patriot\'s',
            'accuracy': 'Righteous',
            'double_bullets': 'Dva',
            'stability': 'Resolute',
            'magazine_size': 'Unending',
            'damage': 'Purgin',
            'fire_rate': 'Vengeful'
        }
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