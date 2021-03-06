from . import general_weapon_functions
import random

def generate(rarity):
    # 5 launcher manufacturers

    body_manufacturer = choose_launcher_part_manufacturer()

    if rarity == 'E-Tech':
        while True:
            if body_manufacturer == 'Torgue':
                # Can't have a Torgue E-Tech launcher, roll again
                # to get another launcher manufacturer
                print("Torgue E-Tech launcher, roll again")
                body_manufacturer = choose_launcher_part_manufacturer()
            else:
                break

    if rarity == 'E-Tech':
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_launcher_part_manufacturer()

    grip_manufacturer = choose_launcher_part_manufacturer()
    scope_manufacturer = choose_launcher_part_manufacturer()
    exhaust_manufacturer = choose_launcher_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'exhaust': exhaust_manufacturer

    }

    return weapon_parts

def choose_launcher_part_manufacturer():
    manufacturers = ['Bandit', 'Maliwan', 'Tediore', 'Torgue', 'Vladof']
    return random.choice(manufacturers)

def is_manufacturer_element_combo_valid(manufacturer, element):

    # Launchers have slightly different rules for manufacturer-element combos,
    # namely that some manufacturers can have explosive elemental launchers, so
    # the following checks are used to override the usual rules specified in
    # is_general_manufacturer_element_combo_valid in general_weapon_functions.py

    if manufacturer == 'Bandit' or manufacturer == 'Torgue':
        is_valid = element == 'Explosion'
    elif manufacturer == 'Maliwan':
        is_valid = (element != 'None' and element != 'Explosion')
    else:
        is_valid = element != 'None'

    return is_valid

def choose_accessory():
    accessories = [
        'magazine_size',
        'accuracy',
        'melee',
        'reload_speed',
        'weapon_swap_speed',
        'rocket_speed',
        'fire_rate',
        'damage'
    ]
    return random.choice(accessories)

def choose_element(weapon_manufacturer):
    if weapon_manufacturer == 'Torgue' or weapon_manufacturer == 'Bandit':
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
