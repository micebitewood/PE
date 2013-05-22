import sys

def rePrime(n, m):
	while(n > 1):
		n, m = m % n, n
	if n == 0:
		return False
	return True
def permutation(count, n):
	a = []
	for c in str(count):
		a.append(c)
	b = []
	for c in str(n):
		b.append(c)
	a.sort()
	b.sort()
	if a == b:
		return True
	return False

Min = 10
primeList = []
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		primeList.append(int(line))

def deFac(n):
	re = []
	for i in primeList:
		if i * 2 > n:
			break
		if n % i == 0:
			re.append(i)
	return re

fin = primeList.index(3037) - 1
ren = []
rem = []
Min = 10
for n in primeList[-1::-1]:
	if n > 15000:
		continue
	nIndex = primeList.index(n)
	nn = n
	ren.clear()
	c = 0
	while nn < 10000000:
		ren.append(nn)
		nn *= n
	for m in primeList[nIndex::-1]:
		mm = m
		rem.clear()
		while mm * n < 10000000:
			rem.append(mm)
			mm *= m
		for nn in ren:
			for mm in rem:
				mult = nn * mm
				if mult < 10000000:
					count = mult - nn - mm + 1
				if permutation(count, mult):
					if mult / count < Min:
						print(nn, mm, mult, count, mult / count)
						Min_n = mult
						Min = mult / count
print(Min_n, Min)
