square = [n * n for n in range(2, 35)]
a = 0
re = []
Max = 9
for D in range(2, 1001):
	if D == square[a]:
		a += 1
		continue
	re.clear()
	x = int(D ** 0.5)
	re.append(x)
	y = 1
	i = 1
	k = -x
	while x * x - D * y * y != 1:
		i = (D - k * k) // i
		j = int(D ** 0.5 - k) // i
		re.append(j)
		k = -k - j * i
		denominator = 1
		numerator = re[-1]
		for n in re[-2::-1]:
			numerator, denominator = denominator + n * numerator, numerator
		x, y = numerator, denominator
	if x > Max:
		Max = x
		MaD = D
print(MaD)
