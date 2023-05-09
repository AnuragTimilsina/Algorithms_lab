class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def fractionalKnapsackGreedy(W, arr):
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    finalvalue = 0.0

    for item in arr:
        # Add all if not full capacity.
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit

        # Add fractional part if can't add completely. 
        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue


# Driver Code
if __name__ == "__main__":
    W = 100
    arr = [Item(60, 1000), Item(100, 200), Item(120, 300)]
 
    max_val = fractionalKnapsackGreedy(W, arr)
    print(max_val)