#!/usr/bin/python3
"""
Solution for the coin change problem
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.

    Parameters:
    coins (list): A list of coin denominations.
    total (int): The target amount to make.

    Returns:
    int: The minimum number of coins needed to make the total amount,
         or -1 if it cannot be made.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins required for each amount
    # Use a large number (infinity) to represent an amount that cannot be reached
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make total 0

    # Fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total is still marked as infinity, it means it's not possible to make the amount
    return dp[total] if dp[total] != float('inf') else -1

