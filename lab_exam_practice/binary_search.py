def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0

    while left<=right:
        mid = (right + left) // 2

        # If x is greater, ignore left half
        if arr[mid] <x:
            left = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            right = mid - 1

        # Means x is present at mid
        else: 
            return mid
        
    # If we reach here, then the element was not present
    return -1

if __name__ == "__main__":
    print(f"The target is in the index: {binary_search([1,4,2,8,9,10,2,3], 9)}")