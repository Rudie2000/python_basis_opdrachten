# Opdracht 4 condities
# Naam student:
# Groep:


# Gegeven lijst met toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Bouw een lijst op met beschikbare toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze uit de beschikbare toppings
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze in de lijst met beschikbare toppings staat
gevonden = False
for topping, prijs in toppings:
    if keuze.lower() == topping:
        gevonden = True
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        break

# Als de keuze niet is gevonden, druk dan een foutmelding af
if not gevonden:
    print("Uw keuze zit niet in ons assortiment")


# Hier de rest van jouw code...