pList = []
pSet = set()
with open('prime1000000.txt', 'r') as f:
	nums = int(f.readline())
	for line in f:
		pList.append(str(int(line)))
		pSet.add(int(line))

def is_prime(n):
	for i in pList:
		i = int(i)
		if n // i < i:
			return True
		if n % i == 0:
			return False

def func(i1, i2):
	s = int(pList[i1] + pList[i2])
	if s not in pSet:
		if s > 1000000 and is_prime(s):
			return True
		else:
			return False
	return True

for i1 in range(1, nums):
	flag = [True for i in range(nums)]
	for i2 in range(i1 + 4, nums):
		if int(pList[i2]) > 10000:
			break
		if not func(i1, i2):
			flag[i2] = False
			continue
		if not func(i2, i1):
			flag[i2] = False
			continue
		for i3 in range(i1 + 1, i2):
			if int(pList[i1]) + int(pList[i2]) + 3 * int(pList[i3]) > 78103:
				break
			if flag[i3] == False:
				continue
			if not func(i1, i3):
				flag[i3] = False
				continue
			if not func(i3, i1):
				flag[i3] = False
				continue
			if not func(i2, i3):
				continue
			if not func(i3, i2):
				continue
			for i4 in range(i3 + 1, i2):
				if int(pList[i1]) + int(pList[i2]) + int(pList[i3]) + 2 * int(pList[i4]) > 78103:
					break
				if flag[i4] == False:
					continue
				if not func(i1, i4):
					flag[i4] = False
					continue
				if not func(i4, i1):
					flag[i4] = False
					continue
				if not func(i2, i4):
					continue
				if not func(i4, i2):
					continue
				if not func(i3, i4):
					continue
				if not func(i4, i3):
					continue
				for i5 in range(i4 + 1, i2):
					if flag[i5] == False:
						continue
					if not func(i1, i5):
						flag[i5] = False
						continue
					if not func(i5, i1):
						flag[i5] = False
						continue
					if not func(i2, i5):
						continue
					if not func(i5, i2):
						continue
					if not func(i3, i5):
						continue
					if not func(i5, i3):
						continue
					if not func(i4, i5):
						continue
					if not func(i5, i4):
						continue
					print(pList[i1], pList[i3], pList[i4], pList[i5], pList[i2])
					s = int(pList[i1]) + int(pList[i2]) + int(pList[i3]) + int(pList[i4]) + int(pList[i5])
					print(s)
