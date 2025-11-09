"""
1. Napišite program koji ispisuje sumu svih parnih brojeva od 1 do 100 (uključivo).
2. Napišite program koji ispisuje prvih 10 neparnih brojeva u obrnutom redoslijedu.
3. Napišite program koji ispisuje Fibonaccijev niz do 1000. Fibonaccijev niz počinje s brojevima 0 i 1, a
svaki sljedeći broj je zbroj prethodna dva broja.
Svaki zadatak riješite for i while petljom.
"""


def main():
    print("Zadatak 1 - Suma svih parnih brojeva od 1 do 100 (for petlja):")
    suma = 0
    for i in range(2, 101, 2):
        suma += i
    print(suma)

    print("Zadatak 1 - Suma svih parnih brojeva od 1 do 100 (while petlja):")
    suma = 0
    i = 2
    while i <= 100:
        suma += i
        i += 2
    print(suma)

    print("Zadatak 2 - Prvih 10 neparnih brojeva obrnutim redoslijedom (for petlja):")
    for i in range(19, 0, -2):
        print(i, end=" ")
    print()

    print("Zadatak 2 - Prvih 10 neparnih brojeva obrnutim redoslijedom (while petlja):")
    i = 19
    while i > 0:
        print(i, end=" ")
        i -= 2
    print()

    print("Zadatak 3 - Fibonaccijev niz do 1000 (for petlja):")
    a, b = 0, 1
    print(a, b, end=" ")
    for i in range(1000):
        c = a + b
        if c > 1000:
            break
        print(c, end=" ")
        a, b = b, c
    print()

    print("Zadatak 3 - Fibonaccijev niz do 1000 (while petlja):")
    a, b, c = 0, 1, 0
    print(a, b , end=" ")
    while True:
        c = a + b
        if c > 1000:
            break
        print(c, end=" ")
        a, b = b, c
    print()

if __name__ == "__main__":
    main()
