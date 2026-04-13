# Example 1
i = 1

while i <= 5:
    print("Number:", i)
    i += 1

# Example 2
choice = "yes"

while choice == "yes":
    print("Hello!")
    choice = input("Continue? (yes/no): ")

# Example 3

number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter a number (0 to stop): "))