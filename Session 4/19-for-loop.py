# Simple Loop
for i in range(1, 6):
    print("Number:", i)

# Looping with steps
for i in range(1, 10, 2):
    print(i)

# Looping Backwards
for i in range(5, 0, -1):
    print(i)

# Looping Through Strings
for letter in "Python":
    print(letter)

# Looping Through Lists
numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)

# Using len() and Index
names = ["Ana", "Mark", "John"]

for i in range(len(names)):
    print(names[i])

# break Statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue Statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Nested Loops
for i in range(3):
    for j in range(3):
        print(i, j)