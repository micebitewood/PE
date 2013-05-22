a = [2]
for i in range(1, 100):
	if i % 3 == 2:
		a.append((i + 1) * 2 // 3)
	else:
		a.append(1)
numerator = 1
denominator = 0
for i in a[-1::-1]:
	numerator, denominator = i * numerator + denominator, numerator
Sum = 0
for i in str(numerator):
	Sum += int(i)
print(Sum)
