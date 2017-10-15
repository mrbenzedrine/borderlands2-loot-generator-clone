import random

from .assassin_class_mods import infiltrator
from .assassin_class_mods import killer
from .assassin_class_mods import ninja
from .assassin_class_mods import professional
from .assassin_class_mods import rogue
from .assassin_class_mods import shot
from .assassin_class_mods import sniper
from .assassin_class_mods import spy
from .assassin_class_mods import stalker
from .assassin_class_mods import survivor

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

def get_class_mod_prefix_function(class_mod_type):
    switcher = {
        'infiltrator': infiltrator.choose_prefix,
        'killer': killer.choose_prefix,
        'ninja': ninja.choose_prefix,
        'professional': professional.choose_prefix,
        'rogue': rogue.choose_prefix,
        'shot': shot.choose_prefix,
        'sniper': sniper.choose_prefix,
        'spy': spy.choose_prefix,
        'stalker': stalker.choose_prefix,
        'survivor': survivor.choose_prefix
    }
    return switcher.get(class_mod_type, 'nothing')

def get_stat_changes_function(class_mod_type):
    switcher = {
        'infiltrator': infiltrator.calculate_stat_changes,
        'killer': killer.calculate_stat_changes,
        'ninja': ninja.calculate_stat_changes,
        'professional': professional.calculate_stat_changes,
        'rogue': rogue.calculate_stat_changes,
        'shot': shot.calculate_stat_changes,
        'sniper': sniper.calculate_stat_changes,
        'spy': spy.calculate_stat_changes,
        'stalker': stalker.calculate_stat_changes,
        'survivor': survivor.calculate_stat_changes
    }
    return switcher.get(class_mod_type, 'nothing')

def get_skill_point_changes_function(class_mod_type):
    switcher = {
        'infiltrator': infiltrator.calculate_skill_point_changes,
        'killer': killer.calculate_skill_point_changes,
        'ninja': ninja.calculate_skill_point_changes,
        'professional': professional.calculate_skill_point_changes,
        'rogue': rogue.calculate_skill_point_changes,
        'shot': shot.calculate_skill_point_changes,
        'sniper': sniper.calculate_skill_point_changes,
        'spy': spy.calculate_skill_point_changes,
        'stalker': stalker.calculate_skill_point_changes,
        'survivor': survivor.calculate_skill_point_changes
    }
    return switcher.get(class_mod_type, 'nothing')
