from ..gear import Gear

class Gun(Gear):

    def __init__(self, type, parts, rarity, element, level, stats, title, prefix):

        # parts: dict; tells us the manufacturer of the
        # different parts of the gun, ie:
        # {'body': 'Hyperion', 'barrel': 'Maliwan', 'grip': 'Torgue', 
        # 'scope': 'Bandit'}

        # element: string, tells us the element of the gun,
        # if any, 'corrosive', 'incendiary' etc

        super().__init__(level, rarity, type, stats)

        self.parts = parts
        self.element = element

        self.manufacturer = parts['body']

        self.title = title
        self.prefix = prefix
