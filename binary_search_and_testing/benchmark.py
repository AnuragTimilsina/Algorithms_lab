from binary_search import binary_search
import time


def generate_array(array_range):
    test_list = [i for i in range(array_range)]
    test_list.sort()
    return test_list

def benchmark():
    
    for i in range(10000000, 100000000, 10000000):
        test_list = generate_array(i)
        start_time = time.time()
        binary_search(test_list, i-10000)
        end_time = time.time()
        print("Worst case search time for {}th size array is: {}s".format(i, end_time-start_time))

benchmark()