data = []
t = []
with open('82.txt', 'r') as f:
	for line in f:
		t.clear()
		line = line.split(',')
		for d in line:
			t.append(int(d))
		data.append(t[:])
re = []
for i in range(80):
	re.append([0 for j in range(80)])
for i in range(80):
	re[i][0] = data[i][0]
for j in range(1, 80):
	for i in range(80):
		Min = re[i][j - 1]
		for k in range(80):
			if k == i or (re[k][j - 1] + data[k][j]) >= Min:
				continue
			temp = re[k][j - 1]
			flag = 1
			if k > i:
				flag = -1
			for l in range(k, i, flag):
				temp += data[l][j]
			if temp < Min:
				Min = temp
		re[i][j] = Min + data[i][j]
Min = re[0][79]
for i in range(80):
	if re[i][79] < Min:
		Min = re[i][79]
print(Min)
