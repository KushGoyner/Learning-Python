def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def divide(a,b):
    return a/b

def floorDivide(a,b):
    return a//b
def expo(a,b):
    return a**b
def mult(a,b):
    return a*b


def main():
    while True:
        print("Calculator: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Divide")
        print("4. Multiply")
        print("5. Floor Divide")
        print("6. Power")
        print("7. to Exit")
        a = int(input("Enter choice number: "))

        match a:
            case 1:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(add(a,b))
            case 2:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(sub(a,b))
            case 3:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(divide(a,b))
            case 4:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(mult(a,b))
            case 5:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(floorDivide(a,b))
            case 6:
                a = int(input("Enter first number"))
                b = int(input("Enter second number"))
                print(expo(a,b))
            case 7:
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()