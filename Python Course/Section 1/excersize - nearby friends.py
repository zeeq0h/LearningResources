nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friends = input("Please enter your friends name: ")

# Add the name to the empty set
user_friends.add(friends)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
friends_nearby = user_friends.intersection(nearby_people)
print("your friend" ,friends_nearby, "is nearby")
