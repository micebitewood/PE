numerator = 1
denominator = 2
count = 0
for i in range(1000):
	if len(str(numerator + denominator)) > len(str(denominator)):
		count += 1
	numerator, denominator = denominator, numerator + 2 * denominator
print(count)
