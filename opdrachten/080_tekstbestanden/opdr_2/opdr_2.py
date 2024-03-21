# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random 
randomGetal = random.randint(1,100)
getal = 0 #getal is 0 omdat dit altijd lager is dan het randomgetal
aantalBeurten = 0
print(randomGetal)

# != is niet gelijk aan
while getal != randomGetal:
    getal = int(input("Raad het getal "))
    aantalBeurten += 1
    if randomGetal < getal:
        print(f"Onjuist,het getal is lager, dit is beurt {aantalBeurten}")
    elif randomGetal > getal:
        print(f"onjuist, het getal is hoger,dit is beurt {aantalBeurten}")

print(f"Gefeliciteerd, je hebt het getal geraden in {aantalBeurten} beurten!")
# met een f kun je een variable printen in een string
