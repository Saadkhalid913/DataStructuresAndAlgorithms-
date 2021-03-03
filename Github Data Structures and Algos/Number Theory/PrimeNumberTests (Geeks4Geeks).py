from math import ceil, sqrt, gcd
import random

# linear O(sqrt(n))


def is_prime1(n):

    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    if not n % 2:
        return False

    for i in range(3, ceil(sqrt(n))):
        if not (n / i) % 1:
            return False

    return True


def is_prime2(n):

    for i in range(100):
        num = random.randint(2, n-2)
        if gcd(num, n) != 1:
            return False
        if (num ** n-1) % n == 1:
            return False

    return True
