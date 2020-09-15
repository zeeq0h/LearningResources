def greet():
    print("Hello")

hello = greet

hello()
############################################################

"""
the funtions on their own.

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)
"""

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum, #you can remove the lambda section to optimise code as it basically repeats itself lower down the line
    "top": max
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 90, 80)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"student: {name}")
    operation = input("Enter 'average, 'total' or 'top' ")

operation_function = operations[operation]
print(operation_function(grades))