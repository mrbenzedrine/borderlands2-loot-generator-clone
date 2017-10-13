class ClassMod:

    def __init__(self, level, rarity, character, stat_changes, skill_point_changes):

        # level: integer telling what the level requirement of the class 
        # mod is

        # rarity: string representing the rarity

        # character: string telling us which character this class mod is 
        # for

        # stat_changes: dict where the keys represent the name of the changed
        # stat and the values are also a string telling us how that stat has
        # been altered by the class mod

        # skill_point_changes: dict where the keys are strings denoting the
        # skills that have had extra points added to by the class mod and the
        # values are integers telling us how many extra points are added to
        # a particular skill


        self.level = level
        self.rarity = rarity
        self.character = character
        self.stat_changes = stat_changes
        self.skill_point_changes = skill_point_changes
