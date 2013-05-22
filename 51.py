data = []
with open('prime10000000.txt', 'r') as f:
	f.readline()
	for line in f:
		s = str(int(line))
		temp = []
		if len(s) > 3 and len(s) < 7:
			for c in s:
				temp.append(c)
			data.append(temp)
for c in '012':
	redundancy = []
	a = []
	for s in data:
		if s.count(c) == 3 and (s not in redundancy):
			a.clear()
			num = s[:]
			a.append(num.index(c))
			num.remove(c)
			a.append(num.index(c) + 1)
			num.remove(c)
			a.append(num.index(c) + 2)
			num.remove(c)
			count = 0
			for st in data:
				if len(st) == len(num) + 3:
					if (a[0] == 0) or (st[a[0]-1] == num[a[0]-1]):
						if st[a[0]] == st[a[1]] == st[a[2]]:
							numt = st[:]
							del numt[a[2]]
							del numt[a[1]]
							del numt[a[0]]
							if numt == num:
								if st not in redundancy:
									redundancy.append(st)
								count += 1
								if count == 8:
									print(st, a)
									break
			if count == 8:
				redundancy.clear()
