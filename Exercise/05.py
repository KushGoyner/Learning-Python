import os


files = os.listdir("Folder")

i = 1
for file in files:
    if file.endswith(".png"):
        os.rename("kush.png",f"{i}.png")
        i+=1
        
