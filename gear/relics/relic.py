from ..gear import Gear

class Relic(Gear):

    def __init__(self, level, rarity, type, stats):

        super().__init__(level, rarity, type, stats)

        # All relics are manufactured by the Eridians

        self.manufacturer = 'Eridian'

