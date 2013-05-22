def next(n):
	re = 1
	r = int(n ** 0.5) + 1
	for i in range(2, r):
		if n % i == 0:
			if i * i == n:
				re += i
			else:
				re += i + n // i
	return re
flag = [0 for n in range(1000000)]
re = []
limit = 100
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		flag[int(line)] = -1
for n in range(1, 1000000):
	if flag[n] != 0:
		continue
	if n > limit:
		print(n)
		limit *= 10
	m = n
	re.clear()
	re.append(m)
	while True:
		m = next(m)
		if m > 1000000 or flag[m] != 0 or m == 1:
			for a in re:
				flag[a] = -1
			break
		if m in re:
			i = re.index(m)
			for a in re[:i]:
				flag[a] = -1
			j = len(re) - i
			for a in re[i:]:
				flag[a] = j
			break
		re.append(m)
Max = 0
for n in flag:
	if n > Max:
		Max = n
print(flag.index(Max))
