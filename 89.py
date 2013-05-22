count = 0
total = 0
subpair = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
with open('89.txt', 'r') as f:
	for line in f:
		if line[-1] == '\n':
			line = line[:len(line) -1]
		total += len(line)
		num = 0
		for i in subpair:
			if i in line:
				line = line[:line.index(i)] + line[line.index(i) + 2:]
				num += subpair[i]
		for i in roman:
			num += line.count(i) * roman[i]
		count += num // 1000
		num %= 1000
		if num >= 900:
			count -= 1
		count += num // 500
		num %= 500
		if num >= 400:
			count += 2
		else:
			count += num // 100
		num %= 100
		if num >= 90:
			count -= 1
		count += num // 50
		num %= 50
		if num >= 40:
			count += 2
		else:
			count += num // 10
		num %= 10
		if num >= 9:
			count -= 1
		count += num // 5
		num %= 5
		if num == 4:
			count += 2
		else:
			count += num
print(total - count)
