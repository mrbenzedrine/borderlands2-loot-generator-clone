import random

def choose_weapon_element(integer):
    switcher = {
        0: "None",
        1: 'Incendiary',
        2: 'Corrosion',
        3: 'Explosion',
        4: 'Shock',
        5: 'Slag'
    }
    return switcher.get(integer, "nothing")

def is_general_weapon_element_combo_valid(weapon_type, weapon_element):

    # I think the only universal limitation for all manufacturers is that
    # smg's and sniper rifles CANNOT be explosive

    # Oh, and also that all launchers must be elemental, you can't have
    # a non-elemental launcher I don't think?


    # Lets set these True by default

    test_1 = True
    test_2 = True

    if(weapon_element == "Explosion"):
        # We get True if the weapon is a launcher or a shotgun, since
        # the only explosive weapons allowed are launchers or shotguns

        test_1 = (weapon_type == "launcher" or weapon_type == 'shotgun' or weapon_type == 'pistol' or weapon_type == 'assault_rifle')
    

    if(weapon_type == 'launcher'):
        test_2 = (weapon_element != "None")

    # Return the boolean of test_1 and test_2; if true then the weapon
    # has passed both tests and is a valid GENERAL weapon, but we must
    # still check the manufacturer specific requirements...

    # That last comment makes me think that it may sometimes take quite
    # a while to generate a valid weapon, eprhaps this effort should
    # be going to creating rules that a valid weapon is chosen, rather
    # than simply checking and then regenrating if the check fails?

    return test_1 and test_2

def green_blue_rarity_spawn_with_accessory():
    # Green and blue rarity weapons have a chance to spawn with an
    # accessory; don't know the exact probability currently so just
    # set it to 1/3 for now

    spawn_with_accesory_chance = random.randint(0,2)

    if(spawn_with_accesory_chance == 0):
        spawn_with_accesory = True
    else:
        spawn_with_accesory = False

    return spawn_with_accesory