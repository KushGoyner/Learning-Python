file = open('youtube.txt','w')

try:
    file.write("Kush Goyner")
finally:
    file.close()

with open("youtube.txt",'w') as file:  #closes file of its own dont need try block and error handling
    file.write("Kush Goyner")

