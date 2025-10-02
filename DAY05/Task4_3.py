liste =[
[" Monday  "," 3:30 PM", "Joe", "Sam"] ,
[" Monday  "," 4:30 PM", "Bob", "Alice"] ,
[" Tuesday  "," 3:30 PM", "Joe", "Bob", "Alice", "Sam"] ,
[" Tuesday  "," 9:30 AM", "Joe", "Bob"]
]

a = str(input("votre nom ? : "))

for i in range(len(liste)):
    if a in liste[i]:
        print(liste[i][:2])