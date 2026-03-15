# dictionary - stores data using key : value pairs

# PRINTS WHOLE DICTIONARY
student = {
    "name": "John",
    "age": 20,
    "course": "Engineering"
}

print(student)

# ACCESSING DICYIONARY VALUES
print(student["name"])
print(student["age"])

# ADDING ITEMS TO A DICTIONARY
student["grade"] = "A"
print(student)

# REMOVING ITEMS
student.pop("age")
del student["name"]

# LENGTH OF THE DICTIONARY
print(len(student))

# CHECK IF KEY EXISTS
if "name" in student:
    print("Name exists")

# DICTIONARIES INSIDE LISTS
students = [
    {"name": "John", "age": 20},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 21}
]

print(students[0]["name"])




