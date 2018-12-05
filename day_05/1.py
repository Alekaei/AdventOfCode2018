polymer = open('input.txt', 'r').read().strip('\n')
possible = [l + l.upper() if i == 0 else l.upper()+l for l in 'abcdefghijklmnopqrstuvwxyz' for i in range(2)]
print(len(polymer))
clearPass = False

while not clearPass:
	old_pol = polymer
	for i in possible:
		polymer = polymer.replace(i, '')

	if old_pol == polymer:
		clearPass = True

print(len(polymer))