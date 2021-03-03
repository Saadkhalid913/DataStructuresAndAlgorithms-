def primes(n):
    prime = []
    i = 2
    while i < n:
        if n % i > 0:
            i += 1

        elif n % i == 0:
            n //= i
            prime += [i]
    if n == i:
        prime += [i]

    return prime
