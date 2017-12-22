from ..gear import Gear

class Shield(Gear):

    def __init__(self, manufacturer, parts, level, rarity, type, stats):

        # manufacturer: string; manufacturer of the shield,
        # 'Pangolin', 'Maliwan' etc

        # parts: dict; gives the manufacturer of each of the different
        # parts of the shield

        super().__init__(level, rarity, type, stats)

        self.manufacturer = manufacturer
        self.parts = parts
