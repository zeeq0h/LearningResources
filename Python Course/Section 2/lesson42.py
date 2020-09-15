friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends):
    print (f"{counter} : {friend}")


print(list(enumerate(friends, start=1)))
#this is the same as
print(list(zip([0, 1, 2], friends)))

print(dict(enumerate(friends)))