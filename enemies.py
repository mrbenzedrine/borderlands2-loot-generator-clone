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
