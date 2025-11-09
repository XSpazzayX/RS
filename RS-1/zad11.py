"""
Napišite funkciju koja prima listu brojeva i vraća rječnik s dvije liste: jedna za parne brojeve, a druga za
neparne brojeve.
Primjer:
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(grupiraj_po_paritetu(lista))
    # {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}
"""


def grupiraj_po_paritetu(lista):
    rezultat = {'parni': [], 'neparni': []}
    for broj in lista:
        if broj % 2 == 0:
            rezultat['parni'].append(broj)
        else:
            rezultat['neparni'].append(broj)
    return rezultat

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(grupiraj_po_paritetu(lista))

if __name__ == "__main__":
    main()