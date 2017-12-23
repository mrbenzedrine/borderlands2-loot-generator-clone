from ..gear import Gear

class ClassMod(Gear):

    def __init__(self, level, rarity, type, stats, character, prefix):

        # character: string telling us which character this class mod is 
        # for

        # prefix: string, the prefix (if any) of the class mod name

        super().__init__(level, rarity, type, stats)

        self.character = character
        self.prefix = prefix
