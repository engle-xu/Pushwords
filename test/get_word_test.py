import unittest

from lib.models import Words


class MyTestCase(unittest.TestCase):
    def test_get_unprocessed_words(self):
        self.assertEqual(Words.get_unprocessed_words(3), False)


if __name__ == '__main__':
    unittest.main()
