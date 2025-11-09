"""
    Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(prvi_i_zadnji(lista)) # (1, 10)

    Funkcija koja vraća n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min().

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

print(maks_i_min(lista)) # (250, 5)

    Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(presjek(skup_1, skup_2)) # {4, 5}
"""


def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]
    for x in lista:
        if x > maks:
            maks = x
        if x < min:
            min = x
    return (maks, min)

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

def main():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(prvi_i_zadnji(lista1))  # (1, 10)

    lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
    print(maks_i_min(lista2))  # (250, 5)

    skup_1 = {1, 2, 3, 4, 5}
    skup_2 = {4, 5, 6, 7, 8}
    print(presjek(skup_1, skup_2))  # {4, 5}

if __name__ == "__main__":
    main()