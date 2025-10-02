#task 2.1
user = []
nb = '1'
i = int(input("donner un chiffre : "))
for j in range(i):
    user.append(nb)
    nb+='1'

user = list(map(int, user))      
somme = sum(user)
affiche = ""
affiche = (' + '.join(map(str, user)))

a = int(input("donner un puissance : "))
resultat = somme ** a
print ('Resultat de la puissance de',affiche,'est',resultat)