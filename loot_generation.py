import weapon_generation
import shield_generation
import grenade_mod_generation
import relic_generation
import random

def enemy_loot_generation(enemy):
    
    # enemy: instance of an enemy class

    enemy_loot_dropped = enemy.drop_loot()
    print(enemy_loot_dropped)

    all_loot = []

    for loot_rarity in enemy_loot_dropped:
        for loot_quantity in range(0, enemy_loot_dropped[loot_rarity]):
            loot = choose_loot_type().generate(loot_rarity, enemy.level)
            all_loot.append(loot)

    return all_loot

def chest_loot_generation():
    pass

def choose_loot_type():
    random_integer = random.randint(0,3)
    switcher = {
        0: weapon_generation,
        1: shield_generation,
        2: grenade_mod_generation,
        3: relic_generation
    }
    return switcher.get(random_integer, 'nothing')
