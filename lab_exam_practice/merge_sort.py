def mergeSort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [i for i in range(n1+1)]
    R = [i for i in range(n2+1)]
    for i in range(0, n1):
        L[i] = A[p + i -1]
    for j in range(0, n2):
        R[j] = A[q+j]
    L[n1] = 10000000
    R[n2] = 10000000
    i = 1
    j = 1
    for k in range(p, r): 
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


if __name__ == '__main__':
    A = [1, 2, 5, 7, 8, 10]
    p = 0
    r = len(A) - 1
    print("array length: ", r)
    mergeSort(A, p, r)
    print(A)
