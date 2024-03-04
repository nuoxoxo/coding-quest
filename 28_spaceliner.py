from collections import defaultdict

ADD = ['seat', 'meal', 'meals', 'luggage', 'fee', 'tax']
SUB = ['discount', 'rebate']

lines = open('28.0').read().splitlines()

def Solver (List:str) -> int:
    C = defaultdict(int)
    curr = None
    for line in lines:
        name, R = line.split(':')
        cost, n = R.split()
        name, cost, n = name.lower(), cost.lower(), int(n)
        if cost in ADD:
            C[name] += n
            curr = '+'
        if cost in SUB:
            C[name] -= n
            curr = '-'
        """if name == 'cosmoair':
            print(name, cost, n, '/temp', C[name])
        """
    res = sorted(C.items(), key=lambda _:_[1])
    for i, line in enumerate(res):print(i, line)
    assert res[0][1] in [191274, 2533]
    return res[0][1]

print('/res', [ Solver, ][0](lines))

