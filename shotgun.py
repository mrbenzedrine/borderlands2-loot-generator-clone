import general_weapon_functions
import random

def generate(rarity):
    # 5 shotgun manufacturers

    body_manufacturer = choose_shotgun_part_manufacturer()

    if(rarity == 'E-Tech'):
        while True:
            if body_manufacturer == 'Torgue' or body_manufacturer == 'Jakobs':
                # Can't have a NON-UNIQUE Torgue or Jakobs E-Tech shotgun, 
                # roll again
                print("Torgue or Jakobs E-Tech shotgun, roll again")
                body_manufacturer = choose_shotgun_part_manufacturer()
            else:
                break

    if(rarity == 'E-Tech'):
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

    weapon_overall_manufacturer = body_manufacturer

    if(weapon_overall_manufacturer == 'Jakobs'):
        weapon_element = 'None'
    elif(weapon_overall_manufacturer == 'Torgue'):
        weapon_element = 'Explosion'
    else:
        weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('shotgun', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("Shotgun is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("Shotgun is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_stuff = {

        'weapon_type': 'shotgun',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts

    }

    return weapon_stuff

def choose_shotgun_part_manufacturer():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Bandit',
        1: 'Hyperion',
        2: 'Jakobs',
        3: 'Tediore',
        4: 'Torgue'
    }
    return switcher.get(random_integer, 'nothing')

def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Only Torgue shotguns can be explosive

    test_1 = True
    test_2 = True

    if(rarity != 'E-Tech'):
        if(element == 'Explosion'):
            test_1 = (manufacturer == 'Torgue')
    elif(rarity == 'E-Tech'):
        # Not allowed non-elemental or explosive E-Tech shotguns
        test_2 = (element != 'None' and element != 'Explosion')

    return test_1 and test_2

def choose_accessory():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'melee',
        1: 'magazine_size',
        2: 'projectile_count',
        3: 'bullet_speed',
        4: 'critical_damage',
        5: 'reload_speed',
        6: 'stability'
    }
    return switcher.get(random_integer, 'none')