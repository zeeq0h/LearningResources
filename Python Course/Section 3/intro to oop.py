"""
my_students = {
    "name": "Rolf Smith",
    "grades": [70,88,64,96],
    "average": #some sort of function, however this is not possible in a dict
}

def average_grades(student):
    return sum(student["grades"]) / len(student["grades"])

print(average_grades(my_students))
"""
#the code above can be simplified and made more effecient by using the following:

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Rolf Smith", [70,88,64,58])
student_two = Student("Logan Paul", [50, 60, 88, 100])

print(student_one.__class__)
print(student_one.name)
print(student_two.name)