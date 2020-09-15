#List comprehensions with conditionals
ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
#if the age in ages is odd, put in the odds list
print(odds)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["Jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]

print(present_friends)