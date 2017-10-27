import random

from .assassin_class_mods.assassin_class_mods_info import assassin_class_mods
from . import general_class_mod_functions

def choose_class_mod_type():
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

def choose_prefix(class_mod_type):
    possible_prefixes = assassin_class_mods[class_mod_type]['prefixes']
    random_integer = random.randint(0,2)

    return possible_prefixes[random_integer]

def calculate_stat_changes(class_mod_type, rarity, level):    
    stats_to_change = assassin_class_mods[class_mod_type]['stat_changes']
    stat_changes = {}

    # Use a placeholder value of +0% for now
    for x in range(0, len(stats_to_change)):
        stat_changes[stats_to_change[x]] = '+0%'

    return stat_changes

def calculate_skill_point_changes(class_mod_type, rarity, level, prefix):
    # Green class mods boost 1 skill, blue boosts 2 skills and purple
    # boosts 3 skills
    # 1 skill is fixed by the prefix, and any other skill point boosts are
    # chsen at random from a predefined set of 3 skills
    all_skill_point_boosts = {}

    # First get the 1 skill boost that is fixed by the prefix
    fixed_skills_to_boost_by_com_prefix = assassin_class_mods[class_mod_type]['fixed_skills_to_boost_by_com_prefix']

    # Have a placeholder value of 1 for the skill point boost for now
    all_skill_point_boosts[fixed_skills_to_boost_by_com_prefix[prefix]] = 1

    # If rarity is green then there's no need to get any more skills to
    # boost, otherwise, call get_remaining_skills_to_boost in
    # general_class_mod_functions
    
    if(rarity != 'Green'):
        all_skill_point_boosts = general_class_mod_functions.get_remaining_skills_to_boost(rarity, prefix, fixed_skills_to_boost_by_com_prefix, all_skill_point_boosts)

    return all_skill_point_boosts
