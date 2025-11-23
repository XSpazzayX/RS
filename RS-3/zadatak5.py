"""
5. Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od
3 sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva
prezime , broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu
zadaci kao u prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina
secure_data mora za svaki rječnik vratiti novi rječnik u obliku: {'prezime': 'prezime',
'broj_kartice': 'enkriptirano', 'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju
hash(str) koja samo vraća hash vrijednost ulaznog stringa ili nešto slično.
"""


import asyncio

async def secure_data(podatak):
    await asyncio.sleep(3)
    return {
        'prezime': podatak['prezime'],
        'broj_kartice': hash(podatak['broj_kartice']),
        'CVV': hash(podatak['CVV'])
    }

async def main():
    podaci = [
        {'prezime': 'Ivic', 'broj_kartice': '1234567890123456', 'CVV': '123'},
        {'prezime': 'Horvat', 'broj_kartice': '9876543210987654', 'CVV': '456'},
        {'prezime': 'Kovacic', 'broj_kartice': '1111222233334444', 'CVV': '789'}
    ]

    zadaci = [asyncio.create_task(secure_data(p)) for p in podaci]

    rezultati = await asyncio.gather(*zadaci)

    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
