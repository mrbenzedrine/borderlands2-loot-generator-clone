from . import general_weapon_functions
import random

def generate(rarity):
    # 5 shotgun manufacturers

    body_manufacturer = choose_shotgun_part_manufacturer()

    if rarity == 'E-Tech':
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a NON-UNIQUE Torgue or Jakobs E-Tech shotgun, 
                # roll again
                print("Torgue or Jakobs E-Tech shotgun, roll again")
                body_manufacturer = choose_shotgun_part_manufacturer()
            else:
                break

    if rarity == 'E-Tech':
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

    return weapon_parts

def choose_shotgun_part_manufacturer():
    manufacturers = ['Bandit', 'Hyperion', 'Jakobs', 'Tediore', 'Torgue']
    return random.choice(manufacturers)

def choose_accessory():
    accessories = [
        'melee',
        'magazine_size',
        'projectile_count',
        'bullet_speed',
        'critical_damage',
        'reload_speed',
        'stability'
    ]
    return random.choice(accessories)

def choose_element(weapon_manufacturer):
    if weapon_manufacturer == 'Jakobs':
        weapon_element = 'None'
    elif weapon_manufacturer == 'Torgue':
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
