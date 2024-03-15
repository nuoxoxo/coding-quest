coins, amount = [1, 2, 3], 5
amount, coins = 856, [40,12,2,1]

def Solution_coin_change(amount, coins):
    C = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(C)]
    for i in range(C):
        for m in range(amount + 1):
            if m == 0:
                dp[i][0] = 1
                continue
            dp[i][m] = dp[i - 1][m]
            coin = m - coins[i - 1]
            if coin > -1:
                dp[i][m] += dp[i][coin]
    for i in range(C):
        for m in range(1, amount + 1):
            dp[i][m] += dp[i - 1][m]
    #print('/coin change - res', dp[-1][-1])
    return dp[-1][-1]

def Solution_correct(amount, coins):
    C = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    for a in range(1, amount + 1):
        for c in range(C):
            if a - coins[c] >= 0:
                dp[a] += dp[a - coins[c]]
    return dp[amount]

res_coin = Solution_coin_change(amount, coins)
res_correct = Solution_correct(amount, coins)

print('/wrong', res_coin)
print('/right', res_correct)
assert res_correct % (10 ** 12) == 769252066051

