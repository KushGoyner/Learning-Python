import os

if(not os.path.exists("data")):
    os.mkdir("data")

# os.rename("data","mkdir")

print(os.listdir("data"))

 