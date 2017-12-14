import random
from . import general_relic_functions

def calculate_stats(level, rarity):

    relic_element = general_relic_functions.choose_element()
    damage_increase = calculate_damage_increase(level, rarity)

    stats = {
        'element': relic_element,
        'damage increase': damage_increase
    }

    return stats

def calculate_damage_increase(level, rarity):

    return '+0%'

