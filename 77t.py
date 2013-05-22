n = 4
prime = [2, 3, 5, 7, 11, 13, 17, 19]

def func(n, re):
	for i in prime:
		if n > i:
			re1 = re[:]
			re1.append(i)
			func(n - i, re1[:])
		elif n == i:
			re.append(i)
			for j in range(1, len(re)):
				if re[j] < re[j - 1]:
					return
			print(re)
		else:
			return

for n in range(4, 20):
	re = []
	print(n)
	func(n, re)
