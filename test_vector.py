from unittest import TestCase
from vector import vector


class Testvector(TestCase):
    def test_add_element(self):
        vector1 = vector()
        vector1.add_element('hello')
        self.assertEqual(vector1.debug_array(), ['hello'])

    def test_remove_element(self):
        vector1 = vector()
        vector1.add_element('Hello')
        self.assertEqual(vector1.remove_element(), None)
