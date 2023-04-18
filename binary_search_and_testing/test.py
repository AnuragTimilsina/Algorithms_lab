import unittest
from binary_search import binary_search



class test_binary_search(unittest.TestCase):

    ## Test the value found:
    def test_normal(self):
        test_values = [1, 2, 7, 9]
        result = binary_search(test_values, 9)
        self.assertEqual(result, 3)

    def test_repeated_list(self):
        test_values = [1, 1, 6, 7, 7, 9, 10]
        result = binary_search(test_values, 7)
        self.assertEqual(result, 3)

    def test_negative_list(self):
        test_values = [-1, -1, 6, 7, 7, 9, 10]
        result = binary_search(test_values, 7)
        self.assertEqual(result, 3)
    

if __name__ == "__main__":
    unittest.main()