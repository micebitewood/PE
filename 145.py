import time

count = 0
t = time.clock()
for n in range(1000000, 1000000000):
	s = str(n)
	if s[-1] == '0':
		continue
	if int(s[0]) % 2 == int(s[-1]) % 2:
		continue
	r = ''
	for num in s[-1::-1]:
		r += num
	rev = int(r)
	Sum = str(rev + n)
	for c in Sum:
		if int(c) % 2 == 0:
			count -= 1
			break
	count += 1
print(count)
print(time.clock() - t)
