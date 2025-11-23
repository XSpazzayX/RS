"""
4. Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere
parnosti broja putem vanjskog API-ja. Korutina prima kao argument broj za koji treba provjeriti
parnost, a vraća poruku "Broj {broj} je paran." ili "Broj {broj} je neparan." nakon 2
sekunde. Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100
(možete koristiti random modul). Listu brojeva izgradite kroz list comprehension sintaksu. Nakon
toga, pohranite u listu zadaci 10 Task objekata koji će izvršavati korutinu provjeri_parnost za
svaki broj iz liste (također kroz list comprehension). Na kraju, koristeći asyncio.gather() , pokrenite
sve korutine konkurentno i ispišite rezultate.
"""


import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)

    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]

    zadaci = [asyncio.create_task(provjeri_parnost(b)) for b in brojevi]

    rezultati = await asyncio.gather(*zadaci)

    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
