class GrenadeMod:

    def __init__(self, level, rarity, manufacturer, stats):

        # level: integer, level of grenade

        # rarity: string, rarity of grenade

        # manufacturer: string, manufacturer of grenade

        # stats: dict, contains data about the stats of the grenade

        self.level = level
        self.rarity = rarity
        self.manufacturer = manufacturer
        self.stats = stats

        # Stats displayed in top half of item card
        main_stats = stats['main_stats']

        # Other stats that are common to EVERY grenade type
        other_stats = stats['other_stats']

        # Stats that are specific to the type of grenade
        type_specific_stats = stats['type_specific_stats']

class AreaOfEffect(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, stats):

        super().__init__(level, rarity, manufacturer, stats)

class BouncingBetty(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, stats):

        super().__init__(level, rarity, manufacturer, stats)

class Transfusion(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, stats):

        super().__init__(level, rarity, manufacturer, stats)

class MIRV(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, stats):

        super().__init__(level, rarity, manufacturer, stats)

class Singularity(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, stats):

        super().__init__(level, rarity, manufacturer, stats)
