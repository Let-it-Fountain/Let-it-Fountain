__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'

import unittest
import bpy


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, len(bpy.data.scenes))
        self.fail('Whoops')


if __name__ == '__main__':
    unittest.main()

