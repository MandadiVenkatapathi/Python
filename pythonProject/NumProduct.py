#W P P to print product of a number
def Product(n):
    product = 1

    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product


# Driver Code
n = int(input("Enter the number:"))
print("-" * 50)
print("product of given number={}".format(Product(n)))
print("-" * 50)