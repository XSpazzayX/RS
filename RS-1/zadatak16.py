"""
Napišite funkciju dijkstra(graph, start) koja prima graf predstavljen kao rječnik susjedstva i 
početni čvor te vraća rječnik s najkraćim udaljenostima od početnog čvora do svih 
ostalih čvorova u grafu koristeći Dijsktra algoritam.

Za rješavanje zadatka možete koristiti modul heapq za gotovu implementaciju prioritetnog reda.

Primjer ulaznih podataka

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

Primjer poziva funkcije:

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, D': 4}
"""


import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def main():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}


if __name__ == "__main__":
    main()