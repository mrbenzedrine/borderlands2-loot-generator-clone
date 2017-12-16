import random

def calculate_stats(level, rarity):

    stats_to_boost = get_stats_to_boost()
    stats = {}

    for stat in stats_to_boost:
        stats[stat] = calculate_stat_increase(level, rarity)

    return stats

def get_stats_to_boost():

    random_integer = random.randint(0,2)
    switcher = {
        0: ['Shield capacity'],
        1: ['Shield recharge delay'],
        2: ['Shield capacity', 'Shield recharge delay']
    }
    return switcher.get(random_integer, 'nothing')

def calculate_stat_increase(level, rarity):

    return '+0%'
