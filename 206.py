import sys
a = 1929394959697989990
while True:
	d = int(a ** 0.5)
	if d ** 2 == a:
		print(d)
		sys.exit()
	for n in range(-2, -20, -2):
		if str(a)[n] != '0':
			s = 10 ** (-n-1)
			t = s // 100 * 9
			a -= s
			while t >= 90:
				a += t
				t //= 100
			break
		elif n == -18:
			sys.exit()
