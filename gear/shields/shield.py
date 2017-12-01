from . import general_shield_functions

class Shield:

    def __init__(self, manufacturer, parts, level, rarity, stats):

        # manufacturer: string; manufacturer of the shield,
        # 'Pangolin', 'Maliwan' etc

        # parts: dict; gives the manufacturer of each of the different
        # parts of the shield

        # level: integer; level requirement of the shield

        # rarity: string; 'White', 'Green' etc

        # stats: dict, contains data about the stats of the shield

        self.manufacturer = manufacturer
        self.type = 'shield' # just a regular shield with no special
        # effects
        self.parts = parts
        self.level = level
        self.rarity = rarity

        # Stats displayed in the item card that are common to all shield
        # types
        main_stats = stats['main_stats']

        # Stats that are specific to the shield type
        type_specific_stats = stats['type_specific_stats']

class AbsorbShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'absorb'

class AdaptiveShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'adaptive'

class AmplifyShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'amplify'

class BoosterShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'booster' 

class NovaShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'nova'

class SpikeShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'spike'

class RoidShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'roid'

class TurtleShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity, stats):

        super().__init__(manufacturer, parts, level, rarity, stats)
        self.type = 'turtle'
