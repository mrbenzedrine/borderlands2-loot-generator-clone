class Gear:

    def __init__(self, level, rarity, type, stats):

        # level: integer, character level requirement to use the piece of gear

        # rarity: string

        # type: string, each gear type (weapon, shield, relic etc) also has
        # their own different types (weapon: pistol, launcher, shield: adaptive,
        # nova etc)

        # stats: dict, contains all the data that make up the stats of the piece 
        # of gear

        self.level = level
        self.rarity = rarity
        self.type = type
        self.stats = stats
