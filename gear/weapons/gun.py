from . import weapons_lvl1_base_stats
from . import weapons_stats_modifiers

class Gun:

    def __init__(self, type, parts, rarity, element, level, stats, title, prefix):

        # type: string; tells us the type of gun, 'pistol', 
        # 'SMG' etc

        # parts: dict; tells us the manufacturer of the
        # different parts of the gun, ie:
        # {'body': 'Hyperion', 'barrel': 'Maliwan', 'grip': 'Torgue', 
        # 'scope': 'Bandit'}

        # rarity: string, tells us the rarity of the gun,
        # 'white', 'green' etc

        # element: string, tells us the element of the gun,
        # if any, 'corrosive', 'incendiary' etc

        # level: integer that tells us the level of the enemy that
        # dropped the gun / the level of the area in which the chest
        # that the gun was found in

        # stats: dict, tells us the values of the stats that appear in the
        # item card

        self.type = type
        self.parts = parts
        self.rarity = rarity
        self.element = element

        self.manufacturer = parts['body']

        # There'll be a probability calculator for the level of the
        # gun, for now just have it the same as the input we receive

        self.level = level

        self.stats = stats

        self.title = title
        self.prefix = prefix
