primeList = []
primeSet = set()
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		primeList.append(int(line))
		primeSet.add(int(line))

def defrac(n):
	re = []
	for i in primeList:
		if i > n:
			break
		if n % i == 0:
			re.append(i)
			while n % i == 0:
				n = n // i
	return re

count = 0
limit = 10
for i in range(2, 1000001):
	if i > limit:
		print(i - 1, count)
		limit *= 10
	count += i - 1
	if i not in primeSet:
		frac = defrac(i)
		plus = []
		newp = []
		minus = []
		for j in frac:
			count -= i // j - 1
			newp.clear()
			for k in minus:
				newp.append(j * k)
			for k in plus:
				count += i // k // j - 1
				minus.append(k * j)
			for k in newp:
				plus.append(k)
				count -= i // k - 1
			plus.append(j)
print(count)
