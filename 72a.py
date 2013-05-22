prime = []
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		prime.append(int(line))

MAX = 2000
count = MAX * (MAX - 1) // 2
minus = []
plus = []
newm = []
for n in prime:
	if n > MAX:
		break
	c = MAX // n - 1
	count -= (c + 1) * c // 2
	newm.clear()
	for m in plus:
		newm.append(n * m)
	for m in minus:
		t = n * m
		if t > MAX:
			continue
		c = MAX // t -1
		count += (c + 1) * c // 2
		plus.append(t)
	for m in newm:
		minus.append(m)
		c = MAX // m - 1
		count -= (c + 1) * c // 2
	minus.append(n)
print(count)
