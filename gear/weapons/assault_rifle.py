from . import general_weapon_functions
import random

def generate(rarity):
    # 5 assault rifle manufacturers

    body_manufacturer = choose_assault_rifle_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a Torgue or Jakobs E-Tech assault rifle, 
                # roll again
                print("Torgue or Jakobs E-Tech assault rifle, roll again")
                body_manufacturer = choose_assault_rifle_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
        barrel_manufacturer = 'E-Tech'
    else:
        barrel_manufacturer = choose_assault_rifle_part_manufacturer()

    grip_manufacturer = choose_assault_rifle_part_manufacturer()
    scope_manufacturer = choose_assault_rifle_part_manufacturer()
    stock_manufacturer = choose_assault_rifle_part_manufacturer()

    weapon_parts = {

        'body': body_manufacturer,
        'barrel': barrel_manufacturer,
        'grip': grip_manufacturer,
        'scope': scope_manufacturer,
        'stock': stock_manufacturer

    }

    return weapon_parts    



def choose_assault_rifle_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Dahl',
        2: 'Jakobs',
        3: 'Torgue',
        4: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Only Torgue assault rifles can be explosive

    test_1 = True
    test_2 = True

    if(rarity != 'E-Tech'):
        if(element == 'Explosion'):
            test_1 = (manufacturer == 'Torgue')
    elif(rarity == 'E-Tech'):
        test_2 = (element != 'None' and element != 'Explosion')

    return test_1 and test_2    

def choose_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'damage',
        1: 'fire_rate',
        2: 'melee',
        3: 'bullet_speed',
        4: 'stability',
        5: 'magazine_size',
        6: 'accuracy'
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
