age = int(input("Enter your age: "))
#and statements
can_learn_programming = age > 0 and age <= 150

print(f"you can learn programming: {can_learn_programming}.")

#or statements
usually_working = age < 18 or age >= 65
print(f"At {age}, you are usually not working {usually_working}")

#trues and falses
print(bool(35))
print(bool("rolph"))
print(bool(0))
print(bool(""))

x = True and False
print(x)

#so 

z = 35 and 0
print(z)
#if the first value is true it goes to the next value
#if the first value is false it will stay at false

#or will give the first value if it is true
#or will go to the next value if the first is false

print(not False)
#prints true
print(not True)
#prints false