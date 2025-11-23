"""
1. Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
korištenja asyncio.gather() i asyncio.create_task() funkcija.
"""


import asyncio

async def dohvat_podataka():
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    podaci = [i for i in range(1, 11)]
    return podaci

async def main():
    rezultat = await dohvat_podataka()
    print(rezultat)

if __name__ == "__main__":
    asyncio.run(main())
