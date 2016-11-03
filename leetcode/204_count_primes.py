"""
Count the number of prime numbers less than a non-negative number, n.
==============================
This is definitely not easy unless you already know Sieve of Eratosthenes.
"""


def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    isPrime = [True] * n
    isPrime[0:2] = [False] * 2
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * 2:n:i] = [False] * ((n - 1 - i * 2) / i + 1)
    return sum(isPrime)
