def dfs_water_jug(cap1, cap2, target):
    start = (0, 0)
    stack = [(start, [start])]
    visited = set([start])
    while stack:
        (a, b), path = stack.pop()
        if a == target or b == target:
            return path
        next_states = []
        next_states.append((cap1, b))
        next_states.append((a, cap2))
        next_states.append((0, b))
        next_states.append((a, 0))
        pour = min(a, cap2 - b)
        next_states.append((a - pour, b + pour))
        pour = min(b, cap1 - a)
        next_states.append((a + pour, b - pour))
        for s in next_states:
            if s not in visited:
                visited.add(s)
                stack.append((s, path + [s]))
    return None

path = dfs_water_jug(4, 3, 2)
print(path)
