import sys
Max = 10
Min = [1]
for i in range(1, 100000):
	Cube = i ** 3
	if Cube >= Max:
		Min.append(i)
		Max *= 10
print(Min)
snum = []
s = []
nums = []
for i in range(1, len(Min)):
	j = Min[i - 1]
	snum.clear()
	nums.clear()
	while j < Min[i]:
		num = j ** 3
		nums.append(num)
		s.clear()
		for c in str(num):
			s.append(c)
		s.sort()
		snum.append(s[:])
		j += 1
	for j in range(len(snum)):
		if snum.count(snum[j]) == 5:
			print(nums[j])
			sys.exit()
