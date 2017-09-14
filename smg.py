import general_weapon_functions
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

    weapon_overall_manufacturer = body_manufacturer

    # No Jakobs or Torgue smgs exist, so there are no manufacturer specific
    # elements that can be set prior to the random generation of an
    # element

    weapon_element = general_weapon_functions.choose_weapon_element()

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid('smg', weapon_element) and is_manufacturer_element_combo_valid(weapon_overall_manufacturer, weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("SMG is ", weapon_element)
            break
        else:
            print("Invalid weapon element combo")
            print("SMG is ", weapon_element)
            weapon_element = general_weapon_functions.choose_weapon_element()

    weapon_stuff = {

        'weapon_type': 'smg',
        'weapon_element': weapon_element,
        'weapon_parts': weapon_parts

    }

    return weapon_stuff


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


def is_manufacturer_element_combo_valid(manufacturer, element, rarity):
    # Maliwan smg's MUST be elemental

    test_1 = True
    test_2 = True

    if(rarity != 'E-Tech'):
        if(manufacturer == 'Maliwan'):
            test_1 = (element != 'None')
    elif(rarity == 'E-Tech'):
        # Not allowed non-elemental E-Tech smg's
        test_2 = (element != 'None')

    return test_1 and test_2

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