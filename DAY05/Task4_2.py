liste=["Guillaume", 2 ,"Nadir", 2 ,"Corentin", "Nadir"]
newListe = []
print(list(set(liste)))

for i in liste:
    if i not in newListe:
        newListe.append(i)
        
print (newListe)