matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
mat = []
for i in range(5):
	mat.append([0 for j in range(5)])
mat[0][0] = -1
mat[1][0] = matrix[0][0] + matrix[1][0]
mat[0][1] = matrix[0][0] + matrix[0][1]
ma = 25000
m = ma
o = [[1, 0], [0, 1]]
while mat[4][4] == 0:
	for i in range(len(o)):
		if mat[o[i][0]][o[i][1]] < m:
			Min = i
			mi = o[i][0]
			mj = o[i][1]
			m = mat[mi][mj]
	if mj > 0 and mat[mi][mj - 1] == 0:
		mat[mi][mj - 1] = mat[mi][mj] + matrix[mi][mj - 1]
		o.append([mi, mj - 1])
	if mj < 4 and mat[mi][mj + 1] == 0:
		mat[mi][mj + 1] = mat[mi][mj] + matrix[mi][mj + 1]
		o.append([mi, mj + 1])
	if mi > 0 and mat[mi - 1][mj] == 0:
		mat[mi - 1][mj] = mat[mi][mj] + matrix[mi - 1][mj]
		o.append([mi - 1, mj])
	if mi < 4 and mat[mi + 1][mj] == 0:
		mat[mi + 1][mj] = mat[mi][mj] + matrix[mi + 1][mj]
		o.append([mi + 1, mj])
	mat[mi][mj] = -1
	del o[Min]
	m = ma
print(mat[4][4])
