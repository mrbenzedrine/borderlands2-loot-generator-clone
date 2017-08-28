from gun import Gun
from generate_gear import generate_weapon

test_gun_2 = generate_weapon('Purple', 5)
print(test_gun_2.type)
print(test_gun_2.stats)
print(test_gun_2.parts)
print(test_gun_2.element)
print("Gun title is ", test_gun_2.title)