import weapon_generation
import shield_generation
import grenade_mod_generation
import class_mod_generation
import relic_generation
import loot_generation
from enemies.enemies import *

while True:

    def initial_choice():

    # Choose between generating a single piece of gear or a loot drop
    # from an enemy

        print("\nWould you like to generate a single piece of gear, or a loot drop from an enemy?")
        print("Please select an option below:" )
        print("a: Single piece of gear")
        print("b: Loot drop from an enemy")

        choice = input()

        if(choice == 'a'):
            choose_gear_type_to_generate()
        elif(choice == 'b'):
            choose_enemy_type_to_drop_loot()
        else:
            print("Invalid choice, please choose a valid choice")
            initial_choice()

    def choose_gear_type_to_generate():

        print("\nPlease choose a piece of gear to generate from the options below:")
        print("a: Gun\nb: Shield\nc: Grenade mod\nd: Class mod\ne: Relic")

        choice = input()

        if(choice == 'a'):
            choose_gear_rarity_and_level(weapon_generation)
        elif(choice == 'b'):
            choose_gear_rarity_and_level(shield_generation)
        elif(choice == 'c'):
            choose_gear_rarity_and_level(grenade_mod_generation)
        elif(choice == 'd'):
            choose_gear_rarity_and_level(class_mod_generation)
        elif(choice == 'e'):
            choose_gear_rarity_and_level(relic_generation)
        else:
            print("Invalid choice, please choose a valid choice")
            choose_gear_type_to_generate()

    def choose_gear_rarity_and_level(gear_generation_module):

        def choose_rarity():

            print("\nPlease choose a rarity from the options below:")
            print("a: White\nb: Green\nc: Blue\nd: Purple")

            choice = input()

            switcher = {
                'a': 'White',
                'b': 'Green',
                'c': 'Blue',
                'd': 'Purple'
            }

            rarity = switcher.get(choice, 'nothing')

            if(rarity == 'nothing'):
                print("Invald choice, please choose a valid choice")
                choose_rarity()

            return rarity

        def choose_level():

            print("\nPlease input the level of the piece of gear")

            choice = input()

            try:
                level = int(choice)
                if level <= 0:
                    raise ValueError("The level must be a positive integer.")
            except ValueError:
                print("The level must be a positive integer.")
                return choose_level()

            return level

        rarity = choose_rarity()
        level = choose_level()

        # Now invoke the generate() function in the module passed to this
        # function

        piece_of_gear = gear_generation_module.generate(rarity, level)

    def choose_enemy_type_to_drop_loot():
        
        print("\nPlease choose a type of enemy from the options below to generate a loot drop from:")
        print("a: Chump\nb: Badass\nc: Super Badass\nd: Ultimate Badass\ne: Chubby/Tubby\nf: Raid Boss")

        choice = input()

        switcher = {
            'a': 'Chump',
            'b': 'Badass',
            'c': 'Super Badass',
            'd': 'Ultimate Badass',
            'e': 'Chubby/Tubby',
            'f': 'Raid Boss'
        }

        enemy_type = switcher.get(choice, 'nothing')

        if(enemy_type == 'nothing'):
            print("Invald choice, please choose a valid choice")

        enemy_class_switcher = {
            'Chump': Chump,
            'Badass': Badass,
            'Super Badass': SuperBadass,
            'Ultimate Badass': UltimateBadass,
            'Chubby/Tubby': Chubby,
            'Raid Boss': RaidBoss
        }

        enemy_class = enemy_class_switcher.get(enemy_type, 'nothing')
        enemy = enemy_class(1) # just set to level 1 for now
        loot = loot_generation.enemy_loot_generation(enemy)
        print(loot)

    initial_choice()
