def rep(i, n):
	while i > 1:
		i, n = n % i, i
	if i == 1:
		return True
	return False

n = 210
count = 0
for i in range(210):
	if rep(i, n):
		print(i, end = ' ')
		count += 1
