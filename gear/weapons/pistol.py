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

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Note that only Torgue pistols can be explosive, none of the
    # others can be

    test_1 = True
    test_2 = True
    test_3 = True
    test_4 = True

    if(rarity != 'E-Tech'):
        if(element == 'Explosion'):
            test_1 = (manufacturer == 'Torgue')
        elif(manufacturer == 'Maliwan'):
            test_4 = (element != 'None')
    elif(rarity == 'E-Tech'):
        test_2 = (element != 'Explosion')
        if(manufacturer != 'Hyperion'):
            test_3 = (element != 'None')

    return test_1 and test_2 and test_3 and test_4

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
