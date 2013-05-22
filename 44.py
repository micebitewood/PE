with open('pentagon', 'r') as f:
	data = []
	for line in f:
		data.append(int(line))
n = 1
while n < 1000:
	m = 0
	while m < n:
		if data[n] - data[m] in data[0:n]:
			if data[n] + data[m] in data[n:n+m]:
				print(n + 1, m + 1, data[n] - data[m])
		m += 1
	n += 1
'''
n = 2
a = 4
while n < 200:
	m = 1
	b = 1
	while m < n:
		k = 1
		c = 1
		while k < n:
			if 3 * (a - b - c) == n - m - k:
				l = n
				d = a
				while l < m + n:
					if 3 * (a + b - d) == n + m - l:
						print(n, m)
					d += l
					l += 1
					d += l
			c += k
			k += 1
			c += k
		b += m
		m += 1
		b += m
	a += n
	n += 1
	a += n
'''
