"""
Napišite funkciju koja broji koliko se puta svaka riječ pojavljuje u tekstu (frekvencija riječi) i vraća rječnik s
rezultatima.
Primjer:
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je
    vrlo popularan."
    print(brojanje_riječi(tekst))
    # {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za':
    1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}
"""


def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    frekvencija = {}
    for rijec in rijeci:
        if rijec in frekvencija:
            frekvencija[rijec] += 1
        else:
            frekvencija[rijec] = 1
    return frekvencija

def main():
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print(brojanje_rijeci(tekst))

if __name__ == "__main__":
    main()
