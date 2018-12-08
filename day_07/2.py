inputs = [(x.split()[1], x.split()[7]) for x in open('input.txt', 'r').readlines()]

done = ''

time = 0

workers = [None, None, None, None, None]


while len(inputs) > 0 or any(workers):
	for i in range(len(workers)):
		if workers[i]:
			workers[i][1] -= 1
			if workers[i][1] == 0:
				done += workers[i][0]
				workers[i] = None 
				inputs = [x for x in inputs if x[0] not in done]
		else:	
			available = [i for i in inputs if i[0] not in [x[1] for x in inputs] and i[0] not in [x[0] for x in workers if x]]
			available.sort(key=lambda x: (x[0], x[1]))
			if len(available) > 0:
				workers[i] = [available[0][0], 61 + (ord(available[0][0]) - ord('A'))]

	time += 1
print(time)