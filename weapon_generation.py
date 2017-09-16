import random
from gun import Gun
import general_weapon_functions
import weapon_prefixes_titles

import pistol
import smg
import assault_rifle
import shotgun
import sniper_rifle
import launcher

def generate(rarity, level):

    # rarity: string telling us what the rarity of the generated 
    # gun should be

    # level: integer; either the level of the enemy that dropped
    # the item or the level of the area in which the chest that
    # the item was found in was

    weapon_type = choose_weapon_type()

    weapon_module = generate_weapon_type(weapon_type)

    weapon_parts = weapon_module.generate(rarity)

    weapon_element = weapon_module.choose_element(weapon_parts['body'])

    # Now need to check validity of the weapon element combo

    while True:
        if (general_weapon_functions.is_general_weapon_element_combo_valid(weapon_type, weapon_element) and weapon_module.is_manufacturer_element_combo_valid(weapon_parts['body'], weapon_element, rarity)) is True:
            print("Valid weapon element combo")
            print("%s is %s " % (weapon_type, weapon_element))
            break
        else:
            print("Invalid weapon element combo")
            print("%s is %s " % (weapon_type, weapon_element))
            weapon_element = weapon_module.choose_element(weapon_parts['body'])


    # Maliwan smg's have a special naming case, hence the check below

    if(weapon_type == 'smg' and weapon_parts['barrel'] == 'Maliwan'):
        weapon_title = weapon_prefixes_titles.names['title']['smg'][weapon_parts['body']][weapon_parts['barrel']][weapon_element]
    else:
        weapon_title = weapon_prefixes_titles.names['title'][weapon_type][weapon_parts['body']][weapon_parts['barrel']]

    if(rarity == 'White'):
        spawn_with_accessory = False
    elif(rarity == 'Green' or rarity == 'Blue'):
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if(spawn_with_accessory is True):
        weapon_accessory = weapon_module.choose_accessory()
        weapon_prefix = weapon_prefixes_titles.names['prefix'][weapon_type][weapon_parts['body']][weapon_accessory]

        weapon_full_name = weapon_prefix + ' ' + weapon_title
    else:
        weapon_accessory = 'none'
        weapon_prefix = ''

        weapon_full_name = weapon_title

    weapon_naming_info = {

        'weapon_prefix': weapon_prefix,
        'weapon_title': weapon_title,
        'weapon_full_name': weapon_full_name,
        'weapon_accessory': weapon_accessory
    }

    print(weapon_parts)
    print(weapon_naming_info)

    return Gun(weapon_type, weapon_parts, rarity, weapon_element, level, weapon_naming_info['weapon_title'], weapon_naming_info['weapon_prefix'])


def choose_weapon_type():
    random_integer = random.randint(0,5)
    switcher = {
      0: 'pistol',
      1: 'smg',
      2: 'assault_rifle',
      3: 'sniper_rifle',
      4: 'shotgun',
      5: 'launcher'
    }
    return switcher.get(random_integer, "nothing")

def generate_weapon_type(weapon_type):
    switcher = {
        'pistol': pistol,
        'smg': smg,
        'assault_rifle': assault_rifle,
        'shotgun': shotgun,
        'sniper_rifle': sniper_rifle,
        'launcher': launcher
    }
    return switcher.get(weapon_type, "nothing")