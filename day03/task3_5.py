from collections import Counter
a = str(input("merci d'écrire une phrase : "))
counts=Counter(a)
for i in a:
    print(i,counts[i])