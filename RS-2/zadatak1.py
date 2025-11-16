"""
Napišite korespondirajuće lambda izraze za sljedeće funkcije:
1. Kvadriranje broja:
    def kvadriraj(x):
    return x ** 2
2. Zbroji pa kvadriraj:
    def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2
3. Kvadriraj duljinu niza:
    def kvadriraj_duljinu(niz):
    return len(niz) ** 2
4. Pomnoži vrijednost s 5 pa potenciraj na x:
    def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x
5. Vrati True ako je broj paran, inače vrati None:
    def paran_broj(x):
    if x % 2 == 0:
    return True
    else:
    return None
"""


def main():
    kvadriraj = lambda x: x**2
    zbroji_pa_kvadriraj = lambda a, b: (a + b)**2
    kvadriraj_duljinu = lambda niz: len(niz)**2
    pomnozi_i_potenciraj = lambda x, y: (y * 5)**x
    paran_broj = lambda x: True if x % 2 == 0 else None

    print(kvadriraj(4))
    print(zbroji_pa_kvadriraj(3, 5))
    print(kvadriraj_duljinu([1, 2, 3, 4]))
    print(pomnozi_i_potenciraj(3, 2))
    print(paran_broj(10))
    print(paran_broj(11))

if __name__ == "__main__":
    main()