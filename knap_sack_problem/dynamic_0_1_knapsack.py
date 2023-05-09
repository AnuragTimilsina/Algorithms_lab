def knapSackDynamic(W, wt, val, n):
    K = K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build tаble K[][] in bоttоm uр mаnner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0  or  w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                        + K[i-1][w-wt[i-1]],
                            K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapSackDynamic(W, wt, val, n))