import weapon_generation
import shield_generation
import loot_generation
import enemies

test_enemy = enemies.Chump(1)
test_loot = loot_generation.enemy_loot_generation(test_enemy)
print(test_loot)
