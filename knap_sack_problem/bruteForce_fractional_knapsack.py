def fractionalKnapsackBruteforce(values,weights,Total_capacity):
    n = len(values)

    def score(i) : return values[i]/weights[i]

    items = sorted(range(n)  , key=score , reverse = True)
    sel, value,weight = [],0,0
    for i in items:
        if weight +weights[i] <= Total_capacity:
            sel += [i]
            weight += weights[i]
            value += values [i]
    return value


if __name__ == '__main__':
    values = [60, 100, 20]
    weights = [100, 200, 300]
    bag_size = 40
    print(fractionalKnapsackBruteforce(values, weights, bag_size))