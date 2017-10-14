import random

def choose_prefix():
    # Need to roll for 2 different 'alignments'

    alignment_1 = choose_alignment_one()
    alignment_2 = choose_alignment_two()

    return {
        'alignment_1': alignment_1,
        'alignment_2': alignment_2
    }

def choose_alignment_one():
    random_integer = random.randint(0,2)
    switcher = {
        0: 'Chaotic',
        1: 'Lawful',
        2: 'Neutral'
    }
    return switcher.get(random_integer, 'nothing')

def choose_alignment_two():
    random_integer = random.randint(0,2)
    switcher = {
        0: 'Evil',
        1: 'Good',
        2: 'Neutral'
    }
    return switcher.get(random_integer, 'nothing')

def calculate_stat_changes(rarity, level, alignments):
    alignment_one_stat_change = get_alignment_one_stat_change(alignments['alignment_1'])
    alignment_two_stat_change = get_alignment_two_stat_change(alignments['alignment_2'])

    stat_changes = {}

    # Copying the stat changes from both alignments
    for stat in alignment_one_stat_change:
        stat_changes[stat] = alignment_one_stat_change[stat]

    for stat in alignment_two_stat_change:
        stat_changes[stat] = alignment_two_stat_change[stat]

    return stat_changes

def get_alignment_one_stat_change(alignment):
    switcher = {
        'Chaotic': {'Fire rate': '+0%'},
        'Lawful': {'Accuracy': '+31%'},
        'Neutral': {'Magazine size': '+0%'}
    }
    return switcher.get(alignment, 'nothing')

def get_alignment_two_stat_change(alignment):
    switcher = {
        'Evil': {'Critical damage': '+0%'},
        'Good': {'Reload speed': '+45%'},
        'Neutral': {'Magazine size': '+0%'}
    }
    return switcher.get(alignment, 'nothing')

def calculate_skill_point_changes(rarity, level):
    all_skill_point_boosts = {}

    fixed_skills_to_boost = ['Like the Wind', 'Tw0 Fang', 'Vel0city']

    if(rarity == 'Blue'):
        # Need to pick 2 skills from fixed_skills_to_boost, so what
        # we'll do is generate a random integer between 0 and 2, remove
        # the skill with that index in fixed_skills_to_boost, and then
        # take the remaining 2 skills left

        random_integer = random.randint(0,2)
        skills_to_boost = fixed_skills_to_boost.remove(fixed_skills_to_boost[random_integer])

    elif(rarity == 'Purple'):
        skills_to_boost = fixed_skills_to_boost

    # Finally, add the skills in skills_to_boost to all_skill_point_boosts

    for x in range(0, len(skills_to_boost)):
        # Have placeholder value of 1 for now
        all_skill_point_boosts[skills_to_boost[x]] = 1

    return all_skill_point_boosts
