import random

from gear.grenade_mods.grenade_mod import GrenadeMod
from gear.grenade_mods import area_of_effect
from gear.grenade_mods import bouncing_betty
from gear.grenade_mods import mirv
from gear.grenade_mods import singularity
from gear.grenade_mods import standard
from gear.grenade_mods import transfusion

def generate(rarity, level):

    # rarity: string, requested rarity of grenade

    # level: integer representing either the level of the enemy that
    # dropped the grenade, or level of the area in which the chest 
    # that the grenade was found in

    grenade_mod_type = choose_grenade_mod_type()
    grenade_mod_manufacturer = get_grenade_mod_manufacturer(grenade_mod_type)

    grenade_mod_type_generation_module = get_grenade_mod_type_generation_module(grenade_mod_type)
    grenade_mod_stats = {
        'main_stats': grenade_mod_type_generation_module.calculate_main_stats(level, rarity),
        'other_stats': grenade_mod_type_generation_module.generate_other_stats(),
        'type_specific_stats': grenade_mod_type_generation_module.calculate_type_specific_stats(level, rarity)
    }

    return GrenadeMod(level, rarity, grenade_mod_type, grenade_mod_stats, grenade_mod_manufacturer)


def choose_grenade_mod_type():
    random_integer = random.randint(0, 5)
    switcher = {
        0: 'standard',
        1: 'area_of_effect',
        2: 'bouncing_betty',
        3: 'transfusion',
        4: 'mirv',
        5: 'singularity'
    }
    return switcher.get(random_integer, 'nothing')

def get_grenade_mod_manufacturer(grenade_mod_type):
    switcher = {
        'standard': choose_standard_manufacturer(),
        'area_of_effect': 'Vladof',
        'bouncing_betty': choose_bouncing_betty_manufacturer(),
        'transfusion': 'Maliwan',
        'mirv': choose_mirv_manufacturer(),
        'singularity': 'Hyperion'
    }
    return switcher.get(grenade_mod_type, 'nothing')

def choose_standard_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Tediore'
    }
    return switcher.get(random_integer, 'nothing')

def choose_bouncing_betty_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Dahl'
    }
    return switcher.get(random_integer, 'nothing')

def choose_mirv_manufacturer():
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Bandit',
        1: 'Torgue'
    }
    return switcher.get(random_integer, 'nothing')

def get_grenade_mod_type_generation_module(grenade_mod_type):
    switcher = {
        'area_of_effect': area_of_effect,
        'bouncing_betty': bouncing_betty,
        'mirv': mirv,
        'singularity': singularity,
        'standard': standard,
        'transfusion': transfusion
    }
    return switcher.get(grenade_mod_type, 'nothing')
