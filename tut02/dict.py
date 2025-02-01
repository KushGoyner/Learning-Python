d = {"name":"Kush",
    "age":24,
    "graducated":False     
}


print(d)
print(d["name"]) # if value not possible then return Error
print(d.get("graducated")) # if value not possible then return true 
print(d.keys())  # return keys

for key in d.keys():
    print(d[key])

print(d.items())


for key,value in d.items():
    print(key,value)

# Methods

dict1 = {122:45,123:89,567:69,670:69}
dict2 = {222:67,566:90}

dict1.update(dict2)  # update the dict1 acc to dict2

# dict1.clear()  clear the dictionary

dict1.pop(122)   # pop 122 key value
dict1.popitem() #remove last key value

del dict1[122] #delete 122 value


