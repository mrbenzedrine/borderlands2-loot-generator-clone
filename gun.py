# I reckon a gun's stats should be calculatable from the
# different parts that make up the gun, so when setting
# the stats of the gun, each stat could potentially
# be the value of a method of the Gun class that calculates
# the stat based on the parts that the gun has?

# In order to generate a gun, you need a way to randomly 
# pick the parts that a Gun object needs, randomly choose
# an element and a weapon type, and since I saw that blog
# post from the devloeprs that said in Brderlands 2 you
# can specify the rairty of a wepaon drop, you explicitly
# PICK a rarity instead of randomising it like the other
# things

# Stats depend on rarity, level, and the manufacturer of
# the different parts of the gun, so perhaps there should
# be base stats for each gun type starting at level 1,
# then multplicative modifiers for the level of the gun, 
# the rarity level and also the different manufacturers 
# of the parts of the gun

# The mutiplier modifer for the level of a gun should be a
# function where you put into it the level and you get
# an output which is the modifier I reckon, I think I
# remember reading in that blog post that BL2 had an
# exponential increase in enemy health so I think the 
# weapons should also have the same increase otherwise the
# weapon damage wouldn't scale correctly?

from weapons_lvl1_base_stats import weapons_lvl1_base_stats
import weapons_stats_modifiers

class Gun:

    def __init__(self, type, parts, rarity, element, level, title):

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

        # I think it's best to generate the Title of the gun somewhere
        # in this initialisation function

        # print(weapons_stats_modifiers.rarity_modifiers)

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
    