def coinChange(coins, amount: int) -> int:

    # dp = [0] + ([float('inf')] * amount)
    dp = [0] + [float("inf")] * (amount)

    for index in range(1, amount + 1):
        for coin in coins:
            if coin <= index:
                dp[index] = min(dp[index], dp[index - coin] + 1)

    # print(dp)
    return dp[-1] if dp[-1] != float("inf") else -1


print(coinChange([1, 2, 5], 11))
