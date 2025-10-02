a = int(input("Ecrivez un nombre : "))
for x in range (2, (a//2)+1):
    multiple =""
    for i in reversed(range (2, a)):
        if i % x == 0:
            multiple+= " "+ str(i)
    print (multiple)