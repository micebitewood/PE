import time
import decimal

a = 8 ** 9876
t = time.clock()
for i in range(20):
	decimal.Decimal(a + i).log10()
print(time.clock() - t)
t = time.clock()
for i in range(20):
	b = str(a + i)
print(time.clock() - t)
