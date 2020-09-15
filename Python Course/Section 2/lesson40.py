#set and dictionary comprehensions

#set comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["Jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)

present_friends = {name.title() for name in present_friends}

print(present_friends)


#disctionary comprehension
friends_two = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timer = {
    friends_two[i]: time_since_seen[i]
    for i in range(len(friends_two))
    if time_since_seen[i] > 5
}

print(long_timer)