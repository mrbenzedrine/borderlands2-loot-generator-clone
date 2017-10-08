import random

# Enemy class will only ever be used as a base for the other enemy classes
# to inherit from, attempting to use it by itself will cause errors as
# there are references to methods and attributes that will only exist
# when they're defined in the class inheriting from Enemy

class Enemy:

    def __init__(self, level):

        self.level = level

    def calculate_potential_loot_dropped(self):

        # Contains methods and attributes that will be defined in
        # the class that inherits from this Enemy class

        # Need to generate one piece of the potential loot

        generated_potential_loot = {
            'rarity': self.calculate_potential_loot_rarity(),
            'quantity': self.potential_loot_quantity
        }

        # Form a new tuple containing both the guaranteed loot pool and one 
        # piece of loot from the potential loot pool

        all_dropped_loot = self.guaranteed_loot_pool + (generated_potential_loot,)

        return all_dropped_loot

class Chump(Enemy):

    def __init__(self, level):

        # level: integer denoting what level the enemy is

        super().__init__(level)

        self.guaranteed_loot_pool = (
            {
                'rarity': 'White',
                'quantity': 2
            },
            {
                'rarity': 'Green',
                'quantity': 1
            }
        )

        self.potential_loot_quantity = 1

        # Not sure yet how to use this data to generate the same 
        # functionality as the calculate_potential_loot_rarity() method

        # self.potential_loot_pool = (
        #     {
        #         'rarity': 'Blue',
        #         'probability': 1/10
        #     },
        #     {
        #         'rarity': 'Purple',
        #         'probability': 1/100
        #     },
        #     {
        #         'rarity': 'Orange',
        #         'probability': 1/500
        #     },
        #     {
        #         'rarity': 'Other', # meaning the raritites in the guaranteed rarity pool 
        #         'probability': 1 - (1/10 + 1/100 + 1/500)
        #     }   
        # )

    def calculate_potential_loot_rarity(self):

        # Need to do a probability roll on what should the item be from
        # the potential loot pool

        random_value = random.random()

        if(random_value <= 1/10):
            potential_rarity = 'Blue'
        elif(random_value > 1/10 and random_value <= 1/10 + 1/100):
            potential_rarity = 'Purple'
        elif(random_value > 1/10 + 1/100 and random_value <= 1/10 + 1/100 + 1/500):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_potential_rarity_from_guaranteed_loot_rarity()

        return potential_rarity

    def choose_potential_rarity_from_guaranteed_loot_rarity(self):
        random_integer = random.randint(0,1)
        switcher = {
            0: 'White',
            1: 'Green'
        }
        return switcher.get(random_integer, 'nothing')

class Badass(Enemy):

    def __init__(self, level):

        super().__init__(level)

        self.guaranteed_loot_pool = (
            {
                'rarity': 'White',
                'quantity': 2
            },
            {
                'rarity': 'Green',
                'quantity': 2
            }
        )

        self.potential_loot_quantity = 1

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if(random_value <= 1/8):
            potential_rarity = 'Blue'
        elif(random_value > 1/8 and random_value <= 1/8 + 1/80):
            potential_rarity = 'Purple'
        elif(random_value > 1/8 + 1/80 and random_value <= 1/8 + 1/80 + 1/450):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_potential_rarity_from_guaranteed_loot_rarity()

        return potential_rarity

    def choose_potential_rarity_from_guaranteed_loot_rarity(self):
        random_integer = random.randint(0,1)
        switcher = {
            0: 'White',
            1: 'Green'
        }
        return switcher.get(random_integer, 'nothing')

class SuperBadass():

    def __init__(self, level):

        self.level = level
        self.loot_pool = (
            {
                'rarity': 'White',
                'quantity': 2
            },
            {
                'rarity': 'Green',
                'quantity': 2
            },
            {
                'rarity': 'Blue',
                'quantity': 1
            }
        )

class UltimateBadass():

    def __init__(self, level):

        self.level = level
        self.loot_pool = (
            {
                'rarity': 'White',
                'quantity': 2
            },
            {
                'rarity': 'Green',
                'quantity': 2
            },
            {
                'rarity': 'Blue',
                'quantity': 2
            },
            {
                'rarity': 'Purple',
                'quantity': 1
            }
        )

class Chubby():

    def __init__(self, level):

        self.level = level
        self.loot_pool = (
            {
                'rarity': 'Green',
                'quantity': 2
            },
            {
                'rarity': 'Blue',
                'quantity': 1
            },
            {
                'rarity': 'Purple',
                'quantity': 1
            },
            {
                'rarity': 'Orange',
                'quantity': 1
            }
        )

class RaidBoss():

    def __init__(self, level):

        self.level = level
        self.loot_pool = (
            {
                'rarity': 'White',
                'quantity': 3
            },
            {
                'rarity': 'Green',
                'quantity': 3
            },
            {
                'rarity': 'Blue',
                'quantity': 3
            },
            {
                'rarity': 'Purple',
                'quantity': 2
            },
            {
                'rarity': 'Orange',
                'quantity': 1
            }        
        )
