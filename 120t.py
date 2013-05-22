a = 10
s = a * a
for n in range(1, a):
	t = (a - 1) ** n + (a + 1) ** n
	r = t % s
	print(r)
