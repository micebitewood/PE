P = []
pc = []
i = 45
s = 1035
P3 = []
while s < 10000:
	P3.append(s)
	i += 1
	s += i
P.append(P3)
pc.append(45)
i = 32
s = i ** 2
P4 = []
while s < 10000:
	P4.append(s)
	s += i
	i += 1
	s += i
P.append(P4)
pc.append(32)
i = 26
s = 1001
P5 = []
while s < 10000:
	P5.append(s)
	s += i + i
	i += 1
	s += i
P.append(P5)
pc.append(26)
i = 23
s = 1035
P6 = []
while s < 10000:
	P6.append(s)
	s += i + i + i
	i += 1
	s += i
P.append(P6)
pc.append(23)
i = 21
s = 1071
P7 = []
while s < 10000:
	P7.append(s)
	s += 4 * i
	i += 1
	s += i
P.append(P7)
pc.append(21)
i = 19
s = 1045
P8 = []
while s < 10000:
	P8.append(s)
	s += 5 * i
	i += 1
	s += i
P.append(P8)
pc.append(19)
i1 = 5
for n1 in P[5]:
	r1 = n1 % 100
	for i2 in range(5):
		for n2 in P[i2]:
			if n2 // 100 == r1:
				r2 = n2 % 100
				for i3 in range(5):
					if i3 != i2:
						for n3 in P[i3]:
							if n3 // 100 == r2:
								r3 = n3 % 100
								for i4 in range(5):
									if i4 != i3 and i4 != i2:
										for n4 in P[i4]:
											if n4 // 100 == r3:
												r4 = n4 % 100
												for i5 in range(5):
													if i5 != i3 and i5 != i2 and i5 != i4:
														for n5 in P[i5]:
															if n5 // 100 == r4:
																r5 = n5 % 100
																for i6 in range(5):
																	if i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2:
																		for n6 in P[i6]:
																			if n6 // 100 == r5:
																				r6 = n6 % 100
																				if n1 // 100 == r6:
																					print(P[i1].index(n1) + pc[i1], P[i2].index(n2) + pc[i2], P[i3].index(n3) + pc[i3], P[i4].index(n4) + pc[i4], P[i5].index(n5) + pc[i5], P[i6].index(n6) + pc[i6])
																					print(n1, n2, n3, n4, n5, n6)
																					print(n1 + n2 + n3 + n4 + n5 + n6)
																					print(i1, i2, i3, i4, i5, i6)
															elif n5 // 100 > r4:
																break
											elif n4 // 100 > r3:
												break
							elif n3 // 100 > r2:
								break
			elif n2 // 100 > r1:
				break
	
'''
for i1 in range(len(P))
for i3 in range(len(a)):
	r3 = a[i3] % 100
	for i4 in range(len(b)):
		if b[i4] // 100 == r3:
			r4 = b[i4] % 100
			for i5 in range(len(c)):
				if c[i5] // 100 == r4:
					r5 = c[i5] % 100
					for i6 in range(len(d)):
						if d[i6] // 100 == r5:
							r6 = d[i6] % 100
							for i7 in range(len(e)):
								if e[i7] // 100 == r6:
									r7 = e[i7] % 100
									for i8 in range(len(f)):
										if f[i8] // 100 == r7:
											r8 = f[i8] % 100
											if a[i3] // 100 == r8:
												print(i3, i4, i5, i6, i7, i8)
												print(a[i3], b[i4], c[i5], d[i6], e[i7], f[i8])
												print(a[i3] + b[i4] + c[i5] + d[i6] + e[i7] + f[i8])
										elif f[i8] // 100 > r7:
											break
								elif e[i7] // 100 > r6:
									break
						elif d[i6] // 100 > r5:
							break
				elif c[i5] // 100 > r4:
					break
		elif b[i4] // 100 > r3:
			break
'''
