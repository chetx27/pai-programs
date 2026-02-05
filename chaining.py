facts = ['A']
rules = [['A', 'B'], ['B', 'C'], ['C', 'G']]

def forward():
    f = facts[:]
    for _ in range(len(rules)):
        for cond, res in rules:
            if cond in f and res not in f:
                f.append(res)
    
    if 'G' in f:
        print("Using forward chaining: Goal Reached!")
    else:
        print("Using forward chaining: Goal Not Reached!")

def backward(goal):
    if goal in facts:
        return True
    for cond, res in rules:
        if res == goal:
            if backward(cond):
                return True
    return False

forward()
if backward('G'):
    print("Using Backward Chaining: Goal Reachable!")
else:
    print("Using Backward Chaining: Goal Not Reachable!")