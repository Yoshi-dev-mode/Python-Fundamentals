# List - is a collection of multiple values stored in a single variable.

# PRINTS LIST
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))

# LIST can store string, integer, boolean, and floats
data = ["John", 25, True, 5.5]

# ACCESS THE LIST
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# NEGATIVE INDEXING
print(fruits[-1])  # cherry

# CHANGING LIST ITEMS

fruits[1] = "mango"
print(fruits)

# APPEND METHOD
fruits.append("orange")

# INSERT METHOD
fruits.insert(1, "grape")

# REMOVE ITEMS
fruits.remove("grape")

# POP METHOD
fruits.pop()

# DELETE FRUITS
del fruits[1]

# LENGTH OF A LIST
print(len(fruits))


# CHECKING IF AN ITEM EXISTS

if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Ain't no way!")

# SLICING LISTS

numbers = [10,20,30,40,50]
print(numbers[1:4]) # [start : end]







