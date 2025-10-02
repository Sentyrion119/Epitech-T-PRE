a = str(input("Open sesame ? : "))

def switch (a):
    if a == 42:
        print('a')
    elif a <= 21:
        print('b')
    elif a% 2 == 0:
        print('c')
    elif a / 2 <= 21:
        print('d') 
    elif a % 2 == 1 and a >= 45 :
        print('e')
    else :
        print('f') 