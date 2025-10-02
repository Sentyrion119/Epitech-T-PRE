
def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print (" O O O O O O")
def ham () :
    print (" ============ ")

def sand(a, b=False):
    for i in range(int(a)):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()
        print(' ')
    
    if b:
        for i in range(int(a)):
            bread()
            lettuce()
            tomato()
            lettuce()
            tomato()
            bread()
            print(' ')

def nb() :
    input("Combien en voulez-vous ? : ")


def veg() :
    input("voulez-vous un Veg Burger, oui ou non: ")

while veg() != "oui" and veg() != "non" :
        veg()

if veg() == 'oui':
    nb() , True
else :
    nb()







sand(nb(), veg())


