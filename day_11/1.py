grid_serial_number = 2568
power_grid = [[ (((((x + 10) * y) + grid_serial_number) * (x + 10)) // 100 % 10) - 5 for x in range(1,301)] for y in range(1,301)]
max_power = -1000000000
pos = (0, 0)

for y in range(1,299):
	for x in range(1, 299):
		total_power = power_grid[y-1][x-1] + power_grid[y-1][x] + power_grid[y-1][x+1] + power_grid[y][x-1] + power_grid[y][x] + power_grid[y][x+1] + power_grid[y+1][x-1] + power_grid[y+1][x] + power_grid[y+1][x+1]
		if total_power > max_power:
			max_power = total_power
			pos = (x, y)
print(pos, max_power)