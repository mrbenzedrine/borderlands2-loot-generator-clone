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
    manufacturers = ['Bandit', 'Dahl', 'Hyperion', 'Maliwan', 'Tediore']
    return random.choice(manufacturers)

def choose_accessory():
    accessories = [
        'melee',
        'accuracy',
        'damage',
        'bullet_speed',
        'stability',
        'reload_speed'
    ]
    return random.choice(accessories)

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
