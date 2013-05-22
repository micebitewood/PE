import decimal

D = [1, 2, 3, 4, 5, 6]
counta = [0 for i in range(37)]
for a in D:
	for b in D:
		for c in D:
			for d in D:
				for e in D:
					for f in D:
						counta[a + b + c + d + e + f] += 1
D = [1, 2, 3, 4]
countb = [0 for i in range(37)]
for a in D:
	for b in D:
		for c in D:
			for d in D:
				for e in D:
					for f in D:
						for g in D:
							for h in D:
								for i in D:
									countb[a + b + c + d + e + f + g + h + i] += 1
maxa = 6 ** 6
maxb = 4 ** 9
ans = 0
for i in range(36, 1, -1):
	ans += countb[i] * sum(counta[:i])
decimal.getcontext().prec = 8
print(decimal.Decimal(ans) / decimal.Decimal(maxa * maxb))
