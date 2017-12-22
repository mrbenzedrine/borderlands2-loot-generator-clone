import unittest
from unittest.mock import patch
from gear.class_mods import dlc_class_mod_generation

class TestDlcClassModGeneration(unittest.TestCase):

    def test_calculate_skill_point_changes(self):

        with patch.dict(dlc_class_mod_generation.assassin_class_mods, {'rogue': {'fixed_skills_to_boost': ['Like the Wind', 'Tw0 Fang', 'Vel0city']}}, clear=True):

            # Check that the appropriate number of skills to boost has been returned
            self.assertTrue(len(dlc_class_mod_generation.calculate_skill_point_changes('White', 1, 'assassin')) == 0)
            self.assertTrue(len(dlc_class_mod_generation.calculate_skill_point_changes('Green', 1, 'assassin')) == 1)
            self.assertTrue(len(dlc_class_mod_generation.calculate_skill_point_changes('Blue', 1, 'assassin')) == 2)
            self.assertTrue(len(dlc_class_mod_generation.calculate_skill_point_changes('Purple', 1, 'assassin')) == 3)

            # Check that assassin_class_mods has not been altered
            self.assertTrue(len(dlc_class_mod_generation.assassin_class_mods['rogue']['fixed_skills_to_boost']) == 3)
