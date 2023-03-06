l = [10, 20, 90, 50, 100, 1, 200]
for i in range(len(l)):
    if i == 0:
        l.pop(i)
        if len(l) != 0:
            middle = len(l)//2-1
    elif i == middle:
        l.pop(i)
    elif i == (len(l) - 1):
        l.pop(i)
print(l)
