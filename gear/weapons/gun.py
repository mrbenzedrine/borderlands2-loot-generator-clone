from . import weapons_lvl1_base_stats
from . import weapons_stats_modifiers

class Gun:

    def __init__(self, type, parts, rarity, element, level, title, prefix):

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

        self.type = type
        self.parts = parts
        self.rarity = rarity
        self.element = element

        self.manufacturer = parts['body']

        # There'll be a probability calculator for the level of the
        # gun, for now just have it the same as the input we receive

        self.level = level

        self.stats = {

            'damage': self.calculate_damage(),
            'accuracy': self.calculate_accuracy(),
            'fire_rate': self.calculate_fire_rate(),
            'reload_speed': self.calculate_reload_speed(),
            'magazine_size': self.calculate_magazine_size()

        }

        self.title = title
        self.prefix = prefix

    def calculate_damage(self):
        return weapons_stats_modifiers.weapons_parts_stats_modifiers['body'][self.parts['body']]*15*weapons_stats_modifiers.level_modifer_function(self.level)*weapons_stats_modifiers.rarity_modifiers[self.rarity]

    def calculate_accuracy(self):
        return 10

    def calculate_fire_rate(self):
        return 10

    def calculate_reload_speed(self):
        return 10

    def calculate_magazine_size(self):
        return 10
    