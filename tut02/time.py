import time

def usingWhile():
    i = 0
    while i<50000:
        i = i+1
        print(i)

def usingFor():
    for i in range(50000):
        print(i)


init = time.time()
print(init)
usingFor()
t=time.time()-init
usingWhile()
print(t)
print(time.time()-init-t)


# sleep

print(5)
time.sleep(5)
print("haha")


# time

t = time.localtime()
formated = time.strftime("%Y-%m-%d %H:%M:%S",t)

print(formated)