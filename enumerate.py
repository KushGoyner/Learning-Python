x = ("kush","love","shyam")
y = enumerate(x)
print(list(y))

file = open("test.py")
file1 = open("test1.py","w")

file1.write("print(\"HelloWorld\")")

read = file.read()

print(read)