# Coin Change Problem   - Find the number of ways to make change for a given amount using given denominations
# Dynamic Programming Approach | Time Complexity: O(n*amount) | Space Complexity: O(amount)
def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount] 

# dynamic programming approach with memoization
def coin_change_ways_memo(coins, amount, memo={}):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    ways = 0
    for coin in coins:
        ways += coin_change_ways_memo(coins, amount - coin, memo)
    memo[amount] = ways
    return ways

# recursive approach (inefficient for large amounts) | Time Complexity: Exponential O(2^amount) | Space Complexity: O(amount)       
def coin_change_ways_recursive(coins, amount, n):
    if amount == 0:
        return 1
    if amount < 0 or n <= 0:
        return 0
    return coin_change_ways_recursive(coins, amount - coins[n - 1], n) + coin_change_ways_recursive(coins, amount, n - 1)  

#recovering the combinations used to make the amount
def coin_change_combinations(coins, amount):
    dp = [[] for _ in range(amount + 1)]
    dp[0] = [[]]  # One way to make amount 0: use no coins

    for coin in coins:
        for i in range(coin, amount + 1):
            for combination in dp[i - coin]:
                dp[i].append(combination + [coin])
    
    return dp[amount]

# Example usage
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    print(f"Number of ways to make change for {amount} is {coin_change_ways(coins, amount)}")  
    print(f"Combinations to make change for {amount} are: {coin_change_combinations(coins, amount)}")     