matrix = []
t = []
with open('83.txt', 'r') as f:
	for line in f:
		line = line.split(',')
		t.clear()
		for num in line:
			t.append(int(num))
		matrix.append(t[:])
mat = []
for i in range(80):
	mat.append([0 for j in range(80)])
ma = 0
for i in range(80):
	ma += sum(matrix[i])
m = ma
mat[0][0] = -1
mat[1][0] = matrix[0][0] + matrix[1][0]
mat[0][1] = matrix[0][0] + matrix[0][1]
o = [[1, 0], [0, 1]]
while mat[79][79] == 0:
	for i in range(len(o)):
		if mat[o[i][0]][o[i][1]] < m:
			Min = i
			mi = o[i][0]
			mj = o[i][1]
			m = mat[mi][mj]
	if mj > 0 and mat[mi][mj - 1] == 0:
		mat[mi][mj - 1] = mat[mi][mj] + matrix[mi][mj - 1]
		o.append([mi, mj - 1])
	if mj < 79 and mat[mi][mj + 1] == 0:
		mat[mi][mj + 1] = mat[mi][mj] + matrix[mi][mj + 1]
		o.append([mi, mj + 1])
	if mi > 0 and mat[mi - 1][mj] == 0:
		mat[mi - 1][mj] = mat[mi][mj] + matrix[mi - 1][mj]
		o.append([mi - 1, mj])
	if mi < 79 and mat[mi + 1][mj] == 0:
		mat[mi + 1][mj] = mat[mi][mj] + matrix[mi + 1][mj]
		o.append([mi + 1, mj])
	mat[mi][mj] = -1
	del o[Min]
	m = ma
print(mat[79][79])
