"""
STRING METHODS:
    1. string.captalize() - capitalized the first letter
    2. string.upper() - capitalized all of the letters
    3. string.lower() - lower case all of the letters
    4. string.find() - finds the specific letter (-1 = not found) (0 above =found)
    ["h","e","l","l","o"] --> [0,1,2,3,4]
    5. string.casefold() - stricker than lower case when it comes to unique symbol
    6. string.count() - counts how many letter in a variable
    7. string.startswith("") - True or False
    8. string.endswith("") - True or False
    9. string.center(width, symbol) - centers the strings
    10. string.ljust(width, symbol) - left justify strings
    11. string.rjust(width, symbol) - right justify strings
    12. string.is___() - output: booleans

"""

python_circuit = "com" 

# DIFFERENCE BETWEEN lower() and casefold()
text1 = "Straße" # ß -> ss = german word

print(text1.lower())
print(text1.casefold())  

