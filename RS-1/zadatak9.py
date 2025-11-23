"""
Napišite funkciju koja prima listu i vraća novu listu koja ne sadrži duplikate. Implementaciju odradite
pomoćnim skupom.
Primjer:
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista)) # [1, 2, 3, 4, 5]
"""


def ukloni_duplikate(lista):
    novi = []
    videni = set()
    for x in lista:
        if x not in videni:
            novi.append(x)
            videni.add(x)
    return novi

def main():
    lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(ukloni_duplikate(lista))

if __name__ == "__main__":
    main()
