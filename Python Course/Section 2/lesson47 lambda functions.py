#def divide(x, y):
#    return x / y

divide = lambda x, y: x / y #if there is no name assigned to it python will destroy it O.O

print(divide(15, 3))

"""
def average(sequence):
    return sum(sequence / len(sequence))

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 90, 80)},
    {"name": "Jen", "grades": (98, 99, 95, 100)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))
"""
#the code above can be simplified like this
average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 90, 80)},
    {"name": "Jen", "grades": (98, 99, 95, 100)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))