import random

from gear.class_mods.class_mod import ClassMod

from gear.class_mods import non_dlc_class_mod_generation
from gear.class_mods import dlc_class_mod_generation

def generate(rarity, level):
    
    class_mod_character = choose_character()
    class_mod_type_info = random.choice(class_mod_types[class_mod_character])

    # Generation of class mods in Tiny Tina DLC is slightly different to
    # non-DLC class mods, so we must handle them differently

    if(not class_mod_type_info['is_dlc']):
        # White rarity class mods only change stats, they don't affect skill
        # points
        if(rarity != 'White'):
            class_mod_prefix = non_dlc_class_mod_generation.choose_prefix(class_mod_character, class_mod_type_info['type'])
            class_mod_info = {
                'stat_changes': non_dlc_class_mod_generation.calculate_stat_changes(class_mod_character, class_mod_type_info['type'], rarity, level),
                'skill_point_changes': non_dlc_class_mod_generation.calculate_skill_point_changes(class_mod_character, class_mod_type_info['type'], rarity, level, class_mod_prefix)
            }
        else:
            class_mod_prefix = 'none'
            class_mod_info = {
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
            'stat_changes': dlc_class_mod_generation.calculate_stat_changes(rarity, level, class_mod_prefixes),
            'skill_point_changes': dlc_class_mod_generation.calculate_skill_point_changes(rarity, level, class_mod_character)
        }

    return ClassMod(level, rarity, class_mod_type_info['type'], class_mod_info, class_mod_character, class_mod_prefix)

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

class_mod_types = {

    'assassin': [
        {'type': 'infiltrator', 'is_dlc': False},
        {'type': 'killer', 'is_dlc': False},
        {'type': 'ninja', 'is_dlc': False},
        {'type': 'professional', 'is_dlc': False},
        {'type': 'rogue', 'is_dlc': True},
        {'type': 'shot', 'is_dlc': False},
        {'type': 'sniper', 'is_dlc': False},
        {'type': 'spy', 'is_dlc': False},
        {'type': 'stalker', 'is_dlc': False},
        {'type': 'survivor', 'is_dlc': False}
    ],

    'commando': [
        {'type': 'engineer', 'is_dlc': False},
        {'type': 'grenadier', 'is_dlc': False},
        {'type': 'gunner', 'is_dlc': False},
        {'type': 'pointman', 'is_dlc': False},
        {'type': 'ranger', 'is_dlc': True},
        {'type': 'rifleman', 'is_dlc': False},
        {'type': 'shock trooper', 'is_dlc': False},
        {'type': 'specialist', 'is_dlc': False},
        {'type': 'tactician', 'is_dlc': False},
        {'type': 'veteran', 'is_dlc': False}
    ],

    'gunzerker': [
        {'type': 'beast', 'is_dlc': False},
        {'type': 'bezerker', 'is_dlc': False},
        {'type': 'devastator', 'is_dlc': False},
        {'type': 'monk', 'is_dlc': True},
        {'type': 'hoarder', 'is_dlc': False},
        {'type': 'raider', 'is_dlc': False},
        {'type': 'renegade', 'is_dlc': False},
        {'type': 'tank', 'is_dlc': False},
        {'type': 'titan', 'is_dlc': False},
        {'type': 'war dog', 'is_dlc': False}
    ],

    'mechromancer': [
        {'type': 'anarchist', 'is_dlc': False},
        {'type': 'catalyst', 'is_dlc': False},
        {'type': 'jill of all trades', 'is_dlc': False},
        {'type': 'necromancer', 'is_dlc': True},
        {'type': 'prodigy', 'is_dlc': False},
        {'type': 'punk', 'is_dlc': False},
        {'type': 'roboteer', 'is_dlc': False},
        {'type': 'sweetheart', 'is_dlc': False},
        {'type': 'technophile', 'is_dlc': False},
        {'type': 'zapper', 'is_dlc': False}
    ],

    'psycho': [
        {'type': 'barbarian', 'is_dlc': True},
        {'type': 'blister', 'is_dlc': False},
        {'type': 'crunch', 'is_dlc': False},
        {'type': 'meat', 'is_dlc': False},
        {'type': 'reaper', 'is_dlc': False},
        {'type': 'sickle', 'is_dlc': False},
        {'type': 'slab', 'is_dlc': False},
        {'type': 'toast', 'is_dlc': False},
        {'type': 'torch', 'is_dlc': False},
        {'type': 'wound', 'is_dlc': False}
    ],

    'siren': [
        {'type': 'banshee', 'is_dlc': False},
        {'type': 'binder', 'is_dlc': False},
        {'type': 'cat', 'is_dlc': False},
        {'type': 'cleric', 'is_dlc': True},
        {'type': 'fox', 'is_dlc': False},
        {'type': 'matriarch', 'is_dlc': False},
        {'type': 'nurse', 'is_dlc': False},
        {'type': 'trickster', 'is_dlc': False},
        {'type': 'warder', 'is_dlc': False},
        {'type': 'witch', 'is_dlc': False}
    ]

}
