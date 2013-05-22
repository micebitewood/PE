x = 1
y = 1
while y < 1000000000000:
	x, y = 3 * x + 2 * y - 2, 4 * x + 3 * y - 3
print(x)
