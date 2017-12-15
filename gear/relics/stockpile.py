import random

def calculate_stats(level, rarity):

    no_of_ammo_types_to_boost = random.randint(1,3)
    are_grenades_boosted = boost_grandes_or_not()

    ammo_types_to_boost = get_ammo_types_to_boost(are_grenades_boosted, no_of_ammo_types_to_boost)

    stats = {}

    for ammo_type in ammo_types_to_boost:
        stats[ammo_type + ' max ammo'] = calculate_max_ammo_increase(level, rarity, ammo_type)

    return stats

def boost_grandes_or_not():

    random_integer = random.randint(0,1)
    switcher = {
        0: True,
        1: False
    }
    return switcher.get(random_integer, 'nothing')

def get_ammo_types_to_boost(are_grenades_boosted, no_of_ammo_types):
    
    ammo_types_to_boost = []
    all_ammo_types = ['Assault rifle', 'Launcher', 'Pistol', 'SMG', 'Sniper rifle', 'Shotgun', 'Grenade']

    if(!are_grenades_boosted):
        del all_ammo_types[all_ammo_types.index('Grenade')]

    for i in range(0,no_of_ammo_types):
        random_integer = random.randint(0,len(all_ammo_types) - 1)
        ammo_types_to_boost.append(all_ammo_types[random_integer])
        del all_ammo_types[random_integer]

    return ammo_types_to_boost

def calculate_max_ammo_increase(level, rarity, ammo_type):

    if(ammo_type == 'Grenade'):
        ammo_increase = '+0'
    else:
        ammo_increase = '+0%'

    return ammo_increase
