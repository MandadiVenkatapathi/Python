num = int(input("Enter a number: "))
if(num > 1):
   for i in range(2,num):
       if (num % i) == 0:
           print("is not a prime number",num)
           break
   else:
       print("is a prime number",num)
