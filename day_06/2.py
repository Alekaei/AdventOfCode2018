inputs = [list(map(int, x.split(', '))) for x in open('input.txt', 'r').read().split('\n')]

max_x = max(inputs, key=lambda x: x[0])[0]
max_y = max(inputs, key=lambda x: x[1])[1]
size = max([max_x, max_y])

cords = set()

for y in range(size):
	for x in range(size):
		if (x, y) in cords:
			continue
		fail = False
		distance_sum = 0
		
		for cord in inputs:
			dist = abs(cord[0] - x) + abs(cord[1] - y)
			if distance_sum + dist >= 10000:
				fail = True
				break
			else:
				distance_sum += dist

		if not fail:
			cords.add((x, y))

print(len(cords))