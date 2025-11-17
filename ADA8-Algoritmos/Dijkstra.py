import heapq
def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    visitados = set()
    heap = [(0, inicio)]
    while heap:
        distancia_actual, nodo = heapq.heappop(heap)
        if nodo in visitados:
            continue
        visitados.add(nodo)
        for vecino, peso in grafo[nodo].items():
            nueva_dist = distancia_actual + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(heap, (nueva_dist, vecino))
    return dist
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'F': 11},
    'E': {'D': 4},
    'F': {}
}
print(dijkstra(grafo, 'A'))
