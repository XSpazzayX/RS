"""
# Raspodijeljeni sustavi: Zadatak za vježbu - 31. 10. 2025.

## Zadatak: Nino Telefonino

### Tekst zadatka

Ima jedan Nino kemu rabi novi telefonino. E ben, zato: Definiraj Python funkciju `validiraj_broj_telefona(broj: str)` koja očekuje broj telefona kao ulazni parametar te vraća rječnik sa sljedećim ključevima:

```python
{
"pozivni_broj": pogledati tablicu (str),
"broj_ostatak": ostatak broja (str),
"vrsta": "fiksna mreža" ili "mobilna mreža" ili "posebne usluge" (str),
"mjesto" : pogledati tablicu (str),
"operater": pogledati tablicu (str),
"validan": True ili False (bool)
}
```

**Validacijska pravila:**

- Funkcija mora ispraviti `broj` tako da ukloni sve nepotrebne znakove (razmake, crtice, zagrade, random whitespace itd.) i provjeriti je li broj ispravan prema pravilima u nastavku.
- Pozivni broj mora biti jedan od onih navedenih u tablici ispod.
- Nakon pozivnog broja, `broj_ostatak` mora imati točno 6 ili 7 znamenki za fiksne mreže, 6 ili 7 znamenki za mobilne mreže te točno 6 znamenki za posebne usluge. `broj_ostatak` predstavlja pretplatnički dio broja (bez pozivnog broja).
- `broj` može počinjati s opcionalnim znakom `+`, `385` ili `00385`, ili pak varijante sa zagradama `(385)917217633` za međunarodne pozive; validacija to mora uzeti u obzir.
- Funkcija mora preslikati/mapirati `broj` na odgovarajuću `vrstu`, `mjesto` ili `operater` na temelju pozivnog broja.
- Ako je broj mobilan, `mjesto` postavite na `None`. Ako je broj posebne usluge, postavite `mjesto` i `operater` na `None`. Ako je broj fiksan, `operater` postavite na `None`.

Ako je broj valjan, postavite ključ `validan` na True i ispunite ostale ključeve prema tablici. Ako broj nije valjan, postavite `validan` na False te postavite samo one ključeve koje je moguće odrediti (npr. `pozivni_broj` i `broj_ostatak`).

**Još napomena:**

- Poželjno je definirati pomoćne funkcije za čišćenje i validaciju broja.

- Korisne metode: `str.replace()`, `str.startsWith()`, `str.isdigit()`, `len()`, `str.join()` (Google it).

- Zadatak probajte riješiti bez regularnih izraza (RegEx).

### Tablica pozivnih brojeva RH:

| Pozivni broj | Mjesto / Operater                                             | Vrsta          |
| ------------ | ------------------------------------------------------------- | -------------- |
| 01           | Grad Zagreb i Zagrebačka županija                             | Fiksna mreža   |
| 020          | Dubrovačko-neretvanska županija                               | Fiksna mreža   |
| 021          | Splitsko-dalmatinska županija                                 | Fiksna mreža   |
| 022          | Šibensko-kninska županija                                     | Fiksna mreža   |
| 023          | Zadarska županija                                             | Fiksna mreža   |
| 031          | Osječko-baranjska županija                                    | Fiksna mreža   |
| 032          | Vukovarsko-srijemska županija                                 | Fiksna mreža   |
| 033          | Virovitičko-podravska županija                                | Fiksna mreža   |
| 034          | Požeško-slavonska županija                                    | Fiksna mreža   |
| 035          | Brodsko-posavska županija                                     | Fiksna mreža   |
| 040          | Međimurska županija                                           | Fiksna mreža   |
| 042          | Varaždinska županija                                          | Fiksna mreža   |
| 043          | Bjelovarsko-bilogorska županija                               | Fiksna mreža   |
| 044          | Sisačko-moslavačka županija                                   | Fiksna mreža   |
| 047          | Karlovačka županija                                           | Fiksna mreža   |
| 048          | Koprivničko-križevačka županija                               | Fiksna mreža   |
| 049          | Krapinsko-zagorska županija                                   | Fiksna mreža   |
| 051          | Primorsko-goranska županija                                   | Fiksna mreža   |
| 052          | Istarska županija                                             | Fiksna mreža   |
| 053          | Ličko-senjska županija                                        | Fiksna mreža   |
| 091          | A1 Hrvatska                                                   | Mobilna mreža  |
| 092          | Tomato                                                        | Mobilna mreža  |
| 095          | Telemach                                                      | Mobilna mreža  |
| 097          | bonbon                                                        | Mobilna mreža  |
| 098, 099     | Hrvatski Telekom                                              | Mobilna mreža  |
| 0800         | Besplatni pozivi                                              | Posebne usluge |
| 060          | Komercijalni pozivi                                           | Posebne usluge |
| 061          | Glasovanje telefonom                                          | Posebne usluge |
| 064          | Usluge s neprimjerenim sadržajem                              | Posebne usluge |
| 065          | Nagradne igre                                                 | Posebne usluge |
| 069          | Usluge namijenjene djeci                                      | Posebne usluge |
| 072          | jedinstveni pristupni broj za cijelu državu za posebne usluge | Posebne usluge |
"""


