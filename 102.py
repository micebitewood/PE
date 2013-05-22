def containOrigin(data):
	denominator = data[1] * data[4] - data[0] * data[5]
	numerator = data[0] * data[3] - data[1] * data[2]
	b = denominator / numerator
	if b < 0:
		return 0
	a = ((-data[4]) - data[2] * b) / data[0]
	if a < 0:
		return 0
	return 1
count = 0
with open('102.txt', 'r') as f:
	for line in f:
		line = line.split(',')
		points = []
		for data in line:
			points.append(int(data))
		count += containOrigin(points)
print(count)
