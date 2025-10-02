a = str(input("Merci d'écrire une phrase : "))
newWord = next(zip(*a.split()))
newA = ''.join(newWord)
print (newA)