p = [1, 1, 2]
g = []
for k in range(1, 1000):
	g.append(k * (3 * k - 1) // 2)
	g.append(k * (3 * k + 1) // 2)
n = 3
flag = [1, 1, -1, -1]
while True:
	re = 0
	i = 0
	for m in g:
		if m > n:
			break
		re += p[n - m] * flag[i]
		i += 1
		i = i % 4
#	if n == 11:
#		print(p)
#		break
	p.append(re)
	if re % 1000000 == 0:
		print(re, n)
		break
	n += 1
