# Function - is a block of code that runs only when it is called.

"""
def greet():
    print("Hello!")

# Greet function can be reuse
greet()
greet()
greet()
"""

"""
    def → used to define a function

    greet → function name

    () → parentheses

    : → start of function code
"""


# FUNCTIONS WITH PARAMETERS
"""
def greet(name):
    print("Hello!", name)

greet("Yoshi")
greet("Bryan")
greet("Chriance")
greet("Nathaniel")
greet("Ken")
"""

# FUNCTIONS WITH MULTIPLE PARAMETERS
"""
def add(a, b):
    result = a + b
    print(result)

add(5, 3)
"""

# FUNCTIONS CAN RETURN VALUES
"""
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
"""

# DEFAULT PARAMETERS
"""
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bryan")
"""

# FUNCTIONS WITH LIST
"""
def print_fruits(fruits):
    print(fruits)

fruits = ["apple", "banana", "mango"]

print_fruits(fruits)
"""

# FUNCTIONS WITH DICTIONARIES
"""
def show_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])

student = {
    "name": "John",
    "age": 20
}

show_student(student)
"""
