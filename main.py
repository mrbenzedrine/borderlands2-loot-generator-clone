import weapon_generation
import shield_generation
import loot_generation
from enemies.enemies import *

test_enemy = SuperBadass(1)
test_loot = loot_generation.enemy_loot_generation(test_enemy)
print(test_loot)
