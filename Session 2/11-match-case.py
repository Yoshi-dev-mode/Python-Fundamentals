
# match-case = It helps make long chains of if-elif-else statements simpler and cleaner.

day = input("Enter a day: ")

if day == "Monday":
    print("Start of the week!")
elif day == "Friday":
    print("Almost weekend!")
elif day == "Saturday" or day == "Sunday":
    print("Weekend time!")
else:
    print("Midweek days.")


# match day:
#     case "Monday": 
#         print("Start of the week!")
#     case "Friday": 
#         print("Almost weekend!")
#     case "Saturday" | "Sunday": 
#         print("Weekend time!")
#     case _: 
#         print("Midweek days.")




x = 7
if x % 2 == 0:
    print("Even")
elif x > 5:
    print("Odd and Big")
else:
    print("Odd and Small")



