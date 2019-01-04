def spiralNumbers(n):
    D = [1, 0]
    T = [[0, 1],
         [-1, 0]]
    k = 1
    r = 0
    c = 0
    out = [[0]*n for i in range(n)]
    while(k <= n**2):
        if 0<=r<n and 0<=c<n and  out[r][c] == 0:
            out[r][c] = k
            k += 1
        else:
            r = r - D[1]
            c = c - D[0]
            tmp = D[0]*T[0][0] + D[1]*T[1][0]
            D[1] = D[0]*T[0][1] + D[1]*T[1][1]
            D[0] = tmp
        r = r + D[1]
        c = c + D[0]
    return out
