import random

def choose_element():

    random_integer = random.randint(0,4)
    switcher = {
        0: 'Incendiary',
        1: 'Corrosion',
        2: 'Shock',
        3: 'Slag',
        4: 'Explosion'
    }
    return switcher.get(random_integer, 'nothing') 

