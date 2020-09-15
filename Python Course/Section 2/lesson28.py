elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,] #this sets how miny times the loop will repeat, you dont necessary have to repeat it

for index in elements: #most users just use a _ if its not going to be used again
    print("hello world")

#you could also do

for index in range(10):
    print("look at this :P")

#or even still

for index in range(2, 20, 3): # numbers from 2 to 20 but going up in 3s
    print(index)


students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 61},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")