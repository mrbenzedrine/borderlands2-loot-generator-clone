import unittest
from gear.weapons import launcher

class TestLauncher(unittest.TestCase):

    def test_is_manufacturer_element_combo_valid(self):

        self.assertTrue(launcher.is_manufacturer_element_combo_valid('Torgue', 'Explosion'))
        self.assertFalse(launcher.is_manufacturer_element_combo_valid('Vladof', 'None'))
