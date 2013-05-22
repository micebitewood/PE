import decimal
import math
square = [n * n for n in range(1, 11)]
i = 0
count = 0
for n in range(1, 101):
	if n == square[i]:
		i += 1
		continue
	decimal.getcontext().prec = 102
	s = str(decimal.Decimal(n).sqrt())
	num = s[:s.find('.')] + s[s.find('.') + 1:-2]
	for c in num:
		count += int(c)
print(count)
