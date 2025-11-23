"""
Napišite funkciju koja prima listu cijelih brojeva i vraća novu lista koja sadrži samo parne brojeve iz
originalne liste.
Primjer:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista)) # [2, 4, 6, 8, 10]
"""


def filtriraj_parne(lista):
    return [x for x in lista if x % 2 == 0]

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filtriraj_parne(lista))

if __name__ == "__main__":
    main()
