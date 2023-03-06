l=[0,0,0,1,2,3,4,5,678,0,0]
even,odd=0,0
for i in range(0,len(l)):
    if i==0:
        x=l.count(i)
    elif(l[i]%2==0):
        even+=1
    else:
        odd+=1
print("Zeros:",x)
print("Evens:",even)
print("Odds:",odd)
