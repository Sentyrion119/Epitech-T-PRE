x = int(input("entrer un nombre et vous aurait la somme de celui-ci : "))
result = 0
for i in range(len(str(x))):

    result += int(str(x)[i])

print (result)