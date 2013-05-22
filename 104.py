import decimal
import math

pand = set()
with open('pandigits.txt', 'r') as f:
	for line in f:
		pand.add(int(line))
a, b = 1, 1
count = 2
limit = 10
while True:
	a, b = a + b, a
	count += 1
	if count > limit:
		limit *= 10
		print(count)
	if a < 100000000000000000:
		continue
	if a % 1000000000 in pand:
		c = str(a)
		c = int(c[:9])
		if c in pand:
			print(count)
			break
