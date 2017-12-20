from . import general_weapon_functions
import random

def generate(rarity):
    # 5 sniper rifle manufacturers

    body_manufacturer = choose_sniper_rifle_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Jakobs':
                # Can't have a Jakobs E-Tech sniper rifle, roll again
                print("Jakobs E-Tech sniper rifle, roll again")
                body_manufacturer = choose_sniper_rifle_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
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
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Dahl',
        1: 'Hyperion',
        2: 'Jakobs',
        3: 'Maliwan',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def choose_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'melee',
        1: 'accuracy',
        2: 'critical_damage',
        3: 'stability',
        4: 'magazine_size',
        5: 'fire_rate',
        6: 'damage'
    }
    return switcher.get(random_integer, 'none')

def choose_element(weapon_manufacturer):
    if(weapon_manufacturer == 'Jakobs'):
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
