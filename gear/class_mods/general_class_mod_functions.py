import random

def get_remaining_skills_to_boost(rarity, com_prefix, fixed_skills_from_com_to_boost, all_skills_to_boost):
    
    leftover_fixed_skills = []

    for prefix in fixed_skills_from_com_to_boost:
        if prefix != com_prefix:
            leftover_fixed_skills.append(fixed_skills_from_com_to_boost[prefix])

    other_skills_to_boost = []

    if rarity == 'Blue':
        # Get 1 extra skill

        random_integer = random.randint(0,1)
        other_skills_to_boost.append(leftover_fixed_skills[random_integer])

    else:
        # Purple rarity, so get 2 extra skills, and these will just be the
        # 2 skills in leftover_fixed_skills

        other_skills_to_boost = leftover_fixed_skills

    # Add the skills in other_skills_to_boost to all_skills_to_boost

    for skill in other_skills_to_boost:
        # Use a placeholder value of 1 for now
        all_skills_to_boost[skill] = 1

    return all_skills_to_boost
