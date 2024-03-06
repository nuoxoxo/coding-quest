choice = '1'
#choice = '0'
PATH = '30.'+choice
s = open(PATH).read()
R = 6 if choice == '1' else 80
C = 10 if choice == '1' else 100
A = [' '] * R * C
print(s, '/len', len(s))

nums = [int(_) for _ in s.split()]
N = len(nums)
curr = 0

def Printer() -> None:
    for r in range(R):
        for c in range(C):
            print(A[c + r*C], end=' ')
        print('\n')

for i in range(0, N-1, 2):
    l, r = nums[i], nums[i + 1]
    curr += l
    for j in range(curr, curr + r):
        A[j] = '#'
    Printer()
    curr += r 

Printer()
print('/end')
