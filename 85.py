n = 1
d1 = 2
m = 2000
d2 = 4002000
Min = 2000
while m >= n:
	s = d2 * d1
	if s > 8000000:
		if s - 8000000 < Min:
			Min = s - 8000000
			MinArea = n * m
		while s > 8000000:
			d2 -= 2 * m
			m -= 1
			s = d2 * d1
	else:
		if 8000000 - s < Min:
			Min = 8000000 - s
			MinArea = n * m
		while s < 8000000:
			d1 += 2 * n + 2
			n += 1
			s = d2 * d1
print(MinArea, Min)
