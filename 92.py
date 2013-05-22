import time
num = dict([c, c**2] for c in range(10))

def square(n):
	m = n
	re = 0
	while m > 0:
		t = num[m % 10]
		re += t
		m = m // 10
	return re

t0=time.clock()
chain = []
flag = [0 for i in range(1, 1001)]
flag[1] = 1
flag[89] = 2
for i in range(1, 1000):
	j = i
	while flag[j] == 0:
		chain.append(j)
		j = square(j)
	if flag[j] == 1:
		while len(chain) > 0:
			flag[chain.pop()] = 1
	elif flag[j] == 2:
		while len(chain) > 0:
			flag[chain.pop()] = 2
count = flag.count(2)
print(count)
for i in range(1000, 10000000):
	j = square(i)
	if flag[j] == 2:
		count += 1
print(count)
print(time.clock()-t0)
