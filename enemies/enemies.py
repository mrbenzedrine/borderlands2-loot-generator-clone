import random

# Enemy class will only ever be used as a base for the other enemy classes
# to inherit from, attempting to use it by itself will cause errors as
# there are references to methods and attributes that will only exist
# when they're defined in the class inheriting from Enemy

class Enemy:

    def __init__(self, level):

        self.level = level
        self.dropped_loot = {
            'White': 0,
            'Green': 0,
            'Blue': 0,
            'Purple': 0,
            'Orange': 0
        }

    def drop_loot(self):

        all_dropped_loot = self.guaranteed_loot_pool + self.calculate_potential_loot_dropped()

        # Now need to iterate through all_dropped_loot and increment the
        # corresponding rarity quantity

        for x in range(0, len(all_dropped_loot)):
            self.dropped_loot[all_dropped_loot[x]['rarity']] = self.dropped_loot[all_dropped_loot[x]['rarity']] + all_dropped_loot[x]['quantity']

        return self.dropped_loot

    def calculate_potential_loot_dropped(self):

        # Contains methods and attributes that will be defined in
        # the class that inherits from this Enemy class

        potential_loot_array = []

        for x in range(0, self.potential_loot_quantity):
            generated_potential_loot = {
                'rarity': self.calculate_potential_loot_rarity(),
                'quantity': 1
            }
            potential_loot_array.append(generated_potential_loot)

        potential_loot_tuple = tuple(potential_loot_array)

        return potential_loot_tuple

    def choose_white_or_green_rarity(self):

        random_value = random.random()

        if(random_value < 0.55):
            rarity = 'White'
        else:
            rarity = 'Green'

        return rarity

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
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

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
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

class SuperBadass(Enemy):

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
            },
            {
                'rarity': 'Blue',
                'quantity': 1
            }
        )

        self.potential_loot_quantity = 1

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if(random_value <= 1/7):
            potential_rarity = 'Blue'
        elif(random_value > 1/7 and random_value <= 1/7 + 1/70):
            potential_rarity = 'Purple'
        elif(random_value > 1/7 + 1/70 and random_value <= 1/7 + 1/70 + 1/400):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

class UltimateBadass(Enemy):

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

        self.potential_loot_quantity = 1

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if(random_value <= 1/6):
            potential_rarity = 'Blue'
        elif(random_value > 1/6 and random_value <= 1/6 + 1/65):
            potential_rarity = 'Purple'
        elif(random_value > 1/6 + 1/65 and random_value <= 1/6 + 1/65 + 1/350):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

class Chubby(Enemy):

    def __init__(self, level):

        super().__init__(level)

        self.guaranteed_loot_pool = (
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

        self.potential_loot_quantity = 1

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if(random_value <= 1/5):
            potential_rarity = 'Blue'
        elif(random_value > 1/5 and random_value <= 1/5 + 1/60):
            potential_rarity = 'Purple'
        elif(random_value > 1/5 + 1/60 and random_value <= 1/5 + 1/60 + 1/325):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

class RaidBoss(Enemy):

    def __init__(self, level):

        super().__init__(level)

        self.guaranteed_loot_pool = (
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

        self.potential_loot_quantity = 4

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if(random_value <= 1/5):
            potential_rarity = 'Blue'
        elif(random_value > 1/5 and random_value <= 1/5 + 1/55):
            potential_rarity = 'Purple'
        elif(random_value > 1/5 + 1/55 and random_value <= 1/5 + 1/55 + 1/300):
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity
