import functools
import time

@functools.lru_cache(maxsize=None)
def fx(x):
    time.sleep(5)
    return x*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 20")
print(fx(6))
print("done for 20")
print(fx(2))
print("done for 20")

# value of these has been computed before hence these values are cached and are returned
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 20")
print(fx(6))
print("done for 20")
print(fx(2))
print("done for 20")