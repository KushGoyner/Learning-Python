list =  [1,2,3,"Kush",[8,"goyner",5],True,7.4,]
 
for i , index in enumerate(list):
    print(i,index)

if 2 in list:
    print("yes")
else:
    print("no")


lst = [i*i for i in range(10+1)]
print(lst)

list.append(111)
# list.sort(re
# verse=True)
list.reverse()
print(list)

list.index(1)  # gives the index of first occurance of given parameter
list.count(1) # return no of times the given parameter appear
list.insert(2,"shyam")  #insert at given index
