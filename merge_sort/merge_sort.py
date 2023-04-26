def sort_merge(my_list, p, r):
    if p<r:
        q = int((p+r)/2)
        sort_merge(my_list, p, q)
        sort_merge(my_list, q+1, r)
        merge(my_list, p, q, r)
        return my_list

def merge(my_list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left_list = [0] * n1
    print("left: ",left_list)
    right_list = [0] * n2
    print("right: ",right_list)
    for i in range(0, n1):
        left_list[i] = my_list[p+i-1]
    for j in range(0, n2):
        right_list[j] = my_list[q+j]
    left_list.append(100000000000)
    right_list.append(100000000000)
    i = 0
    j = 0
    for k in range(p, r):
        if left_list[i] <= right_list[j]:
            my_list[k] = left_list[i]
            i = i + 1
        else:
            my_list[k] = right_list[j]
            j = j + 1  

my_list = [1, 3, 4, 2, 5]
print(sort_merge(my_list, 0, len(my_list)))
