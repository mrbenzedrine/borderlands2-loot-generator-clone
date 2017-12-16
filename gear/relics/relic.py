class Relic:

    def __init__(self, level, rarity, type, stats):

        # level: integer, the level requirement to use the item

        # rarity: string, rarity of the item

        # type: string, the type of the relic, eg. 'stockpile', 'elemental'

        # stats: dict, contains data about the stats of the relic

        self.level = level
        self.rarity = rarity
        self.type = type
        self.stats = stats

        # All relics are manufactured by the Eridians

        self.manufacturer = 'Eridian'

