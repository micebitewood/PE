with open('79.txt', 'r') as f:
	data = f.read()
	data = data.split()
re = []
for i in range(0, 10):
	re.append([])
for num in data:
	for i in range(0, 2):
		for j in range(i+1, 3):
			if num[j] not in re[int(num[i])]:
				re[int(num[i])].append(num[j])
s = []
j = 1
for i in re:
	print('{0} {1}'.format(len(i), i))
while j < 10:
	for i in range(0, 10):
		if len(re[i]) == j:
			k = 0
			while k<j:
				if re[i][k] not in s:
					s.append(re[i][k])
				k += 1
			s.append(str(i))
			break
	j += 1
print(s)
