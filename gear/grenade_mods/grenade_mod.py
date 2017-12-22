from ..gear import Gear

class GrenadeMod(Gear):

    def __init__(self, level, rarity, manufacturer, type, stats):

        # manufacturer: string, manufacturer of grenade

        super().__init__(level, rarity, type, stats)

        self.manufacturer = manufacturer
