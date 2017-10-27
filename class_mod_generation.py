import random

from gear.class_mods.class_mod import ClassMod

from gear.class_mods import non_dlc_class_mod_generation
from gear.class_mods import dlc_class_mod_generation

def generate(rarity, level):
    
    class_mod_character = choose_character()

    character_class_mod_generation_function = get_character_class_mod_generation_function(class_mod_character)

    class_mod_type_info = character_class_mod_generation_function()

    # Generation of class mods in Tiny Tina DLC is slightly different to
    # non-DLC class mods, so we must handle them differently

    if(not class_mod_type_info['is_dlc']):
        # White rarity class mods only change stats, they don't affect skill
        # points
        if(rarity != 'White'):
            class_mod_prefix = non_dlc_class_mod_generation.choose_prefix(class_mod_character, class_mod_type_info['type'])
            class_mod_info = {
                'prefix': class_mod_prefix,
                'stat_changes': non_dlc_class_mod_generation.calculate_stat_changes(class_mod_character, class_mod_type_info['type'], rarity, level),
                'skill_point_changes': non_dlc_class_mod_generation.calculate_skill_point_changes(class_mod_character, class_mod_type_info['type'], rarity, level, class_mod_prefix)
            }
        else:
            class_mod_prefix = 'none'
            class_mod_info = {
                'prefix': class_mod_prefix,
                'stat_changes': non_dlc_class_mod_generation.calculate_stat_changes(class_mod_character, class_mod_type_info['type'], rarity, level),
                'skill_point_changes': 'none'
            }
    else:
        class_mod_prefixes = dlc_class_mod_generation.choose_prefix()
        if(class_mod_prefixes['alignment_1'] != class_mod_prefixes['alignment_2']):
            class_mod_prefix = class_mod_prefixes['alignment_1'] + ' ' + class_mod_prefixes['alignment_2']
        else:
            # We have 2 Neutral prefixes, which becomes 'True Neutral' rather 
            # than 'Neutral Neutral'
            class_mod_prefix = 'True Neutral'
        class_mod_info = {
            'prefix': class_mod_prefix,
            'stat_changes': dlc_class_mod_generation.calculate_stat_changes(rarity, level, class_mod_prefixes),
            'skill_point_changes': dlc_class_mod_generation.calculate_skill_point_changes(rarity, level, class_mod_character)
        }

    return ClassMod(level, rarity, class_mod_character, class_mod_type_info['type'], class_mod_prefix, class_mod_info['stat_changes'], class_mod_info['skill_point_changes'])

def choose_character():
    random_integer = random.randint(0,5)
    switcher = {
        0: 'assassin',
        1: 'commando',
        2: 'gunzerker',
        3: 'mechromancer',
        4: 'psycho',
        5: 'siren'
    }
    return switcher.get(random_integer, 'nothing')

def get_character_class_mod_generation_function(character):
    switcher = {
        'assassin': choose_assassin_class_mod_type,
        'commando': choose_commando_class_mod_type,
        'gunzerker': choose_gunzerker_class_mod_type,
        'mechromancer': choose_mechromancer_class_mod_type,
        'psycho': choose_psycho_class_mod_type,
        'siren': choose_siren_class_mod_type
    }
    return switcher.get(character, 'nothing')

def choose_assassin_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'infiltrator', 'is_dlc': False},
        1: {'type': 'killer', 'is_dlc': False},
        2: {'type': 'ninja', 'is_dlc': False},
        3: {'type': 'professional', 'is_dlc': False},
        4: {'type': 'rogue', 'is_dlc': True},
        5: {'type': 'shot', 'is_dlc': False},
        6: {'type': 'sniper', 'is_dlc': False},
        7: {'type': 'spy', 'is_dlc': False},
        8: {'type': 'stalker', 'is_dlc': False},
        9: {'type': 'survivor', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')

def choose_commando_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'engineer', 'is_dlc': False},
        1: {'type': 'grenadier', 'is_dlc': False},
        2: {'type': 'gunner', 'is_dlc': False},
        3: {'type': 'pointman', 'is_dlc': False},
        4: {'type': 'ranger', 'is_dlc': True},
        5: {'type': 'rifleman', 'is_dlc': False},
        6: {'type': 'shock trooper', 'is_dlc': False},
        7: {'type': 'specialist', 'is_dlc': False},
        8: {'type': 'tactician', 'is_dlc': False},
        9: {'type': 'veteran', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')

def choose_gunzerker_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'beast', 'is_dlc': False},
        1: {'type': 'bezerker', 'is_dlc': False},
        2: {'type': 'devastator', 'is_dlc': False},
        3: {'type': 'monk', 'is_dlc': True},
        4: {'type': 'hoarder', 'is_dlc': False},
        5: {'type': 'raider', 'is_dlc': False},
        6: {'type': 'renegade', 'is_dlc': False},
        7: {'type': 'tank', 'is_dlc': False},
        8: {'type': 'titan', 'is_dlc': False},
        9: {'type': 'war dog', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')

def choose_mechromancer_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'anarchist', 'is_dlc': False},
        1: {'type': 'catalyst', 'is_dlc': False},
        2: {'type': 'jill of all trades', 'is_dlc': False},
        3: {'type': 'necromancer', 'is_dlc': True},
        4: {'type': 'prodigy', 'is_dlc': False},
        5: {'type': 'punk', 'is_dlc': False},
        6: {'type': 'roboteer', 'is_dlc': False},
        7: {'type': 'sweetheart', 'is_dlc': False},
        8: {'type': 'technophile', 'is_dlc': False},
        9: {'type': 'zapper', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')

def choose_psycho_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'barbarian', 'is_dlc': True},
        1: {'type': 'blister', 'is_dlc': False},
        2: {'type': 'crunch', 'is_dlc': False},
        3: {'type': 'meat', 'is_dlc': False},
        4: {'type': 'reaper', 'is_dlc': False},
        5: {'type': 'sickle', 'is_dlc': False},
        6: {'type': 'slab', 'is_dlc': False},
        7: {'type': 'toast', 'is_dlc': False},
        8: {'type': 'torch', 'is_dlc': False},
        9: {'type': 'wound', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')

def choose_siren_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: {'type': 'banshee', 'is_dlc': False},
        1: {'type': 'binder', 'is_dlc': False},
        2: {'type': 'cat', 'is_dlc': False},
        3: {'type': 'cleric', 'is_dlc': True},
        4: {'type': 'fox', 'is_dlc': False},
        5: {'type': 'matriarch', 'is_dlc': False},
        6: {'type': 'nurse', 'is_dlc': False},
        7: {'type': 'trickster', 'is_dlc': False},
        8: {'type': 'warder', 'is_dlc': False},
        9: {'type': 'witch', 'is_dlc': False}
    }
    return switcher.get(random_integer, 'nothing')
