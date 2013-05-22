prime = []
MAX = 100001
with open('prime1000000.txt', 'r') as f:
	f.readline()
	for line in f:
		if len(line) > 6:
			break
		prime.append(int(line))

def gen(mult):
	total = mult[0]
	re = []
	if len(mult[1]) == 1:
		while total < MAX:
			re.append(total)
			total *= mult[1][0]
	else:
		while total < MAX:
			temp = [total, mult[1][:-1]]
			t = gen(temp)
			for n in t:
				re.append(n)
			total *= mult[1][-1]
	return re

mult = []
i = 0
j = 0
t = []
re = set()
count = 1
total = []
while True:
	if i > 1 and prime[i] > mult[j][0]:
			total = gen(mult[j])
			j += 1
	else:
		t.clear()
		total.clear()
		n = prime[i]
		while n < MAX:
			total.append(n)
			n *= prime[i]
		for m in mult:
			t.append(m[1][:])
		for m in t:
			m.append(prime[i])
		for m in prime[:i]:
			t.append([m, prime[i]])
		for m in t:
			mult0 = 1
			for n in m:
				mult0 *= n
			if mult0 > 2000:
				continue
			tp = [mult0, m[:]]
			mult.append(tp)
		mult.sort()
		i += 1
	for n in total:
		re.add(n)
		count += 1
	if count >= 10000:
		total.sort()
		print(count, total[10000 - count - 1])
		break
