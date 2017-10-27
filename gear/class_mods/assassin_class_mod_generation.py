import random

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
