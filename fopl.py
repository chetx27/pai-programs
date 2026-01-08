def unify(p1, p2):
    if p1 == p2: return {}
    if p1[0] != p2[0]: return None
    return unify(p1[1:], p2[1:]) if len(p1) == len(p2) else None

def resolution(clauses):
    print("1.AVB")
    print("2.~A v C")
    print("3.~B v C")
    c1, c2 = clauses[0], clauses[1]
    for i, l1 in enumerate(c1):
        for j, l2 in enumerate(c2):
            if l1[0] != '~' and l2[0] == '~'[1:] + l1[0]:
                new_clause = [l for k, l in enumerate(c1+c2) if k != i and k != len(c1)+j]
                print("Resolvent:", ' v '.join(new_clause))
                return

clauses = [['A', 'B'], ['~A', 'C'], ['~B', 'C']]
resolution(clauses)
