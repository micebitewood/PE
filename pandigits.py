n0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for a in range(1, 10):
	n1 = n0[1:a] + n0[a + 1:]
	for b in range(8):
		n2 = n1[:b] + n1[b + 1:]
		for c in range(7):
			n3 = n2[:c] + n2[c + 1:]
			for d in range(6):
				n4 = n3[:d] + n3[d + 1:]
				for e in range(5):
					n5 = n4[:e] + n4[e + 1:]
					for f in range(4):
						n6 = n5[:f] + n5[f + 1:]
						for g in range(3):
							n7 = n6[:g] + n6[g + 1:]
							for h in range(2):
								n8 = n7[:h] + n7[h + 1:]
								for i in range(1):
									s = n0[a] + n1[b] + n2[c] + n3[d] + n4[e] + n5[f] + n6[g] + n7[h] + n8[i]
									print(s)
