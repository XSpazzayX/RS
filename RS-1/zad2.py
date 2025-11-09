"""
Napišite program koji traži unos godine i provjerava je li godina prijestupna. Godina je prijestupna ako:
 - je djeljiva s 4, ali ne sa 100 ili
 - godine je djeljiva sa 400
Ako godina zadovoljava ove uvjete, program treba ispisati poruku:
Godina _____. je prijestupna.
Ako godina nije prijestupna, program treba ispisat poruku:
Godina _____. nije prijestupna.
"""


def main():
    godina = int(input("Unesite godinu: "))
    if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
        print(f"Godina {godina}. je prijestupna.")
    else:
        print(f"Godina {godina}. nije prijestupna.")

if __name__ == "__main__":
    main()
