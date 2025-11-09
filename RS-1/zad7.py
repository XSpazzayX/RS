"""
Napišite program koji traži od korisnika da unese lozinku. Lozinka mora zadovoljavati sljedeće uvjete:
1. ako duljina lozinke nije između 8 i 15 znakova, ispišite poruku "Lozinka mora sadržavati između 8 i 15
znakova".
2. ako lozinka ne sadrži barem jedno veliko slovo i jedan broj, ispišite "Lozinka mora sadržavati
barem jedno veliko slovo i jedan broj"
3. ako lozinka sadrži riječ "password" ili "lozinka" (bez obzira na velika i mala slova), ispišite: "Lozinka
ne smije sadržavati riječi 'password' ili 'lozinka'"
4. ako lozinka zadovoljava sve uvjete, ispišite "Lozinka je jaka!"
Metode za normalizaciju stringova: lower() , upper() , islower() , isupper() .
Provjera je li znakovni niz broj: isdigit()
Kod za provjeru dodajte u funkciju provjera_lozinke(lozinka) .
"""


def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return
    if not any(c.isupper() for c in lozinka) or not any(c.isdigit() for c in lozinka):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return

    print("Lozinka je jaka!")

def main():
    lozinka = input("Unesite lozinku: ")
    provjera_lozinke(lozinka)

if __name__ == "__main__":
    main()
