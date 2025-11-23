"""
2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka
vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a
druga korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima)
nakon 5 sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate.
Program se mora izvršavati ~5 sekundi.
"""


import asyncio

async def dohvati_korisnike():
    await asyncio.sleep(3)
    return [{"id": i, "ime": f"Korisnik{i}"} for i in range(1, 4)]

async def dohvati_proizvode():
    await asyncio.sleep(5)
    return [{"id": i, "naziv": f"Proizvod{i}"} for i in range(1, 4)]

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print(korisnici)
    print(proizvodi)

if __name__ == "__main__":
    asyncio.run(main())
