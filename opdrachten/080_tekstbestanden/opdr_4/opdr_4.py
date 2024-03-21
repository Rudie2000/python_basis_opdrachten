# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

vraag1 = input("1. Wat is je voornaam \n") 
vraag2 = input("2. Wat is je achternaam \n") 
vraag3 = input("3. Wat neem je mee aan drank \n ")
vraag4 = input("4. Wat neem je mee om te eten? \n ")

lst = []
lst.append(vraag1)
lst.append(vraag2)
lst.append(vraag3)
lst.append(vraag4)

print(lst)
with open("opdracht_080_04.txt", "a") as file:
    file.write("----\n")
    file.write(f"voornaam: {lst[0]}\n")
    file.write(f"achternaam: {lst[1]}\n")
    file.write(f"drank: {lst[2]}\n")
    file.write(f"eten: {lst[3]}\n")
  
