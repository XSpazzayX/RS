class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(self.naziv, self.cijena, self.dostupna_kolicina)

skladiste = [
    Proizvod("Televizor", 3000, 5),
    Proizvod("Mobitel", 1500, 15)
]

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    novi = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi)
