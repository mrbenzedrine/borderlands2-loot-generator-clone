import random

def calculate_stats(level, rarity):

    chosen_manufacturer = choose_manufacturer()
    list_of_possible_traits = get_manufacturer_possible_weapon_traits(chosen_manufacturer)
    no_of_traits_to_boost = random.randint(1,2)
    traits_to_boost = get_traits_to_boost(no_of_traits_to_boost, list_of_possible_traits)

    stats = {}

    for trait in traits_to_boost:
        stats[chosen_manufacturer + ' ' + trait] = calculate_trait_increase(level, rarity)

    return stats

def choose_manufacturer():

    random_integer = random.randint(0,7)
    switcher = {
        0: 'Bandit'
        1: 'Dahl',
        2: 'Hyperion',
        3: 'Jakobs',
        4: 'Maliwan',
        5: 'Tediore',
        6: 'Torgue',
        7: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')

def get_manufacturer_possible_weapon_traits(manufacturer):

    switcher = {
        'Bandit': ['Damage', 'Fire rate', 'Reload speed'],
        'Dahl': ['Burst delay', 'Magazine size', 'Recoil reduction'],
        'Hyperion': ['Damage', 'Max accuracy', 'Reload speed'],
        'Jakobs': ['Accuracy recovery', 'Magazine size', 'Recoil reduction'],
        'Maliwan': ['Damage', 'Fire rate', 'Reload speed'],
        'Tediore' ['Damage', 'Magazine size', 'Recoil reduction'],
        'Torgue': ['Accuracy recovery', 'Fire rate', 'Magazine size'],
        'Vladof': ['Damage', 'Accuracy recovery', 'Recoil reduction']
    }
    return switcher.get(manufacturer, 'nothing')

def get_traits_to_boost(no_of_traits_to_boost, list_of_traits):

    traits_to_boost = []

    random_integer = random.randint(0,2)
    if(no_of_traits_to_boost == 1):
        traits_to_boost.append(list_of_traits[random_integer])
    else:
        # Boosting 2 traits, so can just delete 1 trait from list_of_traits
        # and set traits_to_boost equal to that (since list_of_traits always
        # contains 3 traits
        del list_of_traits[random_integer]
        traits_to_boost - list_of_traits

    return traits_to_boost

def calculate_trait_increase(level, rarity):

    return '+0%'

