import unittest
from src import register, unregister
from src.panels import LetItFountainPanel
from src.operators import InitializeFountainOperator, AddNozzleOperator
import bpy


class TestInit(unittest.TestCase):
    def test_register_unregister(self):
        register()
        self.assertEqual(bpy.types.LetItFountainPanel, LetItFountainPanel)

        unregister()
        self.assertFalse(hasattr(bpy.types, 'LetItFountainPanel'))


if __name__ == '__main__':
    unittest.main()
