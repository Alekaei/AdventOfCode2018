grid_serial_number = 2568
power_grid = [[[(((((x + 10) * y) + grid_serial_number) * (x + 10)) // 100 % 10) - 5, {i:0 for i in range(1, 301 - max([x, y]))} ] for x in range(1,301)] for y in range(1,301)]
max_power = -1000000000
pos = (0, 0)
size = 0
for y in range(300):
	print(f'Checking: {y}')
	for x in range(300):
		for s in power_grid[y][x][1]:
			# s = size
			total_power = 0
			if s > 1:
				total_power = power_grid[y][x][1][s - 1]
			for i in range(s - 1):
				total_power += power_grid[y + s - 1][x + i][0]
				total_power += power_grid[y + i][x + s - 1][0]
			total_power += power_grid[y + s - 1][x + s - 1][0]
			power_grid[y][x][1][s] = total_power

			if total_power > max_power:
				max_power = total_power
				size = s
				pos = (x + 1,y + 1)
print(pos, size, max_power)