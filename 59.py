with open('59.txt', 'r') as f:
	data = f.read()
	data = data.split(',')
with open('59a.txt', 'w') as f:
	for i in data:
		f.write(i)
		f.write('\n')
