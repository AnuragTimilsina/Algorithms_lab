from merge_sort_python import mergeSort
import time


def generate_array(array_range):
    test_list = [i for i in range(array_range)]
    return test_list

def benchmark():
    
    for i in range(100000, 1000000, 100000):
        test_list = generate_array(i)
        start_time = time.time()
        mergeSort(test_list)
        end_time = time.time()
        print("Worst case sort time for {}th size array is: {}s".format(i, end_time-start_time))

benchmark()
