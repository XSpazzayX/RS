from .proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        tekst = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {tekst}, Ukupna cijena: {self.ukupna_cijena} eur")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("Narudžba mora biti lista!")
        return

    if not naruceni_proizvodi:
        print("Narudžba je prazna!")
        return

    for p in naruceni_proizvodi:
        if not isinstance(p, dict):
            print("Svi elementi moraju biti rječnici!")
            return

        if not all(k in p for k in ("naziv", "cijena", "narucena_kolicina")):
            print("Rječnik mora sadržavati naziv, cijena i narucena_kolicina!")
            return

        dostupni = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not dostupni or dostupni.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi)

    narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append({"narudzba": narudzba})
    return narudzba
