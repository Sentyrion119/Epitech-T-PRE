import random

a = []
newA=[]
for i in range (100000):
    a.append(random.randint(1,100000))

#e=0
#while len(a)>0:
#    maxi = a[0]
#    for i in range(len(a)):
#        if maxi < a[i]:
#            maxi = a[i]
#    newA.append(maxi)
#    a.pop(a.index(maxi))
#    print(e)
#    e+=1
    
#print(a)

n = len(a)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if a[j] > a[j+1]:
      a[j], a[j+1] = a[j+1], a[j]
      swapped = True
  if not swapped:
    break

print(a)