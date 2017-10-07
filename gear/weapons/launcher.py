import general_weapon_functions
import random

def generate(rarity):
    # 5 launcher manufacturers

    body_manufacturer = choose_launcher_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue':
                # Can't have a Torgue E-Tech launcher, roll again
                # to get another launcher manufacturer
                print("Torgue E-Tech launcher, roll again")
                body_manufacturer = choose_launcher_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
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
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Maliwan',
        2: 'Tediore',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Torgue and Bandit launchers can be explosive only,
    # Maliwan CAN'T be explosive, and both Tediore and Vladof can be
    # any element apart from non-elemental

    test_1 = True
    test_2 = True
    test_3 = True
    test_4 = True

    if(rarity != 'E-Tech'):
        if(manufacturer == 'Torgue' or manufacturer == 'Bandit'):
            test_1 = (element == 'Explosion')
        elif(manufacturer == 'Maliwan'):
            test_2 = (element != 'Explosion' and element != 'None')
        elif(manufacturer == 'Tediore' or manufacturer == 'Vladof'):
            test_3 = (element != 'None')
    elif(rarity == 'E-Tech'):
        test_4 = (element != 'None' and element != 'Explosion')

    valid_combination = test_1 and test_2 and test_3 and test_4

    return valid_combination

def choose_accessory():
    random_integer = random.randint(0,7)
    switcher = {
        0: 'magazine_size',
        1: 'accuracy',
        2: 'melee',
        3: 'reload_speed',
        4: 'weapon_swap_speed',
        5: 'rocket_speed',
        6: 'fire_rate',
        7: 'damage'
    }
    return switcher.get(random_integer, 'none')

def choose_element(weapon_manufacturer):
    if(weapon_manufacturer == 'Torgue' or weapon_manufacturer == 'Bandit'):
        weapon_element = 'Explosion'
    else:
        weapon_element = general_weapon_functions.choose_weapon_element()

    return weapon_element
