facts = {'A'}

rules = {
    'R1': {'if': {'A'}, 'then': 'B'},
    'R2': {'if': {'B'}, 'then': 'C'},
    'R3': {'if': {'C'}, 'then': 'G'}
}

def forward_chaining():
    changed = True
    while changed:
        changed = False
        for rule in rules.values():
            if rule['if'].issubset(facts) and rule['then'] not in facts:
                facts.add(rule['then'])
                changed = True
    print("Using forward chaining: Goal Reached!" if 'G' in facts else "Using forward chaining: Goal Not Reached!")

def backward_chaining(goal):
    if goal in facts:
        return True
    for rule in rules.values():
        if rule['then'] == goal:
            if all(backward_chaining(f) for f in rule['if']):
                return True
    return False

forward_chaining()
facts = {'A'}
print("Using Backward Chaining: Goal Reachable!" if backward_chaining('G') else "Using Backward Chaining: Goal Not Reachable!")
