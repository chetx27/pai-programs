import heapq

def tsp_nearest_neighbor(dist):
    n = len(dist)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    current = 0
    
    for _ in range(n - 1):
        next_city = -1
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and dist[current][city] < min_dist:
                min_dist = dist[current][city]
                next_city = city
        tour.append(next_city)
        visited[next_city] = True
        current = next_city
    
    tour.append(0)
    return tour, sum(dist[tour[i]][tour[i+1]] for i in range(n))

dist = [
    [0, 20, 42, 35, 100],
    [20, 0, 30, 34, 80],
    [42, 30, 0, 12, 81],
    [35, 34, 12, 0, 79],
    [100, 80, 81, 79, 0]
]

tour, length = tsp_nearest_neighbor(dist)
print(f"Tour: {tour}")
print(f"Tour length: {length}")
