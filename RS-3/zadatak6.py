"""
6. Kako možete unutar main korutine natjerati event loop da obuhvati ispis unutar korutine
fetch_data(2) bez da ju awaitate unutar main funkcije? Preciznije, dokažite kako se može ispisati
tekst Dovršio sam s 2. unutar korutine fetch_data(2) bez da eksplicitno pozivate await task2
unutar main() funkcije.
    import asyncio, time
    async def fetch_data(param):
        print(f"Nešto radim s {param}...")
        await asyncio.sleep(param)
        print(f'Dovršio sam s {param}.')
        return f"Rezultat za {param}"
    async def main():
        task1 = asyncio.create_task(fetch_data(1)) # schedule
        task2 = asyncio.create_task(fetch_data(2)) #schedule
        result1 = await task1
        print("Fetch 1 uspješno završen.")
        return [result1]

        t1 = time.perf_counter()
        results = asyncio.run(main()) # pokretanje event loop-a
        t2 = time.perf_counter()
        print(results)
        print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
"""


import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat za {param}"

async def main_1():
    # Jedan nacin je da  dodamo sleep od x sekundi između taska 2 i taska 1
    # Na taj način dajemo vremena drugom tasku da se izvrši
    task2 = asyncio.create_task(fetch_data(2))
    
    await asyncio.sleep(2)

    task1 = asyncio.create_task(fetch_data(1))
    result1 = await task1

    print("Fetch 1 uspješno završen.")

    return [result1]

async def main_2():
    # Drugi nacin je da cekamo sve taskove iskljucivsi trenutacni task
    # ili naravno ako je dopušteno u zadataku  možemo gatherat task1 i task2 eksplicitno sa asyncio.gather
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    result1 = await task1
    print("Fetch 1 uspješno završen.")

    await asyncio.gather(*(
        asyncio.all_tasks()
        - {asyncio.current_task()}
    ))

    return [result1]


async def main_3():
    # Ručno loopamo i provjeravamo jel task završen
    # Vračamo kontrolu event loopu da može radit 
    # napredak na tasku sa asyncio.sleep(0)
    task1 = asyncio.create_task(fetch_data(1)) # schedule
    task2 = asyncio.create_task(fetch_data(2)) # schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    
    while not task2.done():
        await asyncio.sleep(0)
    
    print("Fetch 2 uspješno završen.", task2.result())
    
    return [result1]

if __name__ == "__main__":
    t1 = time.perf_counter()
    results = asyncio.run(main_1())
    t2 = time.perf_counter()
    print(results)
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

    t1 = time.perf_counter()
    results = asyncio.run(main_2())
    t2 = time.perf_counter()
    print(results)
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

    t1 = time.perf_counter()
    results = asyncio.run(main_3())
    t2 = time.perf_counter()
    print(results)
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")