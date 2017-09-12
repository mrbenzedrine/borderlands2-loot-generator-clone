import random
from gun import Gun

import pistol
import smg
import assault_rifle
import shotgun
import sniper_rifle
import launcher

def generate_weapon(rarity, level):

    # rarity: string telling us what the rarity of the generated 
    # gun should be

    # level: integer; either the level of the enemy that dropped
    # the item or the level of the area in which the chest that
    # the item was found in was

    weapon_type = choose_weapon_type()

    weapon_stuff = generate_weapon_type(weapon_type)(rarity)

    print(weapon_stuff)

    return Gun(weapon_type, weapon_stuff['weapon_parts'], rarity, weapon_stuff['weapon_element'], level, weapon_stuff['weapon_title'], weapon_stuff['weapon_prefix'])


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
        'pistol': pistol.generate_pistol,
        'smg': smg.generate_smg,
        'assault_rifle': assault_rifle.generate_assault_rifle,
        'shotgun': shotgun.generate_shotgun,
        'sniper_rifle': sniper_rifle.generate_sniper_rifle,
        'launcher': launcher.generate_launcher
    }
    return switcher.get(weapon_type, "nothing")