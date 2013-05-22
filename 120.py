Sum = 0
for a in range(3, 1001):
	s = a * a
	r = s - a
	if s % 2 == 0:
		r = r - a
	Sum += r
print(Sum, a)
