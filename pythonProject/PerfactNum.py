n=int(input("enter the number:"))
for i in range(2,n):
    if i%n==0:
        print("it's not a prime number",n)
        break
else:
    print("it's a prime number:",n)