s = {2,4,2,66}
print(s)
print(type(s))
k = {}
print(type(k))
l = set()


for v in s:
    print(v)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

print(s1.union(s2))

s1.update(s2) # update s1
print(s1,s2)

s3 = s1.union(s2) #union
s4 = s1.intersection(s2) #intersection
s5 = s1.symmetric_difference(s2)  # 

print(s3,s4,s5)

s6 = s1.difference(s2)
print(s6)

print(s1.isdisjoint(s2)) #check for disjoint
print(s1.issubset(s2))  #check for subset
print(s1.issuperset(s2)) #check for superset

s1.add(44) # add element
print(s1)
s1.discard(44) # remove element
print(s1)

j = s1.pop()  # delete last element and returns it
print(j)