POZIVNI_BROJEVI = {
        "01": {"vrsta": "fiksna mreža", "mjesto": "Grad Zagreb i Zagrebačka županija", "operater": None},
        "020": {"vrsta": "fiksna mreža", "mjesto": "Dubrovačko-neretvanska županija", "operater": None},
        "021": {"vrsta": "fiksna mreža", "mjesto": "Splitsko-dalmatinska županija", "operater": None},
        "022": {"vrsta": "fiksna mreža", "mjesto": "Šibensko-kninska županija", "operater": None},
        "023": {"vrsta": "fiksna mreža", "mjesto": "Zadarska županija", "operater": None},
        "031": {"vrsta": "fiksna mreža", "mjesto": "Osječko-baranjska županija", "operater": None},
        "032": {"vrsta": "fiksna mreža", "mjesto": "Vukovarsko-srijemska županija", "operater": None},
        "033": {"vrsta": "fiksna mreža", "mjesto": "Virovitičko-podravska županija", "operater": None},
        "034": {"vrsta": "fiksna mreža", "mjesto": "Požeško-slavonska županija", "operater": None},
        "035": {"vrsta": "fiksna mreža", "mjesto": "Brodsko-posavska županija", "operater": None},
        "040": {"vrsta": "fiksna mreža", "mjesto": "Međimurska županija", "operater": None},
        "042": {"vrsta": "fiksna mreža", "mjesto": "Varaždinska županija", "operater": None},
        "043": {"vrsta": "fiksna mreža", "mjesto": "Bjelovarsko-bilogorska županija", "operater": None},
        "044": {"vrsta": "fiksna mreža", "mjesto": "Sisačko-moslavačka županija", "operater": None},
        "047": {"vrsta": "fiksna mreža", "mjesto": "Karlovačka županija", "operater": None},
        "048": {"vrsta": "fiksna mreža", "mjesto": "Koprivničko-križevačka županija", "operater": None},
        "049": {"vrsta": "fiksna mreža", "mjesto": "Krapinsko-zagorska županija", "operater": None},
        "051": {"vrsta": "fiksna mreža", "mjesto": "Primorsko-goranska županija", "operater": None},
        "052": {"vrsta": "fiksna mreža", "mjesto": "Istarska županija", "operater": None},
        "053": {"vrsta": "fiksna mreža", "mjesto": "Ličko-senjska županija", "operater": None},
        "091": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "A1 Hrvatska"},
        "092": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "Tomato"},
        "095": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "Telemach"},
        "097": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "bonbon"},
        "098": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "Hrvatski Telekom"},
        "099": {"vrsta": "mobilna mreža", "mjesto": None, "operater": "Hrvatski Telekom"},
        "0800": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "060": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "061": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "064": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "065": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "069": {"vrsta": "posebne usluge", "mjesto": None, "operater": None},
        "072": {"vrsta": "posebne usluge", "mjesto": None, "operater": None}
}

def ocisti_broj(broj):
    if broj.startswith('+385'):
        broj = "0" + broj[4:]
    elif broj.startswith('00385'):
        broj = "0" + broj[5:]
    elif broj.startswith('385'):
        broj = "0" + broj[3:]
    elif broj.startswith('(385)'):
        broj = "0" + broj[5:]
    
    broj = ''.join(filter(str.isdigit, broj))

    return broj

def izvuci_pozivni_broj(broj):
    pozivni_broj = None

    for pb in POZIVNI_BROJEVI:
        if broj.startswith(pb):
            pozivni_broj = pb
            break

    return pozivni_broj


def validiraj_broj_telefona(broj: str):
    rezultat = {"pozivni_broj": None, "broj_ostatak": None, "vrsta": None, "mjesto": None, "operater": None, "validan": False}

    broj = ocisti_broj(broj)

    pozivni_broj = izvuci_pozivni_broj(broj)

    if pozivni_broj is None:
        rezultat["broj_ostatak"] = broj
        return rezultat
    
    broj_ostatak = broj[len(pozivni_broj):]

    info = POZIVNI_BROJEVI[pozivni_broj]
    rezultat["vrsta"] = info["vrsta"]
    rezultat["operater"] = info["operater"]
    rezultat["mjesto"] = info["mjesto"]
    rezultat["pozivni_broj"] = pozivni_broj
    rezultat["broj_ostatak"] = broj_ostatak

    if rezultat["vrsta"] in ["fiksna mreža", "mobilna mreža"]:
        if len(broj_ostatak) not in [6, 7]:
            return rezultat
    elif rezultat["vrsta"] == "posebne usluge":
        if len(broj_ostatak) != 6:
            return rezultat

    rezultat["validan"] = True

    return rezultat

def main():
    test_brojevi = [
        "+385912345678",       # važeći mobilni broj (međunarodni format)
        "00385987654321",      # važeći mobilni broj (međunarodni format sa 00)
        "0912345678",          # važeći mobilni broj (domaći format)
        "021123456",           # važeći fiksni broj (domaći format)
        "+3852123456",         # nevažeći fiksni broj, samo 5 znamenaka u ostatku
        "0800123456",          # važeći besplatni broj
        "12345",               # nevažeći, prekratak broj
        "+3850991234567",      # nevažeći, vodeća 0 nakon pozivnog broja
        "003850991234567",     # nevažeći, vodeća 0 nakon pozivnog broja
        "999123456",           # nevažeći, nepostojeći hrvatski prefiks
        "031613247",           # važeći fiksni broj
        "049999999",           # važeci fiksni broj
        "(385)2123456",        # nevažeći fiksni broj, samo 5 znamenaka u ostatku
        "(385)21123456",       # važeći fiksni broj
        "+385 98 765 4321",    # važeći mobilni broj
        "+385123",             # nevažeći, prekratak broj
        "091234567890",        # nevažeći, predug broj
        "+385 1 123 4567",     # važeći
        "+385-1-123-4567"      # važeći
    ]

    for b in test_brojevi:
        print(validiraj_broj_telefona(b))

if __name__ == "__main__":
    main()
