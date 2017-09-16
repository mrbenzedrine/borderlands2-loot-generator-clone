import random
import shield

def generate(rarity, level):

    # rarity: string; 'White', 'Green' etc

    # level: integer; will be given either the level of the enemy that 
    # dropped the shield item or the area in which the chest that the 
    # shield was found in

    shield_type = choose_shield_type()

    ShieldClass = get_shield_type_class(shield_type)

    shield_manufacturer = get_shield_manufacturer(shield_type)
    body_manufacturer = generate_manufacturer()
    battery_manufacturer = generate_manufacturer()
    capcitor_manufacturer = generate_manufacturer()

    shield_parts = {

        'body': body_manufacturer,
        'battery': battery_manufacturer,
        'capacitor': capcitor_manufacturer

    }

    return ShieldClass(shield_manufacturer, shield_parts, level, rarity)

def choose_shield_type():
    random_integer = random.randint(0,8)
    switcher = {
        0: 'shield',
        1: 'absorb',
        2: 'adaptive',
        3: 'amplify',
        4: 'booster',
        5: 'nova',
        6: 'spike',
        7: 'roid',
        8: 'turtle'
    }
    return switcher.get(random_integer, 'nothing')

def get_shield_type_class(shield_type):
    switcher = {
        'shield': shield.Shield,
        'absorb': shield.AbsorbShield,
        'adaptive': shield.AdaptiveShield,
        'amplify': shield.AmplifyShield,
        'booster': shield.BoosterShield,
        'nova': shield.NovaShield,
        'spike': shield.SpikeShield,
        'roid': shield.RoidShield,
        'turtle': shield.TurtleShield
    }
    return switcher.get(shield_type, 'nothing')

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
    random_integer = random.randint(0,1)
    switcher = {
        0: 'Maliwan',
        1: 'Torgue'
    }
    return switcher.get(random_integer, 'nothing')

def generate_manufacturer():
    # No non-unique Jakobs shields exist, so Jakobs don't produce
    # shields in general or shield parts
    random_integer = random.randint(0,8)
    switcher = {
        0: 'Anshin',
        1: 'Bandit',
        2: 'Dahl',
        3: 'Hyperion',
        4: 'Maliwan',
        5: 'Pangolin',
        6: 'Tediore',
        7: 'Torgue',
        8: 'Vladof'
    }
    return switcher.get(random_integer, 'nothing')