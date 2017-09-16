import weapon_generation
import shield_generation

test_shield = shield_generation.generate('Purple', 5)
print(test_shield.manufacturer)
print(test_shield.parts)
print(test_shield.level)
print(test_shield.rarity)
print(test_shield.type)