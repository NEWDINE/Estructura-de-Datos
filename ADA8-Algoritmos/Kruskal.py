class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.padre[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.padre[ry] = rx
            else:
                self.padre[ry] = rx
                self.rank[rx] += 1
            return True
        return False
def kruskal(n, aristas):
    aristas.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    costo = 0
    for u, v, w in aristas:
        if uf.union(u, v):
            mst.append((u, v, w))
            costo += w
    return mst, costo
aristas = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]
mst, costo = kruskal(6, aristas)
print("MST:", mst)
print("Costo total:", costo)
