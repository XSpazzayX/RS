"""
3. Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera neka traje ~3 sekunde (simulacija upita prema bazi podataka u Cloudu).
    baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
provjerite podudaranje stringova) i provjeru s lozinkom iz baza_lozinka . Ako su lozinke jednake, korutine
vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
{korisnik}: Autorizacija neuspješna." .
    baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
    ]
Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.
"""


import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)

    for db_korisnik in baza_lozinka:
        if db_korisnik['korisnicko_ime'] == korisnik['korisnicko_ime']:
            if db_korisnik['lozinka'] == lozinka:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."

async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    
    for db_korisnik in baza_korisnika:
        if db_korisnik['korisnicko_ime'] == korisnik['korisnicko_ime'] and db_korisnik['email'] == korisnik['email']:
            return await autorizacija(db_korisnik, korisnik['lozinka'])
    
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def main():
    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

    korisnik = {'korisnicko_ime': 'mirko1234', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka12345'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)


if __name__ == "__main__":
    asyncio.run(main())
