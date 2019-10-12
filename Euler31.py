# Euler 31 how many ways to split 2 pound

amount = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
i = 0
ways = [0] * (amount+1)
ways[0] = 1
while i < len(coins):
    j = coins[i]
    while j <= amount:
        ways[j] += ways[j - coins[i]]
        j += 1
    i += 1
print(ways)
