"""
Definirajte paket shop koji će sadržavati module proizvodi.py i narudzbe.py .
Modul proizvodi.py :
definirajte klasu Proizvod s atributima naziv , cijena i dostupna_kolicina . Dodajte metodu
ispis koja će ispisivati sve atribute proizvoda.
u listu skladiste pohranite 2 objekta klase Proizvod s proizvoljnim vrijednostima atributa. U ovoj
listi ćete pohranjivati instance klase Proizvod koje će predstavljati stanje proizvoda u skladištu.
definirajte funkciju dodaj_proizvod van definicije klase koja će dodavati novi Proizvod u listu
skladiste .
U main.py datoteci učitajte modul proizvodi.py iz paketa shop i pozovite pozovite funkciju
dodaj_proizvod za svaki element iz sljedeće liste:
    proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
    ]
Modul narudzbe.py :
definirajte klasu Narudzba s atributima: naruceni_proizvodi i ukupna_cijena .
dodajte funkciju napravi_narudzbu van definicije klase koja prima listu proizvoda kao argument i
vraća novu instancu klase Narudzba .
dodajte provjeru u funkciju napravi_narudzbu koja će provjeravati dostupnost proizvoda prije nego
što se napravi narudžba. Ako proizvoda nema na stanju, ispišite poruku: "Proizvod {naziv} nije
dostupan!" i ne stvarajte narudžbu.
dodajte provjere u funkciju napravi_narudzbu koja će provjeriti sljedeća 4 uvjeta:
argument naruceni_proizvodi mora biti lista
svaki element u listi mora biti rječnik
svaki rječnik mora sadržavati ključeve naziv , cijena i narucena_kolicina
lista ne smije biti prazna
izračunajte ukupnu cijenu narudžbe koju ćete pohraniti u lokalnu varijablu ukupna_cijena u jednoj
liniji koda.
narudžbe (instanca klase Narudzba ) pohranite u listu rječnika narudzbe .
u klasu Narudzba dodajte metodu ispis_narudzbe koja će ispisivati nazive svih naručenih
proizvoda, količine te ukupnu cijenu narudžbe.
npr. "Naručeni proizvodi: Laptop x 2, Monitor x 1, Ukupna cijena: 11000 eur".

U main.py datoteci učitajte modul narudzbe.py iz paketa shop i pozovite funkciju napravi_narudzbu s
listom proizvoda iz prethodnog zadatka.
"""

from shop.proizvodi import dodaj_proizvod
from shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

narudzba_lista = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzba = napravi_narudzbu(narudzba_lista)

if narudzba:
    narudzba.ispis_narudzbe()
