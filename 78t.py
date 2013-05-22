result = []
def func(n, re):
	if n == 0:
		re.sort()
		if re not in result:
			result.append(re)
	else:
		for m in range(1, n + 1):
			re1 = re[:]
			re1.append(m)
			func(n - m, re1)
n = 20
re = []
for m in range(1, n + 1):
	re1 = re[:]
	re1.append(m)
	func(n - m, re1)
print(len(result))
