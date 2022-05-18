"""
Solution to Problem H (Subprime) from 2022 ANZAC 1.

The naive method of trial division up to and including the square root of a
number is not efficient enough.
"""



from math import sqrt
from itertools import islice


inp = input().split() # Read the values of L and H.
p = input()           # Read the substring to be found in primes.

start = int(inp[0]) # L - the starting index in a list of first 100000 primes.
stop = int(inp[1])  # H - the finishing index in a list of first 100000 primes.
counter = 0         # The number of primes for which p is a substring.

def eratosthenes(n):
    """
    Generates a Boolean list from 0 to n inclusive, where the value at index i
    will eventually be false if i is not prime.
    """
    prime = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    
    prime[0]= False
    prime[1]= False
    
    return prime


def prime_gen():
    """
    Generates a list of only primes up to and including 1.31 million and then
    slices the list to only hold the primes that are needed.
    """
    # Generate primes up to and including 1.31 million.
    primes = eratosthenes(1310000)

    # Extract all the primes in this list.
    primeList = []
    for n, item in enumerate(primes):
        if item == True:
            primeList.append(n)

    # Only take the primes that are needed.
    primeList = primeList[start - 1:stop]
    return primeList

# Generate primes.
primes = prime_gen()

# Find the number of primes for which p is a substring.
for item in primes:
    if (str(p) in str(item)):
        counter += 1

print(counter)