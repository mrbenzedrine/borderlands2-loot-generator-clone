import random

from .assassin_class_mods_info import assassin_class_mods
from .commando_class_mods_info import commando_class_mods
from .gunzerker_class_mods_info import gunzerker_class_mods
from .mechromancer_class_mods_info import mechromancer_class_mods
from .psycho_class_mods_info import psycho_class_mods
from .siren_class_mods_info import siren_class_mods

from . import general_class_mod_functions

def choose_prefix(character, class_mod_type):
    character_class_mod_info = {
        'assassin': assassin_class_mods,
        'commando': commando_class_mods,
        'gunzerker': gunzerker_class_mods,
        'mechromancer': mechromancer_class_mods,
        'psycho': psycho_class_mods,
        'siren': siren_class_mods
    }.get(character, 'nothing')

    possible_prefixes = character_class_mod_info[class_mod_type]['prefixes']

    return random.choice(possible_prefixes)

def calculate_stat_changes(character, class_mod_type, rarity, level):
    character_class_mod_info = {
        'assassin': assassin_class_mods,
        'commando': commando_class_mods,
        'gunzerker': gunzerker_class_mods,
        'mechromancer': mechromancer_class_mods,
        'psycho': psycho_class_mods,
        'siren': siren_class_mods
    }.get(character, 'nothing')

    stats_to_change = character_class_mod_info[class_mod_type]['stat_changes']
    stat_changes = {}

    # Use a placeholder value of +0% for now
    for stat in stats_to_change:
        stat_changes[stat] = '+0%'

    return stat_changes

def calculate_skill_point_changes(character, class_mod_type, rarity, level, prefix):
    character_class_mod_info = {
        'assassin': assassin_class_mods,
        'commando': commando_class_mods,
        'gunzerker': gunzerker_class_mods,
        'mechromancer': mechromancer_class_mods,
        'psycho': psycho_class_mods,
        'siren': siren_class_mods
    }.get(character, 'nothing')

    # Green class mods boost 1 skill, blue boosts 2 skills and purple
    # boosts 3 skills
    # 1 skill is fixed by the prefix, and any other skill point boosts are
    # chsen at random from a predefined set of 3 skills
    all_skill_point_boosts = {}

    # First get the 1 skill boost that is fixed by the prefix
    fixed_skills_to_boost_by_com_prefix = character_class_mod_info[class_mod_type]['fixed_skills_to_boost_by_com_prefix']

    # Have a placeholder value of 1 for the skill point boost for now
    all_skill_point_boosts[fixed_skills_to_boost_by_com_prefix[prefix]] = 1

    # If rarity is green then there's no need to get any more skills to
    # boost, otherwise, call get_remaining_skills_to_boost in
    # general_class_mod_functions
    
    if rarity != 'Green':
        all_skill_point_boosts = general_class_mod_functions.get_remaining_skills_to_boost(rarity, prefix, fixed_skills_to_boost_by_com_prefix, all_skill_point_boosts)

    return all_skill_point_boosts
