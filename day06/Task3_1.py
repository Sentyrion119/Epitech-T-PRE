a = "Bonjour"
b = "Bonjour !"
c = "Vous 2"

def functionA():
    if a.isalpha():
        return True
    else :
        return False

def functionB():
    if set('[~!@#$%^&*()_+{}":;\']+$').intersection(b):
        return True
    else :
        return False
    
def functionC():
    if any(char.isdigit() for char in c):
        return True
    else :
        return False
    
if functionA() and functionB() and functionC():
    print ('Trop fort')
else :
    print('Trop nul')