"""
Napišite program koji traži od korisnika unos dva broja ( float ) te jedan od operatora ( + , - , * , / ).
Program treba ispisati rezultat operacije nad unesenim brojevima u formatu:
Rezultat operacije 5.0 + 3.0 je 8.0
Ako korisnik pokuša dijeljenje s nulom, program treba ispisati poruku:
Dijeljenje s nulom nije dozvoljeno!
Ako korisnik unese nepodržani operator, program treba ispisati poruku:
Nepodržani operator!
"""


def main():
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    op = input("Unesite operator (+, -, *, /): ")

    if op == '+':
        print(f"Rezultat operacije {a} + {b} je {a + b}")
    elif op == '-':
        print(f"Rezultat operacije {a} - {b} je {a - b}")
    elif op == '*':
        print(f"Rezultat operacije {a} * {b} je {a * b}")
    elif op == '/':
        if b == 0:
            print("Dijeljenje s nulom nije dozvoljeno!")
        else:
            print(f"Rezultat operacije {a} / {b} je {a / b}")
    else:
        print("Nepodržani operator!")

if __name__ == "__main__":
    main()
