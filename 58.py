import math
import time

t = time.clock()
nums = set()
numl = []
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for i in f:
		j = int(i)
		nums.add(j)
		if j <= 100000:
			numl.append(j)
diag, diff, count, pcount, rate, j = 1, 2, 1, 0, 1, 1
print(time.clock() - t)

def is_prime(n):
	if n > 1000000:
		s = int(n ** 0.5)+1
		for a in numl:
			if a <= s:
				if diag % a == 0:
					return 0
		return 1
	else:
		if n in nums:
			return 1
	return 0

while rate >= 0.1:
	for i in range(4):
		diag = diag + diff
		count += 1
		pcount += is_prime(diag)
	rate = pcount / count
	diff += 2
print(diag, diff-1, rate)
print(time.clock() - t)
