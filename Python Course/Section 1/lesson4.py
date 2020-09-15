my_string = "Hello, world!" #this is a string
print(my_string)

string_with_quotes = "Hello it's me." #if using single ' it would cause an error
another_with_quotes = 'he said "You are amazing!" yesterday.' #this is another use for 

multiline = """Hello, world!
my name is Logan welcome to my programn.
"""
print(multiline)

name = "Logan"
greeting = "Hello, "  + name
print(greeting)

#integers must be converted to strings for joining together
age = 34
age_as_str = str(age)
words = greeting + age_as_str
print(words)