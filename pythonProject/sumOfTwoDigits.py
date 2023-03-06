n=int(input("Enter the number:"))
count=0
while(n>0):
    r=n%10
    count+=r
    n=n//10
print("-"*50)
print("sum of digits in the number are:",count)
print("-"*50)