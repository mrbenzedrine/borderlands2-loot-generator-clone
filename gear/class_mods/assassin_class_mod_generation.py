import random

def choose_class_mod_type():
    random_integer = random.randint(0,9)
    switcher = {
        0: 'infiltrator',
        1: 'killer',
        2: 'ninja',
        3: 'professional',
        4: 'rogue',
        5: 'shot',
        6: 'sniper',
        7: 'spy',
        8: 'stalker',
        9: 'survivor'
    }
    return switcher.get(random_integer, 'nothing')

def get_stat_changes_function(class_mod_type):
    switcher = {
        'infiltrator': calculate_infiltrator_com_stat_changes,
        'killer': calculate_killer_com_stat_changes,
        'ninja': calculate_ninja_com_stat_changes,
        'professional': calculate_professional_com_stat_changes,
        'rogue': calculate_rogue_com_stat_changes,
        'shot': calculate_shot_com_stat_changes,
        'sniper': calculate_sniper_com_stat_changes,
        'spy': calculate_spy_com_stat_changes,
        'stalker': calculate_stalker_com_stat_changes,
        'survivor'calculate_survivor_com_stat_changes:
    }
    return switcher.get(class_mod_type, 'nothing')

def calculate_infiltrator_com_stat_changes(rarity, level):
    pass

def calculate_killer_com_stat_changes(rarity, level):
    pass

def calculate_ninja_com_stat_changes(rarity, level):
    pass

def calculate_professional_com_stat_changes(rarity, level):
    pass

def calculate_rogue_com_stat_changes(rarity, level):
    pass

def calculate_shot_com_stat_changes(rarity, level):
    pass

def calculate_sniper_com_stat_changes(rarity, level):
    pass

def calculate_spy_com_stat_changes(rarity, level):
    pass

def calculate_stalker_com_stat_changes(rarity, level):
    pass

def calculate_survivor_com_stat_changes(rarity, level):
    pass


def get_skill_point_changes_function(class_mod_type):
    switcher = {
        'infiltrator': calculate_infiltrator_com_skill_point_changes,
        'killer': calculate_killer_com_skill_point_changes,
        'ninja': calculate_ninja_com_skill_point_changes,
        'professional': calculate_professional_com_skill_point_changes,
        'rogue': calculate_rogue_com_skill_point_changes,
        'shot': calculate_shot_com_skill_point_changes,
        'sniper': calculate_sniper_com_skill_point_changes,
        'spy': calculate_spy_com_skill_point_changes,
        'stalker': calculate_stalker_com_skill_point_changes,
        'survivor':calculate_survivor_com_skill_point_changes
    }
    return switcher.get(class_mod_type, 'nothing')

def calculate_infiltrator_com_skill_point_changes(rarity, level):
    pass

def calculate_killer_com_skill_point_changes(rarity, level):
    pass

def calculate_ninja_com_skill_point_changes(rarity, level):
    pass

def calculate_professional_com_skill_point_changes(rarity, level):
    pass

def calculate_rogue_com_skill_point_changes(rarity, level):
    pass

def calculate_shot_com_skill_point_changes(rarity, level):
    pass

def calculate_sniper_com_skill_point_changes(rarity, level):
    pass

def calculate_spy_com_skill_point_changes(rarity, level):
    pass

def calculate_stalker_com_skill_point_changes(rarity, level):
    pass

def calculate_survivor_com_skill_point_changes(rarity, level):
    pass
