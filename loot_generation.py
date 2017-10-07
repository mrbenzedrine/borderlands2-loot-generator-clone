import weapon_generation
import shield_generation
import random

def enemy_loot_generation(enemy):
    
    # enemy: instance of an enemy class

    enemy_loot_dropped = enemy.calculate_potential_loot_dropped()
    print(enemy_loot_dropped)

    # Create array that will hold all the loot dropped by the enemy

    all_loot = []

    for index in range(0, len(enemy_loot_dropped)):
        loot_pool_part = enemy_loot_dropped[index]
        for quantity in range(0, loot_pool_part['quantity']):
            loot = choose_loot_type().generate(loot_pool_part['rarity'], enemy.level)
            all_loot.append(loot)

    return all_loot

def chest_loot_generation():
    pass

def choose_loot_type():
    random_integer = random.randint(0,1)
    switcher = {
        0: weapon_generation,
        1: shield_generation
    }
    return switcher.get(random_integer, 'nothing')
