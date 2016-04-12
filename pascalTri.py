def pascal(numRows):
    p = [[1]*(i + 1) for i in range (numRows)]
    for i in range(numRows):
        for j in range(1, i):
            p[i][j] = p[i-1][j-1] + p[i-1][j]
    return p
