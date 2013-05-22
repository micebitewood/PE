ways = [[0], [0], [0], [0, 0]]
primel = []
primes = set()
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		primel.append(int(line))
		primes.add(int(line))
n = 4
count = 0
while count < 5000:
	count = 0
	pindex = 0
	ways.append([])
	prime = primel[pindex]
	while prime <= n:
		if prime > n // 2:
			pindex += 1
			prime = primel[pindex]
			ways[n].append(0)
			continue
		if prime == 2:
			ways[n].append(sum(ways[n - prime]))
		else:
			ways[n].append(sum(ways[n - prime][pindex:]))
		if n - prime in primes:
			ways[n][pindex] += 1
		count += ways[n][pindex]
		pindex += 1
		prime = primel[pindex]
	n += 1
print(n - 1, ways[n - 1])
print(count)
