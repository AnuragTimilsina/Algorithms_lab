def sort_insertion(my_list):
    for j in range(1, len(my_list)):
        key = my_list[j]
        # Insert A[J] into the sorted sequence A[0...j-1]
        i = j - 1
        while i > -1 and my_list[i] > key:
            my_list[i+1] = my_list[i]
            i = i - 1
        my_list[i+1] = key
    return my_list


my_list = [-1, -20, 3, -100, -1, -99]
print(sort_insertion(my_list))
            
