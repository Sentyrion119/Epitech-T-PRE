import re
a = str(input("mot ? : "))
a = a.lower()   
nphrase = re.sub(r"[^a-zA-Z]","", a)        
def newTry(a):
    if a[0] == a[-1]:
        return True

    if a[0] != a[-1]:
        return False
    
    return newTry(a, a[+1], a[-1])

if newTry(a):
    print("yes")
else :
    print("no")