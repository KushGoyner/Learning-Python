a = int(input("Enter a Value: "))

if(not (5<a<9)):
    raise ValueError("value should be between 5 and 9")

class CustomError(Exception):
    pass


try:
    pass
except CustomError:
    pass