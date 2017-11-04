import weapon_generation
import shield_generation
import grenade_mod_generation
import class_mod_generation
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
        print("a: Gun\nb: Shield\nc: Grenade mod\nd: Class mod")

        choice = input()

        if(choice == 'a'):
            choose_gear_rarity_and_level(weapon_generation)
        elif(choice == 'b'):
            choose_gear_rarity_and_level(shield_generation)
        elif(choice == 'c'):
            choose_gear_rarity_and_level(grenade_mod_generation)
        elif(choice == 'd'):
            choose_gear_rarity_and_level(class_mod_generation)
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
            level = int(choice)

            return level

        rarity = choose_rarity()
        level = choose_level()

        # Now invoke the generate() function in the module passed to this
        # function

        piece_of_gear = gear_generation_module.generate(rarity, level)

    def choose_enemy_type_to_drop_loot():
        pass

    initial_choice()
