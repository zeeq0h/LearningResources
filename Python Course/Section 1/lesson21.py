friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_ages["Rolf"])

friends_ages["Bob"] = 20
friends_ages["Rolf"] = 25

print(friends_ages)
#dictionary does keep order
#you cannot have duplicate keys in a dictionary
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

#you can change a list of tuples into a dict

friends_list = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friends_age_list = dict(friends_list)
print(friends_age_list)