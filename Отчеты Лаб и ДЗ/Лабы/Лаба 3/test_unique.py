import unittest
from unique import Unique

class TestUnique(unittest.TestCase):

    def test_unique_integers(self):
        data = [1, 1, 2, 2, 3, 3]
        unique_iterator = Unique(data)
        result = list(unique_iterator)
        self.assertEqual(result, [1, 2, 3])

    def test_unique_strings_case_sensitive(self):
        data = ['a', 'A', 'b', 'B']
        unique_iterator = Unique(data)
        result = list(unique_iterator)
        self.assertEqual(result, ['a', 'A', 'b', 'B'])

    def test_unique_strings_ignore_case(self):
        data = ['a', 'A', 'b', 'B']
        unique_iterator = Unique(data, ignore_case=True)
        result = list(unique_iterator)
        self.assertEqual(result, ['a', 'b'])

if __name__ == '__main__':
    unittest.main()
