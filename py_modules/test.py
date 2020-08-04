import unittest
from .slugify import slugify


class PyModulesTest(unittest.TestCase):

    def test_slugify_cyrillic_string(self):
        slugified_str = slugify('строка на русском языке')
        self.assertEqual(slugified_str, 'stroka-na-russkom-yazike')
