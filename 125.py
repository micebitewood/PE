palindromic = set()
for i in range(10000):
	s = str(i)
	s1 = s[:]
	s2 = s[:-1]
	for c in s[-1::-1]:
		s1 += c
		s2 += c
	palindromic.add(int(s1))
	palindromic.add(int(s2))

print('first part ended', 100000000 ** 0.5)
c = 0
count = 0
re = set()
for k in range(1, 10000):
	a = k + 1
	b = k * k + k
	c += b - k
	for n in range(1, 10000):
		total = a * n * n + b * n + c
		if total > 100000000:
			break
		if total in palindromic:
			re.add(total)
print(sum(re))
