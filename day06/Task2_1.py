def recur_sum(num):
   if num <= 1:
       return num
   else:
       return num + recur_sum(num-1)

num = input("Merci de mettre un nombre :")

if num.isdigit() == True and int(num) <= 0 :
   print("Merci d'écrire un chiffre positif")
elif num.isdigit() == True and int(num) > 0:
    num = int(num)
    print("La somme est",recur_sum(num))
else:
   print("merci d'écrire un chiffre ou un nombre")