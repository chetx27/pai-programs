def unify(p1, p2):

if p1 == p2: 
return {} 
if len(p1) != len(p2) or p1[0] != p2[0]: return None 
return unify(p1[1:], p2[1:])

def resolution(clauses):

print("1.A v B\n2.~A v C\n3.~B v C")
c1, c2 = clauses [0], clauses [1]
for i, 11 in enumerate(c1):
 for j, 12 in enumerate(c2):
   if 12 == '~' + 11 or 11 == '~' + 12:

       res = [1 for k, 1 in enumerate(c1+c2) if k != i and k != len(c1)+i]
 print("Resolvent:",' v '.join(res))

return

clauses = [['A', 'B'], ['~A', 'C'], ['B', 'C]] resolution(clauses)