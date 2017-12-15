import random

def calculate_stats(level, rarity):

    no_of_elemental_resistances = random.randint(1,4)
    elemental_resistances = get_elemental_resistances(no_of_elemental_resistances)

    stats = {}
    for i in range(0,no_of_elemental_resistances):
        stats[elemental_resistances[i] + ' resistance'] = calculate_resistance(level, rarity)

    return stats

def get_elemental_resistances(no_of_elemental_resistances):

    chosen_elemental_resistances = []
    all_elements = ['Incendiary', 'Corrosion', 'Shock', 'Explosion', 'Non-elemental']

    for i in range(0,no_of_elemental_resistances):
        random_integer = random.randint(0,len(all_elements) - 1)
        chosen_elemental_resistances.append(all_elements[random_integer])
        del all_elements[random_integer]

    return chosen_elemental_resistances

def calculate_resistance(level, rarity):

    return '+0%'
