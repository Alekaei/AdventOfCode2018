polymer = open('input.txt', 'r').read().strip('\n')
possible = [l + l.upper() if i == 0 else l.upper()+l for l in 'abcdefghijklmnopqrstuvwxyz' for i in range(2)]

polyLengths = {}
for l in 'abcdefghijklmnopqrstuvwxyz':
	polyLengths[l] = polymer.replace(l, '').replace(l.upper(), '')
	clearPass = False
	while not clearPass:
		old_pol = polyLengths[l]
		for i in possible:
			polyLengths[l] = polyLengths[l].replace(i, '')

		if old_pol == polyLengths[l]:
			clearPass = True
	polyLengths[l] = len(polyLengths[l])

print(min(polyLengths.values()))