# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

#a^2 + b^2 = c^2

import math

a = int(input("Geef de lengte van de eerste zijde \n"))

b = int(input("Geef de lengte van de tweede zijde \n"))

kwadrant_schuine_zijde = (a ** 2) + (b ** 2)

schuine_zijde = (math.sqrt(kwadrant_schuine_zijde))

print(f"De lengte van de schuine zijde is: {schuine_zijde} ")