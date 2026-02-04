dist = [
    [0, 20, 42, 35, 100],
    [20, 0, 30, 34, 80],
    [42, 30, 0, 12, 81],
    [35, 34, 12, 0, 79],
    [100, 80, 81, 79, 0]
]

tour = [0]
unvisited = [1, 2, 3, 4]

while unvisited:
    next_node = min(unvisited, key=lambda x: dist[tour[-1]][x])
    tour.append(next_node)
    unvisited.remove(next_node)

tour.append(0)
length = sum(dist[tour[i]][tour[i+1]] for i in range(len(dist)))

print(f"Tour: {tour}")
print(f"Tour length: {length}")