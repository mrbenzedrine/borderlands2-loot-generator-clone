class Chump:

    def __init__(self, level):

        # level: integer denoting what level the enemy is

        self.level = level
        self.loot_pool = (
            {
                'rarity': 'White',
                'quantity': 2
            },
            {
                'rarity': 'Green',
                'quantity': 1
            }
        )

class Badass:

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
            }
        )

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
