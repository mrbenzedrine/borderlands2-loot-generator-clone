import random
from . import general_relic_functions

def calculate_stats(level, rarity):

    relic_element = general_relic_functions.choose_element()
    damage_increase = calculate_damage_increase(level, rarity)

    # Can't have non-elemental elemental relic, so check if we have
    # a valid element

    while True:
        if(check_valid_element(relic_element) is True):
            break
        else:
            relic_element = general_relic_functions.choose_element()

    stats = {
        'element': relic_element,
        'damage increase': damage_increase
    }

    return stats

def calculate_damage_increase(level, rarity):

    return '+0%'

def check_valid_element(element):

    test = element != 'Non-elemental'

    return test
