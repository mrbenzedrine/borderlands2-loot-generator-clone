import random
from gear.relics.relic import Relic
from gear.relics import aggression
from gear.relics import allegiance
from gear.relics import elemental
from gear.relics import proficiency
from gear.relics import protection
from gear.relics import resistance
from gear.relics import stockpile
from gear.relics import strength
from gear.relics import tenacity
from gear.relics import vitality 

def generate(level, rarity):

    relic_type = choose_relic_type()
    relic_type_generation_module = get_relic_type_generation_module(relic_type)
    relic_stats = relic_type_generation_module.calculate_stats(level, rarity) 

    return Relic(level, rarity, relic_type, relic_stats)

def choose_relic_type():

    random_integer = random.randint(0,9)
    switcher = {
        0: 'aggression',
        1: 'allegiance',
        2: 'elemental',
        3: 'proficiency',
        4: 'protection',
        5: 'resistance',
        6: 'stockpile',
        7: 'strength',
        8: 'tenacity',
        9: 'vitality'
    }
    return switcher.get(random_integer, 'nothing')

def get_relic_type_generation_module(relic_type):
    switcher = {
        'aggression': aggression,
        'allegiance': allegiance,
        'elemental': elemental,
        'proficiency': proficiency,
        'protection': protection,
        'resistance': resistance,
        'stockpile': stockpile,
        'strength': strength,
        'tenacity': tenacity,
        'vitality': vitality
    }
    return switcher.get(relic_type, 'nothing')
