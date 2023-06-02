def lcs_length(a, b):
    m = len(a)
    n = len(b)
    # Empty matrix
    L = [[0 for x in range(n+1)] for x in range(m+1)] 

    # Building the matrix in bottom-up way
    for i in range(m+1):  
        for j in range(n+1):
            if i ==0 or j ==0:
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # Output:
    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n

    while i > 0 and j > 0:

        if a[i-1] == b[j-1]:
            lcs_algo[index-1] = a[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("The LCS is: ", lcs_algo)

    return L


S1 = "ACADB"
S2 = "CBDA"
result = lcs_length(S1, S2)

for i in result:
    print(i)
    print()



    