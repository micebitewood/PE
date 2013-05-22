import time

tc = time.clock()

re = set()

def gcd(i, j):
	while i > 1:
		i, j = j % i, i
	if i == 1:
		return True
	else:
		return False

rem = set()
for i in range(1, 866, 2):
	for j in range(i + 2, 750000, 2):
		if i * j >= 750000:
			break
		if gcd(i, j):
			a = i * j
			b = (j * j - i * i) // 2
			c = (j * j + i * i) // 2
			s = a + b + c
			t = s
			while t <= 1500000:
				if t in re:
					rem.add(t)
				else:
					re.add(t)
				t += s
for n in rem:
	re.remove(n)
print(len(re))
print(time.clock() - tc)
