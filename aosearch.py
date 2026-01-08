H = {'A':-1,'B':5,'C':2,'D':4,'E':7,'F':9,'G':3,'H':0,'I':0,'J':0}
conds = {
'A':{'OR':['B'],'AND':['C','D']},
'B':{'OR':['E','F']},
'C':{'OR':['G'],'AND':['H','I']},
'D':{'OR':['J']}
}
def cst(n):
    d = conds[n]
    res = {}
    if 'AND' in d: res[' AND '.join(d['AND'])] = sum(H[x] for x in d['AND'])+1
    if 'OR' in d: res[' OR '.join(d['OR'])] = min(H[x] for x in d['OR'])+1
    print(f"{n}:{{{d}}}>>>{{cst}}".replace('cst',str(res)))
    return min(res.values())
for n in 'DCBA':
    H[n] = cst(n)
print('Shortest Path: A<--(C AND D)[C<--(H AND I)[H+I]+D<--J]')
