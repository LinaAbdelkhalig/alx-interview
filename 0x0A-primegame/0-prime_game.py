#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values, where each round uses a different n.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
        None: If there is no clear winner.
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(limit):
        """Generates a list of primes up to a given limit using the Sieve of Eratosthenes."""
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        return primes

    # Find the maximum value of n for all rounds
    max_num = max(nums)

    # Precompute primes up to the largest number in nums
    primes = sieve_of_eratosthenes(max_num)

    # Count of prime numbers up to each index
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of prime numbers in the range 1 to n
        total_primes = prime_count[n]

        # If the total primes are odd, Maria wins; if even, Ben wins
        if total_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

