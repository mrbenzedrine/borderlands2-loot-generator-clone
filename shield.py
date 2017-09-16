class Shield:

    def __init__(self, manufacturer, parts, level, rarity):

        # manufacturer: string; manufacturer of the shield,
        # 'Pangolin', 'Maliwan' etc

        # parts: dict; gives the manufacturer of each of the different
        # parts of the shield

        # level: integer; level requirement of the shield

        # rarity: string; 'White', 'Green' etc

        self.manufacturer = manufacturer
        self.type = 'shield' # just a regular shield with no special
        # effects
        self.parts = parts
        self.level = level
        self.rarity = rarity

        # Stats will be calculated from the different parts of the shield,
        # but have placeholder values for now

        self.stats = {

            'capacity': 0,
            'recharge_rate': 0,
            'recharge_delay': 0

        }

        self.extra_stats = self.get_extra_stats()

    def get_extra_stats(self):
        # Regula shields have no extra stats (if we disregard 
        # possible elemental resistance / immunity for now),
        # so let us just return the string 'none' for now
        return 'none'

class AbsorbShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'absorb'

    def get_extra_stats(self):
        return {
            'absorb_chance': self.calculate_absorb_chance()
        }

    def calculate_absorb_chance(self):
        # Placeholder value for now, instead of a calculation
        return 0

class AdaptiveShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'adaptive'

    def get_extra_stats(self):
        return {
            'elemental_resistance': self.calculate_elemental_resistance(),
            'max_health_increase': self.calculate_max_health_increase()
        }

    def calculate_elemental_resistance(self):
        # Placeholder value for now, instead of a calculation
        return 0

    def calculate_max_health_increase(self):
        # Placeholder value for now, instead of a calculation
        return 0  

class AmplifyShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'amplify'

    def get_extra_stats(self):
        return {
            'amp_damage': self.calculate_amp_damage(),
            'amp_shot_drain': self.calculate_amp_shot_drain()
        }

    def calculate_amp_damage(self):
        # Placeholder value for now, instead of a calculation
        return 0

    def calculate_amp_shot_drain(self):
        # Placeholder value for now, instead of a calculation
        return 0

class BoosterShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'booster'

    def get_extra_stats(self):
        return {
            'booster_chance': self.calculate_booster_chance()
        }

    def calculate_booster_chance(self):
        # Placeholder value for now, instead of a calculation
        return 0    

class NovaShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'nova'

    def get_extra_stats(self):
        return {
            'element': 'none', # not listed in the item card's
            # stats, but instead in the item card description

            # Also need to generate an element, and will need to be
            # constrained in some fashion to ashere to what elements
            # it can be

            'nova_damage': self.calculate_nova_damage(),
            'nova_radius': self.calculate_nova_radius()
        }

    def calculate_nova_damage(self):
        # Placeholder value for now, instead of a calculation
        return 0

    def calculate_nova_radius(self):
        # Placeholder value for now, instead of a calculation
        return 0

class SpikeShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'spike'

    def get_extra_stats(self):
        return {
            'element': 'none', # not listed in the item card's
            # stats, but instead in the item card description

            # Same deal as the element geenration in NovaShield class

            'spike_damage': self.calculate_spike_damage()
        }

    def calculate_spike_damage(self):
        # Placeholder value for now, instead of a calculation
        return 0

class RoidShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'roid'

    def get_extra_stats(self):
        return {
            'roid_damage': self.calculate_roid_damage()
        }

    def calculate_roid_damage(self):
        # Placeholder value for now, instead of a calculation
        return 0

class TurtleShield(Shield):

    def __init__(self, manufacturer, parts, level, rarity):

        super().__init__(manufacturer, parts, level, rarity)
        self.type = 'turtle'

    def get_extra_stats(self):
        return {
            'capacity_increase': self.calculate_capacity_increase(),
            # EVen though capacity increase isn't a separate attribute
            # in the item card, it makes sense to have an attribute
            # to show the capacity increase due to the type being a
            # turtle shield
            'max_health_decrease': self.calculate_max_health_decrease()
        }

    def calculate_capacity_increase(self):
        # Placeholder value for now, instead of a calculation
        return 0

    def calculate_max_health_decrease(self):
        # Placeholder value for now, instead of a calculation
        return 0
