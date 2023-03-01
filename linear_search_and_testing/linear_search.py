def linear_search(values, target):
    n = len(values)
    for i in range(n):
        if values[i] == target:
            return i
    return -1


# List comprehension:

def linear_search_comprehension(values, target):
    result = [i for i in range(len(values)) if values[i]==target][0]
    return result


if __name__ == "__main__":
    print(linear_search([1,4,2,8,9], 9))
    print(linear_search_comprehension([1, 4 ,2, 8, 9], 9))
