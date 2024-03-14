# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

# Zoek de leeftijdsgroep van de bezoeker
for categorie, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        leeftijdsgroep = categorie
        break

# Bepaal de korting
korting_percentage = kortings_percentages[leeftijdsgroep]
korting_bedrag = normale_toegangsprijs * (korting_percentage / 100)
te_betalen_bedrag = normale_toegangsprijs - korting_bedrag

# Print de output
print(f"U behoort tot de groep {leeftijdsgroep}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {te_betalen_bedrag}")