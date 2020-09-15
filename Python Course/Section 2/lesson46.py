def add(x, y=3):
    total = x + y
    return total

print(add(5, 10)) #if you pass a number in it will replace the default (y=3)

print(add(x=3)) #named arguments


print(1, 2, 3, 4, 5, sep=" - ")