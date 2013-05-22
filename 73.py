def HCF(n, d):
	while n > 1:
		n, d = d % n, n
	if n == 1:
		return True
	elif n == 0:
		return False
count = 0
for d in range(2, 12001):
	Min = d // 3 + 1
	Max = d // 2
	for n in range(Min, Max + 1):
		if HCF(n, d):
			if 1 / 3 < n / d < 1 / 2:
				count += 1
print(count)			
