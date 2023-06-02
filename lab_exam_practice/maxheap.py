def maxheapify(A, i, end):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < end and A[left] > A[largest]:
        largest = left

    if right < end and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, largest, end)


def heap(A, n):
    for i in range(n // 2, -1, -1):
        maxheapify(A, i, n)

    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        maxheapify(A, 0, i)


a = [2, 4, 12, 1, 9, 100, 50, 200, 2000, 50000,150]
heap(a, len(a))
print(a)
