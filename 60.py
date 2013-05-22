import sys
primelist = []
primeset = set()
with open('prime1000000.txt', 'r') as f:
	nums = int(f.readline())
	for line in f:
		primelist.append(str(int(line)))
		primeset.add(str(int(line)))
conprime = [[] for i in range(nums)]
prime = []
re = []
def is_prime(n):
	for i in primelist:
		i = int(i)
		if n // i < i:
			return True
		if n % i == 0:
			return False
for n in range(nums):
	for m in range(n):
		ss = primelist[n] + primelist[m]
		tt = primelist[m] + primelist[n]
		if (ss in primeset) and (tt in primeset) or (len(ss) > 6 and is_prime(int(ss)) and is_prime(int(tt))):
			conprime[m].append(primelist[n])
			if len(conprime[m]) >= 5:
				if int(primelist[m]) not in prime:
					prime.append(int(primelist[m]))
					prime.sort()
					if len(prime) >= 5:
						for i1 in prime:
							n1 = primelist.index(str(i1))
							m1 = prime.index(i1)
							if len(prime[m1:]) < 5:
								break
							for i2 in prime[m1 + 1:]:
								m2 = prime.index(i2)
								if len(prime[m2:]) < 4:
									break
								if str(i2) in conprime[n1]:
									n2 = primelist.index(str(i2))
									for i3 in prime[m2 + 1:]:
										m3 = prime.index(i3)
										if len(prime[m3:]) < 3:
											break
										if (str(i3) in conprime[n2]) and (str(i3) in conprime[n1]):
											n3 = primelist.index(str(i3))
											for i4 in prime[m3 + 1:]:
												m4 = prime.index(i4)
												if len(prime[m4:]) < 2:
													break
												if (str(i4) in conprime[n3]) and (str(i4) in conprime[n2]) and (str(i4) in conprime[n1]):
													n4 = primelist.index(str(i4))
													for i5 in prime[m4 + 1:]:
														m5 = prime.index(i5)
														if (str(i5) in conprime[n4]) and (str(i5) in conprime[n3]) and (str(i5) in conprime[n2]) and (str(i5) in conprime[n1]):
															print(i1, i2, i3, i4, i5)
															print(i1 + i2 + i3 + i4 + i5)
															sys.exit()
									
