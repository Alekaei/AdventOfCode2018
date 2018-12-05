inputs = open('input.txt', 'r').read().split('\n')
twos = 0
threes = 0
for i in inputs:
	occurs = {}
	for letter in i:
		if letter in occurs:
			occurs[letter] += 1
		else:
			occurs[letter] = 1
	if 2 in occurs.values():
		twos += 1
	if 3 in occurs.values():
		threes += 1
print(twos * threes)