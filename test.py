import time
import math

a = 1234
b = 4321
t = time.clock()
for i in range(1000):
	c = b ** a
print(time.clock() - t)
t = time.clock()
for i in range(1000):
	c = a * math.log(b)
print(time.clock() - t)
