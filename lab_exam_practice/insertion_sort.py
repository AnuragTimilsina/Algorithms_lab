def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1--j-1]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

if __name__ == '__main__':
    A = [5, 2, 7, 8, 10, 1]
    insertion_sort(A)
    print(A)