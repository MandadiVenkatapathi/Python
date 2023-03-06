n = int(input("Enter the number:"))  # n=565
temp=n
rev = 0
while (n > 0):
    remind = n % 10
    rev = rev * 10 + remind
    n //= 10
if (temp== rev):
    print("is palindrome")
else:
    print("not a palindrome")