#while loops
#repeat a code an undified number of times until the user 'breaks' the loop

user_input = int(input("Enter a value between 1-10, please: "))

while user_input < 1 or user_input > 10:
    user_input = input("error, please enter a value between 1 and 10 only: ")
    if user_input >= 1 and user_input <=10:
        print("you printed a number between 1 and 10")

print(pi)