a = str(input("Ecrivez un mot ou une phrase : "))
b = ""
for i in range (len(a)):
    b += a[i]*2
print (b)