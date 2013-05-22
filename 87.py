square = []
cube = []
fourth = []
result = set()
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		n = int(line)
		mult = n * n
		if mult > 50000000:
			break
		square.append(mult)
		mult *= n
		if mult > 50000000:
			continue
		cube.append(mult)
		mult *= n
		if mult > 50000000:
			continue
		fourth.append(mult)
for i in square:
	for j in cube:
		for k in fourth:
			if i + j + k < 50000000:
				result.add(i + j + k)
print(len(result))
