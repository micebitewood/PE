import time

t = time.clock()
def relPrime(maxi, mini):
	while maxi % mini != 0:
		maxi, mini = mini, maxi % mini
	if mini == 1:
		return True
	return False

p = []
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		p.append(int(line))

ma = 0
n = 0
for i in range(1000, 10000):
	if i == p[n]:
		n += 1
	else:
		flag = [True for j in range(i)]
		for j in range(1, i):
			if not relPrime(i, j):
				k = j
				while k < i:
					flag[k] = False
					k += j
		ratio = i / (flag.count(True) - 1)
		if ratio > ma:
			ma_i = i
			ma = ratio
print(ma_i, ma)
print(time.clock() - t)
