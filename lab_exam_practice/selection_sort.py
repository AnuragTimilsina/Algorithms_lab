def selectionSort(A):
    for i in range(len(A)):
        m = i
        for j in range(i+1, len(A)):
            if A[j] < A[m]:
                m = j
        temp = A[i]
        A[i] = A[m]
        A[m] = temp


if __name__ == '__main__':
    A = [5, 2, 7, 8, 10, 1]
    selectionSort(A)
    print(A)