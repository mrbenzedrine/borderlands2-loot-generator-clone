import random
from gun import Gun

import pistol
import smg
import assault_rifle
import shotgun
import sniper_rifle
import launcher

# Next cool thing would be to have different types of enemies which
# then call generate_weapon() depending on their badass ranking,
# ie, have super badasses drop a certain numebr of whatever guns

# Oh, and also start doing shields, grenades etc

# Could introduce the naming convention when I'm feeling like not
# thinking too hard =P

# Also, I'm gonna have to think about how to introduce the 
# limitations of the gun depending on the manufacturer; ie,
# torgue weapons are only explosive, the bandit manufacturer
# doesn't manufacture sniper rifles etc
# Perhaps you first generate the manufacturer of the parts BEFORE
# you generate the weapon type, and then there are separate function
# for generating bandit, dahl weapons etc because then there'll
# be differences in the number of choices you have for WHAT weapon
# types they can be and also WHICH weapon types are available for 
# each manufacturer

# Another limitation is that the manufacturer can be E-Tech only if
# the gun is Purple rarity I think right?

# Dunno how to handle E-Tech weapons yet since I don;t understand
# how they work =P

def generate_weapon(rarity, level):

    # rarity: string telling us what the rarity of the generated 
    # gun should be

    # level: integer; either the level of the enemy that dropped
    # the item or the level of the area in which the chest that
    # the item was found in was

    # Need to generate the following things:

    # The weapon type, ie, pistol, smg etc, and then, based on that:
    
    # 4 manufacturers; 1 for each different part of the weapon

    # The level for the weapon, somehow based on the given info
    # about the level of the enemy / area the weaon was dropped

    # The element of the gun



    # There are 6 weapon types, so choose a random number between
    # 0 and 5

    weapon_type_random_integer = random.randint(0, 5)
    weapon_type = choose_weapon_type(weapon_type_random_integer)

    weapon_stuff = generate_weapon_type(weapon_type)()

    print(weapon_stuff)

    return Gun(weapon_type, weapon_stuff['weapon_parts'], rarity, weapon_stuff['weapon_element'], level, weapon_stuff['weapon_title'])


def choose_weapon_type(integer):
  switcher = {
      0: 'pistol',
      1: 'smg',
      2: 'assualt_rifle',
      3: 'sniper_rifle',
      4: 'shotgun',
      5: 'launcher'
  }
  return switcher.get(integer, "nothing")

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