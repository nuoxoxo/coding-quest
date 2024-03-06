def solver(choice: int) -> None:
    PATH = '30.'+str(choice)
    s = open(PATH).read()
    R = 6 if choice else 80
    C = 10 if choice else 100
    def Printer(A) -> None:
        nonlocal R, C
        for r in range(R):
            for c in range(C): print(A[c + r*C], end=' ')
            print()
        print('/end')
    A = [' '] * R * C
    print(s, '/len', len(s))
    nums = [int(_) for _ in s.split()]
    N = len(nums)
    curr = 0
    for idx in range(0, N-1, 2):
        l, r = nums[ idx ], nums[idx + 1]
        curr += l
        for i in range(curr, curr + r):
            A[i] = '@'
        Printer( A )
        curr += r
    Printer( A )

[ solver, ][ 0 ]( 0 )