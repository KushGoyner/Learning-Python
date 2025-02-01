# Strings are immutable
a = "!!Kush!!! ! Goyner !"
print(len(a))  # Length
print(a[:-8]) # slicing (-ve index == len(str) - given negative no.)
print(a.upper()) ## toUpper
print(a.lower()) ## toLower
print(a.rstrip("!")) # strip the given paramenter from last of the string
print(a.replace("Kush","love")) # replace you already knows
print(a.split(" ")) ## Split the string according to given parameter and store each in list
print(a.capitalize()) # Capitalize first letter 
print(a.center(50))  # 50 = lenght of string + len(a) ADD extra space start of string
print(a.count("Kush")) # Number of times given parameter appears
print(a.endswith("!")) # if the string ends with given parameter (True or False)
print(a.find("G")) # Find the first occurance of the given parameter and return INDEX
print(a.index("Kush")) # given the index of given parameter if not found gives error 
print(a.isalnum()) # true if not contains special char instead false
print(a.islower())  # true for if all char lower else false
print(a.isprintable()) #is printable
print(a.swapcase()) # lower to upper and upper to lower