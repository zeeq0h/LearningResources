#while loops
#repeat a code an undified number of times until the user 'breaks' the loop
user_input = input("Do you wish to run the program? (y/n) ")

while user_input == "y":
    print("We're running!")
    user_input = input("Do you wish to run the program? (y/n) ")

print("We stopped running.")
    