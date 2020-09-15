#list comprehension

"""
#longer way
numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)
"""

#quick way
numbers = [0, 1, 2, 3, 4]
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)
#variable = [(what variable becomes) for how many of those objects are affected]

friend_ages = [22, 31, 35, 37]
age_strings = [f"my friends age is {age} years old" for age in friend_ages]
print(age_strings)

names = ["Rolf", "Bob", "Jen"]
lowercase_names = [name.lower() for name in names]
print(lowercase_names)

friend_input = input("enter your friends name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend_input.lower() in friends_lower:
    print(f"{friend_input.title()} is one of your friends")

