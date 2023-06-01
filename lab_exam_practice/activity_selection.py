def activity_selection(a, s, f, n):
    A = [0] * n
    A[1] = a[1]

    k = 1
    iter = 1

    for i in range(2, n+1):
        if (s[i] >= f[k]):
            iter = iter + 1
            A[iter] = a[i]
            k = i

    '''
    Making first element of the list A (index 0) equal to iter
    just to know the length of the list when used in different function.
    '''

    A[0] = iter
    return A


if __name__ == '__main__':
  #Lists staring from 1. Elements at index 0 are fake
  a = [0, 2, 3, 5, 1, 4]
  s = [0, 0, 1, 3, 4, 1]
  f = [0, 2, 3, 4, 6, 6]
  p = activity_selection(a, s, f, 5)

  #p[0] is the length upto which activities are stored
  for i in range(1, p[0]+1):
    print(p[i])