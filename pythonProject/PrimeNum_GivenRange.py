l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in l:
    if (num == 0 or num == 1):
        continue
    for i in range(2, num):
        if (i % num == 0):
            print("It's not a prime numbers list", num)
            break
        else:
            print("list of prime numbers in given list:", num)



