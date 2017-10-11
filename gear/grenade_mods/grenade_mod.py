class GrenadeMod:

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        # level: integer, level of grenade

        # rarity: string, rarity of grenade

        # manufacturer: string, manufacturer of grenade

        # element: string, element of grenade

        # delivery_mechanism: string, denotes the way the grendae travels
        # when thrown, ie, 'sticky', 'longbow', 'rubberised' etc

        self.level = level
        self.rarity = rarity
        self.manufacturer = manufacturer
        self.type = 'standard' # normal grenade with no special effects

        # Stats displayed in top half of item card
        # Will be calculatable from grenade parts eventually, but have
        # placeholder values for now
        main_stats = {
            'damage': 0,
            'blast_radius': 0,
            'fuse_time': 0
        }

        # Other stats that are common to EVERY grenade type
        other_stats = {
            'element': element,
            'delivery_mechanism': delivery_mechanism
        }

        # Stats that are specific to the type of grenade
        type_specific_stats = self.get_type_specific_stats()

        self.stats = {
            'main_stats': main_stats,
            'other_stats': other_stats,
            'type_specific_stats': type_specific_stats
        }

    def get_type_specific_stats(self):
        # No extra stats for standard grenade
        return 'none'
