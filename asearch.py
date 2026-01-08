def astar(start, goal):
    graph = {
        'A': [('P',1), ('B',4)],
        'P': [('G',3)],
        'B': [('C',2)],
        'C': [('G',2)],
        'G': [('T',2)],
        'T': [('J',1)],
        'J': []
    }

    h = {'A':7,'P':6,'B':6,'C':4,'G':2,'T':1,'J':0}

    open_set = {start}
    g = {start:0}
    parent = {start:start}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + h[x])

        if n == goal:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(start)
            path.reverse()
            print("Path found :",path)
            return path

        open_set.remove(n)

        for m,w in graph.get(n,[]):
            if m not in g or g[m] > g[n]+w:
                g[m]=g[n]+w
                parent[m]=n
                open_set.add(m)

    print("Path does not exist")
    return None


astar('A','J')