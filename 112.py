import sys
def isBouncy(s):
	b = []
	for c in s:
		b.append(c)
	c = b[:]
	b.sort()
	r = b[-1::-1]
	if c == b or c == r:
		return False
	return True
n = 21781
bouncy = 19602
while True:
	if isBouncy(str(n)):
		bouncy += 1
	if bouncy * 100 / n >= 99:
		print(bouncy, n)
		sys.exit()
	n += 1
