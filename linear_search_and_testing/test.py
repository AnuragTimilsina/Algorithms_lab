import unittest
from linear_search import linear_search

test_values = [1, 7, 2, 9]

class test_linear_search(unittest.TestCase):

    ## Test the value found:
    def value_check(self):
        result = linear_search(test_values, 9)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
