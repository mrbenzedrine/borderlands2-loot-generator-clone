from . import general_weapon_functions
import random

def generate(rarity):
    # Still need to generate:

    # 4 manufacturers; 1 for each different part of the weapon
    # The element of the gun

    body_manufacturer =  choose_pistol_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a Torgue or Jakobs E-Tech pistol, roll again
                print("Torgue or Jakobs E-Tech pistol, roll again")
                body_manufacturer = choose_pistol_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_pistol_part_manufacturer()

    grip_manufacturer = choose_pistol_part_manufacturer()
    scope_manufacturer = choose_pistol_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer

    }

    return weapon_parts

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

def choose_accessory():
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

def choose_element(weapon_manufacturer):
    if(weapon_manufacturer == 'Jakobs'):
        weapon_element = 'None'
    elif(weapon_manufacturer == 'Torgue'):
        weapon_element = 'Explosion'
    else:
        weapon_element = general_weapon_functions.choose_weapon_element()

    return weapon_element

def calculate_stats(level, rarity, parts, accessory):

    stats = {
        'damage': 0,
        'accuracy': 0,
        'fire_rate': 0,
        'reload_speed': 0,
        'magazine_size': 0
    }

    return stats
