def warshall(M):
    n = len(M)
    R = [fila[:] for fila in M]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])
    return R
M = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]
resultado = warshall(M)
for fila in resultado:
    print(fila)