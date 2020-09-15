#if statements 
friend = "Rolf"
user_name = input("What is your name? ")

if user_name == friend:
    print("Hello friend!"),
    print("this runs too.")
else:
    print("Hello, stranger!")

#this is outwith the loop so will run anyway
print("This runs anyway.")


if 5:
    print("runs")

#if a variable evaluates to true it will always run

name = input("enter your name: ")
print(bool(name))
#it will always be true if a string is entered
if name:
    print("we know your name.")


friends_list = ["Rolf", "Jen", "Anne"]
family = ["Jen", "Charlie"]

user_name_new = input("Enter your name: ")

if user_name_new in friends_list:
    print("Hello, friend!")
elif user_name_new in family:
    print("Hello, family!")
else:
    print("I dont know you")
#there is no limit to how many elif statements you can have 
#they are evaluated in order
#so the first will run if true and the rest are skipped