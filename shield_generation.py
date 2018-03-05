import random
from gear.shields.shield import Shield
from gear.shields import absorb
from gear.shields import adaptive
from gear.shields import amplify
from gear.shields import booster
from gear.shields import nova
from gear.shields import roid
from gear.shields import spike
from gear.shields import standard
from gear.shields import turtle

def generate(rarity, level):

    # rarity: string; 'White', 'Green' etc

    # level: integer; will be given either the level of the enemy that 
    # dropped the shield item or the area in which the chest that the 
    # shield was found in

    shield_type = choose_shield_type()

    shield_manufacturer = get_shield_manufacturer(shield_type)
    body_manufacturer = generate_manufacturer()
    battery_manufacturer = generate_manufacturer()
    capacitor_manufacturer = generate_manufacturer()

    shield_parts = {

        'body': body_manufacturer,
        'battery': battery_manufacturer,
        'capacitor': capacitor_manufacturer

    }

    shield_type_generation_module = get_shield_type_generation_module(shield_type)
    shield_main_stats = shield_type_generation_module.calculate_main_stats(level, rarity)

    if(shield_type == 'nova' or shield_type == 'spike'):
        shield_type_specific_stats = shield_type_generation_module.calculate_type_specific_stats(level, rarity, shield_manufacturer)
    else:
        shield_type_specific_stats = shield_type_generation_module.calculate_type_specific_stats(level, rarity)

    shield_stats = {
        'main_stats': shield_main_stats,
        'type_specific_stats': shield_type_specific_stats
    }

    return Shield(level, rarity, shield_type, shield_stats, shield_manufacturer, shield_parts)

def choose_shield_type():
    types = [
        'shield',
        'absorb',
        'adaptive',
        'amplify',
        'booster',
        'nova',
        'spike',
        'roid',
        'turtle'
    ]
    return random.choice(types)

def get_shield_manufacturer(shield_type):
    switcher = {
        'shield': 'Tediore',
        'absorb': 'Vladof',
        'adaptive': 'Anshin',
        'amplify': 'Hyperion',
        'booster': 'Dahl',
        'nova': choose_nova_spike_manufacturer(),
        'spike': choose_nova_spike_manufacturer(),
        'roid': 'Bandit',
        'turtle': 'Pangolin'
    }
    return switcher.get(shield_type, 'nothing')

def choose_nova_spike_manufacturer():
    manufacturers = ['Maliwan', 'Torgue']
    return random.choice(manufacturers)

def generate_manufacturer():
    # No non-unique Jakobs shields exist, so Jakobs don't produce
    # shields in general or shield parts
    manufacturers = [
        'Anshin',
        'Bandit',
        'Dahl',
        'Hyperion',
        'Maliwan',
        'Pangolin',
        'Tediore',
        'Torgue',
        'Vladof'
    ]
    return random.choice(manufacturers)

def get_shield_type_generation_module(shield_type):
    switcher = {
        'absorb': absorb,
        'adaptive': adaptive,
        'amplify': amplify,
        'booster': booster,
        'nova': nova,
        'roid': roid,
        'spike': spike,
        'shield': standard,
        'turtle': turtle
    }
    return switcher.get(shield_type, 'nothing')
