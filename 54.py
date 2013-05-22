'''H-Heart, D-Diamond, S-Spade, C-Club'''
def firstWin(nums, types):
	nums[0].sort()
	nums[1].sort()
	v = [0, 0]
	s = [[], []]
	for i in range(2):
		j = 0
		while j < 5:
			if nums[i].count(nums[i][j]) == 2:
				v[i] += 1
				s[i].append(100+nums[i][j])
				j += 2
			elif nums[i].count(nums[i][j]) == 3:
				v[i] += 3
				s[i].append(200+nums[i][j])
				j += 3
			elif nums[i].count(nums[i][j]) == 4:
				v[i] += 7
				s[i].append(300+nums[i][j])
				j += 4
			else:
				s[i].append(nums[i][j])
				j += 1
		if v[i] == 4:
			v[i] = 6
		if v[i] == 0:
			if types[i].count(types[i][0]) == 5:
				v[i] = 5
			if nums[i][0] + 1 == nums[i][1] and nums[i][1] + 1 == nums[i][2] and nums[i][2] + 1 == nums[i][3] and nums[i][3] + 1 == nums[i][4]:
				v[i] += 4
	if v[0] > v[1]:		
		return 1
	elif v[0] < v[1]:
		return 0
	else:
		va = v[0]
		if va == 9 or va == 4:
			if nums[0][4] > nums[1][4]:
				return 1
			else:
				return 0
		else:
			s[0].sort()
			s[1].sort()
			if s[0][-1:] > s[1][-1:]:
				return 1
			else:
				return 0

w = 0
with open('54.txt', 'r') as f:
	for line in f:
		hands = line.split()
		nums = []
		types = []
		for s in hands:
			types.append(s[1])
			if s[0] > '1' and s[0] <= '9':
				nums.append(int(s[0]))
			elif s[0] == 'T':
				nums.append(10)
			elif s[0] == 'J':
				nums.append(11)
			elif s[0] == 'Q':
				nums.append(12)
			elif s[0] == 'K':
				nums.append(13)
			elif s[0] == 'A':
				nums.append(14)
		n = [nums[0:5], nums[5:10]]
		t = [types[0:5], types[5:10]]
		w += firstWin(n, t)
print(w)
