n = 1
s = 1
with open('pentagon', 'w') as f:
	while n < 100000:
		f.write(str(s) + '\n')
		s += n + n + n + 1
		n += 1
