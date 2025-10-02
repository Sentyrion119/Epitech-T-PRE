
def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O")
def ham () :
    print (" ============ ")

def sand(a):
    for i in range(a):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()
        print(' ')
        
a = input("veuillez mettre le nombre de Burger que vous souhaitez : ")

if a.isdigit():
    if int(a) >= 1 :
        sand(int(a))
    elif int(a) == 0:
        print("Merci de mettre un nombre supérieur a zéro")
else  :
    print("Merci de mettre un nombre.")

