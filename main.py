from gun import Gun
import weapon_generation

test_gun = weapon_generation.generate('E-Tech', 5)
print(test_gun.type)
print(test_gun.stats)
print(test_gun.parts)
print(test_gun.element)
test_gun_full_name = test_gun.prefix + ' ' + test_gun.title
print("Gun full name is", test_gun_full_name)