inputs = open('input.txt', 'r').read().split('\n')

for i in range(len(inputs)):
	for j in range(len(inputs)):
		if i == j:
			continue
		word1 = inputs[i]
		word2 = inputs[j]
		difference = [x for x in range(len(word1)) if word1[x] != word2[x]]
		if len(difference) == 1:
			index = difference[0]
			print(word1[:index] + word1[index + 1:])
			exit()