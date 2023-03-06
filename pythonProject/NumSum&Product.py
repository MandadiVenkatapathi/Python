#W P P to print sum & product of a number
n = int(input("Enter the number:"))
sum=0
mul=1
while(n>0):
    rem=n%10
    sum+=rem
    mul*=rem
    n=n//10
print("Sum of given number:",sum)
print("product of given number:",mul)