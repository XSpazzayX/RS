"""
Implementirajte igru pogađanja broja u rasponu od 1 do 100. Korisnik unosi svoj pokušaj, a program nakon
svakog unosa ispisuje poruku koja označava je li uneseni broj veći, manji ili jednak traženom broju. Igra traje
dok korisnik ne pogodi točan broj.
Za izlazak iz igre koristite pomoćnu bool varijablu broj_je_pogoden.
Na kraju ispišite korisniku poruku: "Bravo, pogodio si u __ pokušaja".
"""


import random

def main():
    trazeni_broj = random.randint(1, 100)
    broj_je_pogoden = False
    pokusaji = 0

    while not broj_je_pogoden:
        pokusaj = int(input("Pogodi broj (1-100): "))
        pokusaji += 1

        if pokusaj < trazeni_broj:
            print("Traženi broj je veći.")
        elif pokusaj > trazeni_broj:
            print("Traženi broj je manji.")
        else:
            broj_je_pogoden = True
            print(f"Bravo, pogodio si u {pokusaji} pokušaja.")

if __name__ == "__main__":
    main()
