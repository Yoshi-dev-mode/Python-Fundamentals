"""
Nested conditional statement - putting one if statement inside another.
                             - It is like asking “if this is true, then check another thing.”

"""

age = 18
if age >= 18:
    if age < 21:
        print("You are an adult but not yet 21.")
    else:
        print("You are 21 or older.")
else:
    print("You are a minor.")
