from . import general_weapon_functions
import random

def generate(rarity):
    # 5 sniper rifle manufacturers

    body_manufacturer = choose_sniper_rifle_part_manufacturer()

    if rarity == 'E-Tech':
        while True:
            if body_manufacturer == 'Jakobs':
                # Can't have a Jakobs E-Tech sniper rifle, roll again
                print("Jakobs E-Tech sniper rifle, roll again")
                body_manufacturer = choose_sniper_rifle_part_manufacturer()
            else:
                break

    if rarity == 'E-Tech':
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_sniper_rifle_part_manufacturer()

    grip_manufacturer = choose_sniper_rifle_part_manufacturer()
    scope_manufacturer = choose_sniper_rifle_part_manufacturer()
    stock_manufacturer = choose_sniper_rifle_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'stock': stock_manufacturer

    }

    return weapon_parts

def choose_sniper_rifle_part_manufacturer():
    manufacturers = ['Dahl', 'Hyperion', 'Jakobs', 'Maliwan', 'Vladof']
    return random.choice(manufacturers)

def choose_accessory():
    accessories = [
        'melee',
        'accuracy',
        'critical_damage',
        'stability',
        'magazine_size',
        'fire_rate',
        'damage'
    ]
    return random.choice(accessories)

def choose_element(weapon_manufacturer):
    if weapon_manufacturer == 'Jakobs':
        weapon_element = 'None'
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
