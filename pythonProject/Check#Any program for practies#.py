n=int(input("enter the number:"))
for i in range(1,2*n):
    for j in range(1,2*n):
        if i ==j or i+j==2*n:
            print('',end=' ')
        else:
            print(' ',end=' ')
    print()