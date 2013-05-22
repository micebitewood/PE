import math

ma = 0
lines = 0
ma_line = 0
with open('99.txt', 'r') as f:
	for line in f:
		data = line.split(',')
		b = int(data[0])
		a = int(data[1])
		lines += 1
		if ma < a * math.log2(b):
			ma = a * math.log2(b)
			ma_line = lines
print(ma_line)
