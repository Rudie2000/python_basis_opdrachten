# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering? \n") 
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? \n") 
vraag3 = input("Wat vind jij de mooiste stad van Nederland? \n ")

#print(input(vraag1), input(vraag2), input(vraag3))

lst = []
lst.append(vraag1)
lst.append(vraag2)
lst.append(vraag3)
print(lst)
fo = open('opdracht1.1.txt', 'wt')
for i in lst:
    fo.write(i + "\n")
fo.close()