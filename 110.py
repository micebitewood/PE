re = []
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
def gen(total, fac):
	for n in range(3, 20, 2):
		t = total / n
		fac1 = fac[:]
		fac1.append(n)
		if t > 1:
			gen(t, fac1)
		else:
			fac1.sort()
			fac1.reverse()
			s = 1
			for i in range(len(fac1)):
				s *= prime[i] ** (fac1[i] // 2)
			re.append(s)
			break
gen(7999999, [])
re.sort()
print(re[0])
