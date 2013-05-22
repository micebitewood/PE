n = 180180
while True:
	s = n * n
	count = 2
	for i in range(2, n):
		if s % i == 0:
			count += 1
	if count > 1000:
		print(n)
		break
#	print(count)
#	break
	n += 1
