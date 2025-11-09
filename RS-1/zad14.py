"""

    Napišite funkciju isPrime() koja prima cijeli broj i vraća True ako je broj prost, a False ako nije. Prost broj je prirodan broj veći od 1 koji je dijeljiv jedino s 1 i samim sobom.

Primjer:

print(isPrime(7)) # True
print(isPrime(10)) # False

    Napišite funkciju primes_in_range() koja prima dva argumenta: start i end i vraća listu svih prostih brojeva u tom rasponu.

Primjer:

print(primes_in_range(1, 10)) # [2, 3, 5, 7]
"""


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for n in range(start, end + 1):
        if isPrime(n):
            primes.append(n)
    return primes

def main():
    print(isPrime(7))   # True
    print(isPrime(10))  # False
    print(primes_in_range(1, 10))  # [2, 3, 5, 7]

if __name__ == "__main__":
    main()