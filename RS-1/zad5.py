"""
Vježba 5: Analiziraj sljedeće for petlje
Pojasnite zašto sljedeća petlja nema (previše) smisla:
    for i in range(1, 2):
        print(i)

Što ce ispisati sljedeća petlja?
    for i in range(10, 1, 2):
        print(i)

Što će ispisati sljedeća petlja?
    for i in range(10, 1, -1):
        print(i)

"""


def main():
    print("Petlja 1:")
    for i in range(1, 2): # Ova petlja nema previše smisla jer će se izvršiti samo jedanput jer je završna (stop) vrijednost rangea isključiva
        print(i)

    print("Petlja 2:")
    for i in range(10, 1, 2): # Ova petlja neće ispisati ništa zato jer je početna vrijednost veća od završne, a korak je pozitivan
        print(i)

    print("Petlja 3:")
    for i in range(10, 1, -1): # Ova petlja će ispisati silazno brojeve od 10 do 2
        print(i)

if __name__ == "__main__":
    main()
