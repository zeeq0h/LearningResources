friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

#first number is the starting point, and the second point is the finishing point
print(friends[2:4])

#or you can do this to get all friends except the 1st one
print(friends[1:])
#or all friends except number 4 
print(friends[:4])

print(friends[-3:])
#this prints the list but counting backwards technically but also skips -4

print(friends[:-2])
#this will print all except the last 2 elements

print(friends[-3:-1])