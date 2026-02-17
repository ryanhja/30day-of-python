import math


def sieve_of_atkin(limit):
    if limit < 2:
        return []

    # Initialisation correcte
    sieve = [False] * (limit + 1)
    sieve[2] = True
    sieve[3] = True

    sqrt_limit = int(math.sqrt(limit)) + 1

    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):

            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] ^= True

    # Éliminer les multiples des carrés
    for r in range(5, sqrt_limit):
        if sieve[r]:
            for multiple in range(r * r, limit + 1, r * r):
                sieve[multiple] = False

    # Retourner la liste des nombres premiers
    return [num for num in range(2, limit + 1) if sieve[num]]


def pick_prime(primes, min_size=1000):
    """Retourne un nombre premier >= min_size"""
    for prime in primes:
        if prime >= min_size:
            return prime

    return primes[-1]  # si aucun n’est assez grand


def compute_hash(string, modulus):
    """Polynomial rolling hash (variante DJB2)"""
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)  # hash * 33 XOR c

    return hash_value % modulus


if __name__ == '__main__':

    # Génération des nombres premiers
    primes = sieve_of_atkin(10000)

    # Choisir un modulus premier >= 1000
    modulus = pick_prime(primes, 1000)

    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]

    print(f"Modulus choisi : {modulus}\n")

    for string in test_array:
        hash_value = compute_hash(string, modulus)
        print(f"Hash of {string} is {hash_value}")
