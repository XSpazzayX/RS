"""
1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:
    parni_kvadrati = ...
    print(parni_kvadrati) # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764,
    1936, 2116, 2304, 2500]
2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
sadrže slovo a :
    rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
    "pjesma", "otorinolaringolog"]
    duljine_sa_slovom_a = ...
    print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]
3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti su
kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:
    kubovi = ...
    print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9:
    729}, {10: 10}]
4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s
korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:
    korijeni = ...
    print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32,
    350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}
5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti
su zbrojeni bodovi, iz liste studenti :
    studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
    ]
    zbrojeni_bodovi = ...
    print(zbrojeni_bodovi) # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362},
    {'Ivić': 236}, {'Matić': 266}]
6. Koristeći dictionary comprehension, izgradite rječnik gdje su ključevi brojevi od 1 do 10, a vrijednosti su
liste faktorijela tih brojeva.
    import math
    faktorijeli = ...
    print(faktorijeli) # {1: [1], 2: [1, 2], 3: [1, 2, 6], 4: [1, 2, 6, 24], 5: [1, 2, 6, 24,
    120], 6: [1, 2, 6, 24, 120, 720], 7: [1, 2, 6, 24, 120, 720, 5040], 8: [1, 2, 6, 24, 120,
    720, 5040, 40320], 9: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880], 10: [1, 2, 6, 24, 120,
    720, 5040, 40320, 362880, 3628800]}
"""


def main():
    parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
    print(parni_kvadrati)

    rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
              "pjesma", "otorinolaringolog"]
    duljine_sa_slovom_a = [len(r) for r in rijeci if "a" in r]
    print(duljine_sa_slovom_a)

    kubovi = [{x: (x**3 if x % 2 == 1 else x)} for x in range(1, 11)]
    print(kubovi)

    import math
    korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
    print(korijeni)

    studenti = [
        {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
        {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
        {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
        {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
        {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
        {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
    ]
    zbrojeni_bodovi = [{s["prezime"]: sum(s["bodovi"])} for s in studenti]
    print(zbrojeni_bodovi)

    import math
    faktorijeli = {x: [math.factorial(i) for i in range(1, x+1)] for x in range(1, 11)}
    print(faktorijeli)

if __name__ == "__main__":
    main()
