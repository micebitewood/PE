data = []
with open('81.txt', 'r') as f:
	for line in f:
		line = line.split(',')
		line = [int(i) for i in line]
		data.append(line)
for i in range(1, 80):
	data[0][i] += data[0][i-1]
	data[i][0] += data[i-1][0]
for i in range(1, 80):
	for j in range(1, 80):
		if data[i-1][j] > data[i][j-1]:
			data[i][j] += data[i][j-1]
		else:
			data[i][j] += data[i-1][j]
print(data[79][79])
