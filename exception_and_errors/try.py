a = input("Enter a number: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)


try:
    num = int(input("Enter: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Entered number is not a number")
except IndexError:
    print("Invalid index access.")
finally:
    print("Thank you for the cooperate. ")