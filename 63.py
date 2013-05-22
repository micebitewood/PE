n = 1
count = 0
while n < 10:
	d = 1
	m = n
	while m // d > 0:
		count += 1
		d *= 10
		m *= n
	n += 1
	print(count)
print(count)
