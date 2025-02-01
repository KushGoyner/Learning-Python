for i in range(1,10,2):
    print(i)

for i in range(4):
    for j in range(i):
        print('*',end="")
        if j == 5:
            continue
        if j == 4:
            break
    print()

i = 0
while i <3 :
    print(i)
    i+=1

#for loop with else (execute else only if loop is not breaked )

for i in range(5):
    print(i) 

else:
    print("Sorry no i")

