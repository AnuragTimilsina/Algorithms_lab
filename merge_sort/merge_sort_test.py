import unittest
from merge_sort_python import mergeSort

class merge_sort_test(unittest.TestCase):

    def test_sort_normal(self):
        check_list = [51, 9, 23, 0, 3]
        sorted_list = [0, 3, 9, 23, 51]
        self.assertEqual(mergeSort(check_list), sorted_list)

    def test_sort_repeated(self):
        check_list = [51, 51, 9, 9, 10, 0, 1]
        sorted_list = [0, 1, 9, 9, 10, 51, 51]
        self.assertEqual(mergeSort(check_list), sorted_list)
    
    def test_sort_with_negative(self):
        check_list = [-1, -20, 3, -100, -1, -99]
        sorted_list = [-100, -99, -20, -1, -1, 3] 
        self.assertEqual(mergeSort(check_list), sorted_list)


if __name__ == '__main__':
    unittest.main()