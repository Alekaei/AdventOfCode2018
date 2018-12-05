inputs = [(lambda y: (int(y[0][1:]), list(map(int, y[2][:-1].split(','))), list(map(int, y[3].split('x')))))(x.split()) for x in open('input.txt').read().split('\n')]
rows = {}
for claim in inputs:
	start_x, start_y = claim[1][0], claim[1][1]
	end_x, end_y = start_x + claim[2][0], start_y + claim[2][1]
	for y in range(start_y, end_y):
		if y in rows:
			if len(rows[y]) < end_x:
				rows[y] += [0] * (end_x - len(rows[y]))
		else:
			rows[y] = [0] * end_x
		for x in range(start_x, end_x):
			rows[y][x] += 1

for claim in inputs:
	start_x, start_y = claim[1][0], claim[1][1]
	end_x, end_y = start_x + claim[2][0], start_y + claim[2][1]
	moreThenOne = False
	for y in range(start_y, end_y):
		for x in range(start_x, end_x):
			if rows[y][x] > 1:
				moreThenOne = True
				break
	if not moreThenOne:
		print(claim)
