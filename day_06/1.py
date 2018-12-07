inputs = [list(map(int, x.split(', '))) for x in open('input.txt', 'r').read().split('\n')]
max_x = max(inputs, key=lambda x: x[0])[0]
max_y = max(inputs, key=lambda x: x[1])[1]
size = max([max_x, max_y])
grid = [[[-1, float('inf')] for x in range(size + 1)] for y in range(size + 1)]

for index, cord in enumerate(inputs):
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			dist = abs(cord[0] - col) + abs(cord[1] - row)
			if dist < grid[row][col][1]:
				grid[row][col] = [index, dist]
			elif dist == grid[row][col][1]:
				grid[row][col] = [-1, dist]

# Get all the ids on the edges AKA span infinitely 
top = grid[0]
top = [i[0] for i in top]
right = [(row[-1])[0] for row in grid]
bottom = [col[0] for col in grid[-1]]
left = [(row[0])[0] for row in grid]
infinite = set(top + right + bottom + left)

# truncate grid and remove any that span infinitly 
grid = [col[0] for row in grid for col in row if col[0] not in infinite]
# Get Sizes
counts = {}
for i in grid:
	if i in counts:
		counts[i] += 1
	else:
		counts[i] = 1

largest = max(counts, key=lambda x: counts[x])
print('Largest Id:', largest, '\tSize:', counts[largest])