class Shield:

    def __init__(self, manufacturer, parts, level, rarity, type, stats):

        # manufacturer: string; manufacturer of the shield,
        # 'Pangolin', 'Maliwan' etc

        # parts: dict; gives the manufacturer of each of the different
        # parts of the shield

        # level: integer; level requirement of the shield

        # rarity: string; 'White', 'Green' etc

        # type: string, gives the type of the shield

        # stats: dict, contains data about the stats of the shield

        self.manufacturer = manufacturer
        self.type = type
        self.parts = parts
        self.level = level
        self.rarity = rarity

        # Stats displayed in the item card that are common to all shield
        # types
        main_stats = stats['main_stats']

        # Stats that are specific to the shield type
        type_specific_stats = stats['type_specific_stats']
