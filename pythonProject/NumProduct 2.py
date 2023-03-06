#W P P to print product of a number
n = int(input("Enter the number:"))
product=1
while(n>0):
    product *= (n%10)
    n=n//10
print("product of given number={}".format(product))