# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

geencrypt= []
tekst = "Deze zin wil ik gaan encrypten, dat lijkt me leuk"# input("Voer hier de tekst in die je wil encrypten ")
#print(ord(tekst))


# Opdelen in een lijst van karakters
char_list = [char for char in tekst]
for getal in char_list:
    ord1 = (ord(getal))
    #print(ord1)
    print(chr(ord1 + 5))
    geencrypt.append(chr(ord1 + 5))

test = ''.join(geencrypt)
print(test)