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

class AreaOfEffect(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        super().__init__(level, rarity, manufacturer, element, delivery_mechanism)
        self.type = 'area_of_effect'

    def get_type_specific_stats(self):
        return {
            'damage_per_sec': self.calculate_damage_per_sec()
        }

    def calculate_damage_per_sec(self):
        # AoE grenades cannot be explosive, so this stat will always be 
        # relevant/non-zero unlike bouncing betties which CAN be explosive
        return 0

class BouncingBetty(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        super().__init__(level, rarity, manufacturer, element, delivery_mechanism)
        self.type = 'bouncing_betty'

    def get_type_specific_stats(self):
        return {
            'damage_per_sec': self.calculate_damage_per_sec()
        }

    def calculate_damage_per_sec(self):
        # Bouncing betties can be explosive, in which case this stat
        # is irrelevant, so it'll just be zero if the element of the
        # grenade is explosive
        return 0

class Transfusion(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        super().__init__(level, rarity, manufacturer, element, delivery_mechanism)
        self.type = 'transfusion'

    def get_type_specific_stats(self):
        return {
            'no_of_child_grenades': self.calculate_no_of_child_grenades()
            'healing_percentage': self.calculate_healing_percentage()
        }

    def calculate_no_of_child_grenades(self):
        # Will likely have a probability roll that is depends to some
        # degree on the rarity that'll determine the no. of child grenades,
        # but have placeholder value for now
        return 0

    def calculate_healing_percentage(self):
        # Determines what percentage of the damage inflicted is converted
        # into the healing health orbs
        return 0

class MIRV(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        super().__init__(level, rarity, manufacturer, element, delivery_mechanism)
        self.type = 'mirv'

    def get_type_specific_stats(self):
        return {
            'no_of_child_grenades': self.calculate_no_of_child_grenades()
        }

    def calculate_no_of_child_grenades(self):
        return 0

class Singularity(GrenadeMod):

    def __init__(self, level, rarity, manufacturer, element, delivery_mechanism):

        super().__init__(level, rarity, manufacturer, element, delivery_mechanism)
        self.type = 'singularity'

    def get_type_specific_stats(self):
        return {
            'damage_per_sec': self.calculate_damage_per_sec()
        }

    def calculate_damage_per_sec(self):
        # Singularity grenades can be explosive too, and in that case 
        # this stat is irrelevant, so it'll just be zero if the element 
        # of the grenade is explosive
        return 0
