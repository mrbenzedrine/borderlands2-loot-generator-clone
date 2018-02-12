import random
from gear.weapons.gun import Gun
import gear.weapons.general_weapon_functions as general_weapon_functions
import gear.weapons.weapon_prefixes_titles as weapon_prefixes_titles

import gear.weapons.pistol as pistol
import gear.weapons.smg as smg
import gear.weapons.assault_rifle as assault_rifle
import gear.weapons.shotgun as shotgun
import gear.weapons.sniper_rifle as sniper_rifle
import gear.weapons.launcher as launcher

def generate(rarity, level):

    # rarity: string telling us what the rarity of the generated 
    # gun should be

    # level: integer; either the level of the enemy that dropped
    # the item or the level of the area in which the chest that
    # the item was found in was

    weapon_types = ['assault_rifle', 'launcher', 'pistol', 'shotgun', 'smg', 'sniper_rifle']
    weapon_type = random.choice(weapon_types)

    weapon_module = generate_weapon_type(weapon_type)

    weapon_parts = weapon_module.generate(rarity)

    weapon_element = weapon_module.choose_element(weapon_parts['body'])

    # Now need to check validity of the weapon element combo

    while True:
        is_weapon_element_valid = general_weapon_functions.is_general_weapon_element_combo_valid(weapon_type, weapon_element)

        if weapon_type == 'launcher':
            is_manufacturer_element_valid = weapon_module.is_manufacturer_element_combo_valid(weapon_parts['body'], weapon_element)
        else:
            is_manufacturer_element_valid = general_weapon_functions.is_general_manufacturer_element_combo_valid(weapon_parts['body'], weapon_element)

        is_rarity_element_valid = general_weapon_functions.is_rarity_element_combo_valid(rarity, weapon_element)
        print("%s is %s " % (weapon_type, weapon_element))
        if is_weapon_element_valid and is_manufacturer_element_valid and is_rarity_element_valid:
            print("Valid weapon element combo")
            break
        else:
            print("Invalid weapon element combo")
            weapon_element = weapon_module.choose_element(weapon_parts['body'])


    # Maliwan smg's have a special naming case, hence the check below

    if weapon_type == 'smg' and weapon_parts['barrel'] == 'Maliwan':
        weapon_title = weapon_prefixes_titles.names['title']['smg'][weapon_parts['body']][weapon_parts['barrel']][weapon_element]
    else:
        weapon_title = weapon_prefixes_titles.names['title'][weapon_type][weapon_parts['body']][weapon_parts['barrel']]

    if rarity == 'White':
        spawn_with_accessory = False
    elif rarity == 'Green' or rarity == 'Blue':
        spawn_with_accessory = general_weapon_functions.green_blue_rarity_spawn_with_accessory()
    else:
        # Purple and above ALWAYS spawn with an accessory
        spawn_with_accessory = True

    if spawn_with_accessory is True:
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

    weapon_stats = weapon_module.calculate_stats(level, rarity, weapon_parts, weapon_accessory)

    return Gun(level, rarity, weapon_type, weapon_stats, weapon_parts, weapon_element, weapon_naming_info['weapon_title'], weapon_naming_info['weapon_prefix'])

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
