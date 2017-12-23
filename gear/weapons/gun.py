from ..gear import Gear

class Gun(Gear):

    def __init__(self, level, rarity, type, stats, parts, element, title, prefix):

        # parts: dict; tells us the manufacturer of the
        # different parts of the gun, ie:
        # {'body': 'Hyperion', 'barrel': 'Maliwan', 'grip': 'Torgue', 
        # 'scope': 'Bandit'}

        # element: string, tells us the element of the gun,
        # if any, 'corrosive', 'incendiary' etc

        # title: string, the main part of the name of the weapon

        # prefix: string, the prefix (if any) of the name of the weapon

        super().__init__(level, rarity, type, stats)

        self.parts = parts
        self.element = element
        self.title = title
        self.prefix = prefix
        self.manufacturer = parts['body']
