"""
Napišite funkciju count_vowels_consonants() koja prima string i vraća rječnik s brojem samoglasnika i brojem suglasnika u tekstu.

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

Primjer:

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(count_vowels_consonants(tekst))

# {'vowels': 30, 'consonants': 48}
"""


def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = {'vowels': 0, 'consonants': 0}

    for char in tekst:
        if char in vowels:
            count['vowels'] += 1
        elif char in consonants:
            count['consonants'] += 1

    return count

def main():
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print(count_vowels_consonants(tekst))  # {'vowels': 30, 'consonants': 48}

if __name__ == "__main__":
    main()