import random

def calculate_stats(level, rarity):

    weapon_type = choose_weapon_type()
    stat_name = weapon_type + ' damage'

    stats = {
        stat_name: calculate_damage_increase(level, rarity)
    }

    return stats

def choose_weapon_type():
    
    random_integer = random.randint(0,5)
    switcher = {
        0: 'assault rifle',
        1: 'launcher',
        2: 'pistol',
        3: 'shotgun',
        4: 'smg',
        5: 'sniper rifle'
    }
    return switcher.get(random_integer, 'nothing')

def calculate_damage_increase(level, rarity):

    # Use a placeholder value of 0% for now

    return '+0%'

