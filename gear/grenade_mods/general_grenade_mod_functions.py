import random

def choose_delivery_mechanism():
    random_integer = random.randint(0,6)
    switcher = {
        0: 'Lobbed',
        1: 'Lobbed Sticky',
        2: 'Homing',
        3: 'Homing Sticky',
        4: 'Longbow',
        5: 'Longbow Sticky',
        6: 'Rubberised'
    }
    return switcher.get(random_integer, 'nothing')

def choose_element():
    random_integer = random.randint(0,4)
    switcher = {
        0: 'Incendiary',
        1: 'Corrosion',
        2: 'Explosion',
        3: 'Shock',
        4: 'Slag'
    }
    return switcher.get(random_integer, "nothing")
