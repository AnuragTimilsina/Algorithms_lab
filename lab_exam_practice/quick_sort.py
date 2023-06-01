def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r): # Remember this!!! Python ko range le largest value 1 lee omit garxa. 
                          # So r - 1 pseudo code maa xa tara maile 1 rakhe.
        if A[j] <= x:
            i +=1
            # Less pythonic:
            # temp = A[i]
            # A[i] = A[j]
            # A[j] = temp

            # more pythonic:
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

if __name__ == '__main__':
    A = [5, 2, 7, 8, 10, 1]
    p = 0
    r = len(A) - 1
    print("array length: ", r)
    quickSort(A, p, r)
    print(A)


            