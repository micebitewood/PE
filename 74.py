fvalue = [1]
fnum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
f = 1
for i in range(1, 10):
	f *= i
	fvalue.append(f)
factorial = dict(zip(fnum, fvalue))
s = []
count = 0
f = [0 for i in range(3000000)]
for i in range(1000000):
	if f[i] != 0:
		continue
	j = i
	s.clear()
	while True:
		Sum = 0
		s.append(j)
		for c in str(j):
			Sum += factorial[c]
		if f[Sum] > 0:
			if len(s) + f[Sum] == 60:
				count += 1
			Index = len(s)
			s.append(Sum)
			break
		elif Sum not in s:
			j = Sum
		else:
			Index = s.index(Sum)
			if len(s) == 60:
				count += 1
			break
	for j in range(len(s) - 1, -1, -1):
		if j <= Index and f[s[j]] == 0:
			if j == Index == len(s) - 1:
				f[s[j]] = 1
			elif j == Index:
				f[s[j]] = f[s[j + 1]]
			else:
				f[s[j]] = f[s[j+1]] + 1
		elif j > Index:
			f[s[j]] = len(s) - Index
print(count)
