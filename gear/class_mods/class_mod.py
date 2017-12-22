from ..gear import Gear

class ClassMod(Gear):

    def __init__(self, level, rarity, character, type, prefix, stats):

        # character: string telling us which character this class mod is 
        # for

        super().__init__(level, rarity, type, stats)

        self.character = character
        self.prefix = prefix
