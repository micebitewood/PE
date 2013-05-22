import sys
sudoku = []
count = 0
t = []
Sum = 0
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def rec(sudoku, coordinate):
	sudoku1 = [sudoku[i][:] for i in range(9)]
	i = coordinate[0][0]
	j = coordinate[0][1]
	for n in num:
		if n not in sudoku[i]:
			line = [sudoku[k][j] for k in range(9)]
			if n not in line:
				a = i // 3 * 3
				b = j // 3 * 3
				sq = [sudoku[l][k] for l in range(a, a + 3) for k in range(b, b + 3)]
				if n not in sq:
					sudoku1[i][j] = n
					if len(coordinate) == 1:
						for i in range(3):
							print(sudoku1[0][i], end = '')
						print()
						return True
					if rec(sudoku1[:], coordinate[1:]):
						return True
	return False

def solve(sudoku):
	c = 0
	zeros = []
	for i in range(len(sudoku)):
		for j in range(len(sudoku[i])):
			if sudoku[i][j] == '0':
				zeros.append([i, j])
	rec(sudoku[:], zeros)

with open('96.txt', 'r') as f:
	for line in f:
		if count == 0:
			count += 1
			continue
		line = line[:-1]
		t.clear()
		for i in line:
			t.append(i)
		sudoku.append(t[:])
		count += 1
		count %= 10
		if count == 0:
			solve(sudoku)
			sudoku.clear()
