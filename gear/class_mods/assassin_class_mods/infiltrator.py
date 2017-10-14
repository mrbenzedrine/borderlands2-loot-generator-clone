import random

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

    # Now calculate any other skill point boosts depending on the rarity

    leftover_fixed_skills = []

    # Grab the 2 skills leftover and put them in leftover_fixed_skills
    for com_prefix in fixed_skill_boost_by_com_prefix:
        if(com_prefix != prefix):
            leftover_fixed_skills.append(fixed_skill_boost_by_com_prefix[com_prefix])

    other_skills_to_boost = []

    if(rarity == 'Blue'):
        # Get 1 more skill to boost

        # Need to do a roll on the two skills in leftover_fixed_skills

        random_integer = random.randint(0,1)
        other_skills_to_boost.append(leftover_fixed_skills[random_integer])

    elif(rarity == 'Purple'):
        # Need to boost the other 2 skills in leftover_fixed_skills,
        # so can simply set other_skills_to_boost equal to 
        # leftover_fixed_skills

        other_skills_to_boost = leftover_fixed_skills

    # Now add the skills in other_skills_to_boost to all_skill_point_boosts

    for x in range(0, len(other_skills_to_boost)):
        # Have placeholder value of 1 for now
        all_skill_point_boosts[other_skills_to_boost[x]] = 1

    return all_skill_point_boosts
