def mergeSort(arr):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        
        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

    # When all elements are traversed in either arr1 or arr2,
    # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

arr = [10, 9, 2, 4, 6, 13]
mergeSort(arr)
print(arr)