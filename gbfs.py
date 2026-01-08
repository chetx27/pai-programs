from heapq import heappush, heappop

M = C = 3

def valid(s):
    ml, cl, _ = s
    mr, cr = M-ml, C-cl
    if not (0 <= ml <= M and 0 <= cl <= C): return False
    if ml > 0 and cl > ml: return False
    if mr > 0 and cr > mr: return False
    return True

def goal(s):
    return s == (0,0,False)

def h(s):
    return s[0] + s[1]

def successors(s):
    ml, cl, b = s
    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
    res = []
    for m,c in moves:
        if b:
            n = (ml-m, cl-c, False)
            d = f"Move {m}M {c}C L->R"
        else:
            n = (ml+m, cl+c, True)
            d = f"Move {m}M {c}C R->L"
        if valid(n):
            res.append((n,d))
    return res

def greedy():
    start = (3,3,True)
    pq = []
    heappush(pq,(h(start),start))
    parent = {start:(None,None)}
    seen = set()
    while pq:
        _, s = heappop(pq)
        if s in seen: continue
        seen.add(s)
        if goal(s):
            path=[]
            while s:
                p,m = parent[s]
                path.append((s,m))
                s=p
            return path[::-1]
        for n,mv in successors(s):
            if n not in parent:
                parent[n]=(s,mv)
                heappush(pq,(h(n),n))

path = greedy()

def fmt(s):
    m,c,b = s
    return f"{m}M,{c}C,{'B' if b else '-'}"

for i,(s,mv) in enumerate(path):
    ml,cl,b = s
    mr,cr = 3-ml,3-cl
    if i==0:
        print(f"Step {i}: L=({fmt(s)}) R=({fmt((mr,cr,0))})")
    else:
        print(f"Step {i}: {mv} --> L=({fmt(s)}) R=({fmt((mr,cr,0))})")