name = "Logan"
age = 34
print(f"you are {age}")
#using f strings to print integers

greeting = f"how are you, {name}?"
print(greeting)

#however this doesnt change if we update name variable
name = "Bob"
print(greeting)

name = "Logan"
final_greeting = "How are you, {}?"
logan_greeting = final_greeting.format(name)
print(logan_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)