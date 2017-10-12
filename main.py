import weapon_generation
import shield_generation
import grenade_mod_generation
import loot_generation
from enemies.enemies import *

test_grenade = grenade_mod_generation.generate('Purple', 5)
print(test_grenade)
print(test_grenade.stats)
