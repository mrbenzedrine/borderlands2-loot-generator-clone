import random
from .. import general_class_mod_functions

def choose_prefix():
    # Only used for green rarity and upwards
    random_integer = random.randint(0,2)
    switcher = {
        0: 'Graceful',
        1: 'Tricky',
        2: 'Rugged'
    }
    return switcher.get(random_integer, 'nothing')

def calculate_stat_changes(rarity, level):    
    # Will be calculatable via rarity and level, but have placeholder
    # value for now
    return {
        'Fire rate': '+0%',
        'Melee damage': '+0%'
    }

def calculate_skill_point_changes(rarity, level, prefix):
    # Green class mods boost 1 skill, blue boosts 2 skills and purple
    # boosts 3 skills
    # 1 skill is fixed by the prefix, and any other skill point boosts are
    # chsen at random from a predefined set of 3 skills
    all_skill_point_boosts = {}

    # First get the 1 skill boost that is fixed by the prefix
    fixed_skill_boost_by_com_prefix = {
        'Graceful': 'Be Like Water',
        'Tricky': 'Unf0rseen',
        'Rugged': 'Ir0n Hand'
    }

    # Have a placeholder value of 1 for the skill point boost for now
    all_skill_point_boosts[fixed_skill_boost_by_com_prefix[prefix]] = 1

    # If rarity is green then there's no need to get any more skills to
    # boost, otherwise, call get_remaining_skills_to_boost in
    # general_class_mod_functions
    
    if(rarity != 'Green'):
        all_skill_point_boosts = general_class_mod_functions.get_remaining_skills_to_boost(rarity, prefix, fixed_skill_boost_by_com_prefix, all_skill_point_boosts)

    return all_skill_point_boosts
