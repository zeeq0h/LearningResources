#lists
friends = ["Rolph","Dylan","Cammy"]
#you want to make sense in lists
#i.e strings with strings
print(friends[0])
print(len(friends))
#prints number of objects in list

friends_info = [["Rolph", 24],["Dylan", 16],["Cammy", 30]]
print(friends_info[0])
#to get dylan's age
print(friends_info[1][1])

#lists are best suited in this form
friends_list = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27],
    ["Charlie", 37],
    ["Jen", 25],
    ["Adam", 29],
]

friends = ["Rolph","Dylan","Cammy"]
friends.append("Jen")
print(friends)
friends.remove("Rolph")
print(friends)
#friends_info.remove(["Rolph", 24])
#this would remove a list from a list