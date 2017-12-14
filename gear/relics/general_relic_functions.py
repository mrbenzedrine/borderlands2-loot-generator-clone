import random

def choose_element():

    random_integer = random.randint(0,5)
    switcher = {
        0: 'Incendiary',
        1: 'Corrosion',
        2: 'Shock',
        3: 'Slag',
        4: 'Explosion',
        5: 'Non-elemental'
    }
    return switcher.get(random_integer, 'nothing') 

