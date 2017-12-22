class ClassMod:

    def __init__(self, level, rarity, character, type, prefix, stats):

        # level: integer telling what the level requirement of the class 
        # mod is

        # rarity: string representing the rarity

        # character: string telling us which character this class mod is 
        # for

        # stats: dict giving the stats changes of the class mod, and the
        # skill point changes

        self.level = level
        self.rarity = rarity
        self.character = character
        self.type = type
        self.prefix = prefix
        self.stats = stats
