count = 0
MAX = 51
for x1 in range(MAX):
	for y1 in range(MAX):
		if x1 + y1 == 0:
			continue
		s1 = x1 * x1 + y1 * y1
		for x2 in range(MAX):
			for y2 in range(MAX):
				if x2 + y2 == 0:
					continue
				if x1 == x2 and y1 == y2:
					continue
				s = x1 * x2 + y1 * y2
				if s == 0:
					count += 1
				elif s - s1 == 0:
					count += 1
				elif s - x2 * x2 - y2 * y2 == 0:
					count += 1
print(count)
