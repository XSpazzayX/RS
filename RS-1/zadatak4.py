"""
Napišite program koji traži od korisnika unos cijelih brojeva sve dok korisnik ne unese broj 0 . Nakon unosa
0 , program treba ispisati zbroj svih prethodno unesenih brojeva.
"""


def main():
    zbroj = 0

    while True:
        broj = int(input("Unesite cijeli broj (0 za kraj): "))
        if broj == 0:
            break
        zbroj += broj

    print(f"Zbroj unesenih brojeva je {zbroj}")

if __name__ == "__main__":
    main()
