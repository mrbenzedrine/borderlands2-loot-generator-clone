import unittest
from gear.weapons import assault_rifle

class TestAssaultRifle(unittest.TestCase):

    def test_is_manufacturer_element_combo_valid(self):

        self.assertTrue(assault_rifle.is_manufacturer_element_combo_valid('Torgue', 'Explosion'))
        self.assertFalse(assault_rifle.is_manufacturer_element_combo_valid('Torgue', 'Corrosion'))

        self.assertFalse(assault_rifle.is_manufacturer_element_combo_valid('Bandit', 'Explosion'))
        self.assertTrue(assault_rifle.is_manufacturer_element_combo_valid('Bandit', 'None'))
