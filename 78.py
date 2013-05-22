import collections

n = 3
re = [[0], collections.deque([1]), collections.deque([1, 2])]
limit = 10
while True:
	re.append(collections.deque([re[n - 1].popleft()]))
	if n % 2 == 0:
		med = n // 2
	else:
		med = n // 2 + 1
	for i in range(2, med):
		re[n].append(re[n - i].popleft() + re[n][-1])
	for i in range(med, n):
		re[n].append(re[n - i][0] + re[n][-1])
	re[n].append(re[n][-1] + 1)
#	if n == 10:
#		print(re)
#		break
	if re[n][-1] > limit:
		print(re[n][-1], n)
		limit *= 10
	if re[n][-1] % 1000000 == 0:
		print(n)
		break
	n += 1
