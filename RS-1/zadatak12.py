"""
Napišite funkciju koja prima rječnik i vraća novi rječnik u kojem su ključevi i vrijednosti zamijenjeni.
Primjer:
    rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
    print(obrni_rjecnik(rjecnik))
    # {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}
"""


def obrni_rjecnik(rjecnik):
    novi = {vrijednost: ključ for ključ, vrijednost in rjecnik.items()}
    return novi

def main():
    rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
    print(obrni_rjecnik(rjecnik))

if __name__ == "__main__":
    main()
