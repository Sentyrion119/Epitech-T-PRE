
a = int(input("merci de donner un nombre : ")), str(input("merci d'écrire un mot ou une phrase : "))
 
vowel = "a"
find = list(filter(lambda tup: vowel in tup, a[0]))
#for i in range (len(a)):
 #   x = a[1].find("a")
  #  if x :
   #     print(a[0])

if a[0] == 0:
    exit
elif find:
    print('oura')
elif a[0] >= 42 :
    print(a[0])
else :
    print(a[1])