''' Exercise 1: Write a function to greet the user by name.

Instructions:

Define a function called that takes one parameter, (name).
Inside the function, create a greeting message that includes the name passed as an argument.
Print the greeting message using the print function '''

def greet(name="Friend"):
    return f"Hello, {name}!"
# print(greet())
print(greet(input('What\'s your name? ').capitalize()))
    