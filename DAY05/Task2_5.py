list = [1, 2, 3, 4, 5]
newList =[]
maxi = list[0]
#list.sort(reverse=True)
#print(list)
        
while len(list)>0:
    maxi = list[0]
    for i in range(len(list)):
        if maxi < list[i]:
            maxi = list[i]
    newList.append(maxi)
    list.pop(list.index(maxi))
    
print(newList)
    
        