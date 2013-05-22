s = 0
with open('test', 'r') as f:
	for line in f:
		s += int(line)
print(s)
