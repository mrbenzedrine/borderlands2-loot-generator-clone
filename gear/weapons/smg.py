from . import general_weapon_functions
import random

def generate(rarity):
    # There are 5 smg manuafcturers

    body_manufacturer = choose_smg_part_manufacturer()

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
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

    return weapon_parts


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

def choose_accessory():
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

def choose_element(weapon_manufacturer):
    # No Jakobs or Torgue smgs exist, so there are no manufacturer specific
    # elements that can be set prior to the random generation of an
    # element

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
