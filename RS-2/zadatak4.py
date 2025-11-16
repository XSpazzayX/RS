"""
1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
Dodajte metodu ispis koja će ispisivati sve atribute automobila.
Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu
ispis .
Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.
2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b .
3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene .
Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
novu listu studenti_objekti :
    studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
    ]
Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste
studenti_objekti . Implementirajte u jednoj liniji koda.
4. Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će
ispisivati "Radim na poziciji {pozicija}".
Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department .
Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
povećava plaću radnika ( Radnik ) za iznos povecanje .
Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode
work i give_raise .
"""

def main():
    import datetime
    class Automobil:
        def __init__(self, marka, model, godina_proizvodnje, kilometraza):
            self.marka = marka
            self.model = model
            self.godina_proizvodnje = godina_proizvodnje
            self.kilometraza = kilometraza
        def ispis(self):
            print(self.marka, self.model, self.godina_proizvodnje, self.kilometraza)
        def starost(self):
            print(datetime.datetime.now().year - self.godina_proizvodnje)

    auto = Automobil("Audi", "A4", 2010, 220000)
    auto.ispis()
    auto.starost()

    class Kalkulator:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def zbroj(self):
            return self.a + self.b
        def oduzimanje(self):
            return self.a - self.b
        def mnozenje(self):
            return self.a * self.b
        def dijeljenje(self):
            return self.a / self.b
        def potenciranje(self):
            return self.a ** self.b
        def korijen(self):
            import math
            return math.sqrt(self.a)
    
    kalkulator = Kalkulator(9, 3)
    print(kalkulator.zbroj())
    print(kalkulator.oduzimanje())
    print(kalkulator.mnozenje())
    print(kalkulator.dijeljenje())
    print(kalkulator.potenciranje())
    print(kalkulator.korijen())

    class Student:
        def __init__(self, ime, prezime, godine, ocjene):
            self.ime = ime
            self.prezime = prezime
            self.godine = godine
            self.ocjene = ocjene
        def prosjek(self):
            return sum(self.ocjene) / len(self.ocjene)

    studenti = [
        {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
        {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
        {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
        {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
        {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
        {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
    ]
    studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]
    najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
    print(najbolji_student.ime, najbolji_student.prezime)

    import math
    class Krug:
        def __init__(self, r):
            self.r = r
        def opseg(self):
            return 2 * math.pi * self.r
        def povrsina(self):
            return math.pi * self.r**2

    k = Krug(5)
    print(k.opseg(), k.povrsina())

    class Radnik:
        def __init__(self, ime, pozicija, placa):
            self.ime = ime
            self.pozicija = pozicija
            self.placa = placa
        def work(self):
            print(f"Radim na poziciji {self.pozicija}")
    class Manager(Radnik):
        def __init__(self, ime, pozicija, placa, department):
            super().__init__(ime, pozicija, placa)
            self.department = department
        def work(self):
            print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
        def give_raise(self, radnik, povecanje):
            radnik.placa += povecanje

    r = Radnik("Luka", "Tehničar", 900)
    m = Manager("Marko", "Voditelj", 2000, "IT")
    r.work()
    m.work()
    print(r.placa)
    m.give_raise(r, 300)
    print(r.placa)

if __name__ == "__main__":
    main()
