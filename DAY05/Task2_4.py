list = [5, 2, 4, 3, 1]
mini = list[0]
maxi = list[0]
#print(min(list))
#print(max(list))

for i in range(len(list)):
    if maxi < list[i]:
        maxi = list[i]
    elif mini > list[i]:
        mini = list[i] 
           
print(maxi)
print(mini)
        