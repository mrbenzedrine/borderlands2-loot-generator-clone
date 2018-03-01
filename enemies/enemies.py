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

        for item in all_dropped_loot:
            self.dropped_loot[item['rarity']] += item['quantity']

        return self.dropped_loot

    def calculate_potential_loot_rarity(self):

        random_value = random.random()

        if random_value <= self.potential_loot_probabilities['Blue']:
            potential_rarity = 'Blue'
        elif random_value > self.potential_loot_probabilities['Blue'] and random_value <= self.potential_loot_probabilities['Blue'] + self.potential_loot_probabilities['Purple']:
            potential_rarity = 'Purple'
        elif random_value > self.potential_loot_probabilities['Blue'] + self.potential_loot_probabilities['Purple'] and random_value <= self.potential_loot_probabilities['Blue'] + self.potential_loot_probabilities['Purple'] + self.potential_loot_probabilities['Orange']:
            potential_rarity = 'Orange'
        else:
            potential_rarity = self.choose_white_or_green_rarity()

        return potential_rarity

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

        self.potential_loot_probabilities = {
            'Blue': 1/10,
            'Purple': 1/100,
            'Orange': 1/500
        }

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

        self.potential_loot_probabilities = {
            'Blue': 1/8,
            'Purple': 1/80,
            'Orange': 1/450
        }

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

        self.potential_loot_probabilities = {
            'Blue': 1/7,
            'Purple': 1/70,
            'Orange': 1/400
        }

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

        self.potential_loot_probabilities = {
            'Blue': 1/6,
            'Purple': 1/65,
            'Orange': 1/350
        }

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

        self.potential_loot_probabilities = {
            'Blue': 1/5,
            'Purple': 1/60,
            'Orange': 1/325
        }

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

        self.potential_loot_probabilities = {
            'Blue': 1/5,
            'Purple': 1/55,
            'Orange': 1/300
        }
