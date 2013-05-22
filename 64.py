data = []
temp = []
square = [i * i for i in range(2, 101)]
j = 0
result = 0
for n in range(2, 10001):
	if n == square[j]:
		j += 1
		continue
	a = int(n ** 0.5)
	temp.clear()
	data.clear()
	temp.append(n - a * a)
	temp.append(int(n ** 0.5 + a) // temp[0])
	temp.append(a - temp[0] * temp[1])
	while temp not in data:
		data.append(temp[:])
		temp.clear()
		temp.append((n - data[-1][2] ** 2) // data[-1][0])
		temp.append(int(n ** 0.5 - data[-1][2]) // temp[0])
		temp.append(-data[-1][2] - temp[0] * temp[1])
	count = data.index(temp)
	period = len(data) - count
	if period % 2 == 1:
		result += 1
print(result)
