double = lambda x:x*2
cube = lambda s:s*s*s

print(double(7))
print(cube(3))

avg = lambda x,y,z:(x+y+z)/3

print(avg(1,2,3))


def app(fx,value):
    return 6 + fx(value)

print(app(cube,5))