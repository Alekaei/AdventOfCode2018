inputs = [list(line.strip('\n')) for line in open('testcase_0.txt', 'r').readlines()]
class Unit:
	GOBLINS = 0
	ELFS = 0
	UNITS = []
	__slots__ = ['x', 'y', 'health', 'type']
	def __init__(self, pos, type):
		self.x = pos[0]
		self.y = pos[1]
		self.health = 200
		self.type = type
		if self.type == 'G':
			Unit.GOBLINS += 1
		else:
			Unit.ELFS += 1
		Unit.UNITS.append(self)

	def move(self):
		visited = {(self.x, self.y):[0, None]}
		check = [(self.x, self.y)]
		enemies = []
		while len(check) > 0 and len(enemies) == 0:
			checkPoint = check[0]
			up = (checkPoint[0], checkPoint[1] - 1)
			left = (checkPoint[0] - 1, checkPoint[1])
			right = (checkPoint[0] + 1, checkPoint[1])
			down = (checkPoint[0], checkPoint[1] + 1)
			for p in [x for x in [up, left, right, down] if inputs[x[1]][x[0]] in '.GE'.replace(self.type, '') and x not in visited.keys()]:
				check.append(p)
				visited[p] = [visited[checkPoint][0] + 1, checkPoint]
				if inputs[p[1]][p[0]] in 'GE':
					enemies.append(p)
			del check[0]
		
		if len(enemies) == 0:
			return 

		enemies.sort(key=lambda x: (visited[x][0], x[1], x[0]))
		enemy = enemies[0]
		move_to = enemy
		while visited[move_to][1] and visited[move_to][1] != (self.x, self.y):
			move_to = visited[move_to][1]
		if move_to != enemy:
			inputs[self.y][self.x] = '.'
			self.x, self.y = move_to[0], move_to[1]
			inputs[self.y][self.x] = self.type
	
	def attack(self):
		up = (self.x, self.y - 1)
		left = (self.x - 1, self.y)
		right = (self.x + 1, self.y)
		down = (self.x, self.y + 1)
		enemies = [[u for u in Unit.UNITS if (u.x, u.y) == x][0] for x in [up, down, left, right] if inputs[x[1]][x[0]] == 'GE'.replace(self.type, '')]
		if len(enemies) == 0:
			return False, 0
		enemies.sort(key=lambda enemy: (enemy.health, enemy.y, enemy.x))
		enemy = enemies[0]
		return enemy.damage()

	def damage(self):
		self.health -= 3
		if self.health <= 0:
			index = Unit.UNITS.index(self)
			Unit.UNITS.remove(self)
			if self.type == 'G':
				Unit.GOBLINS -= 1
			else:
				Unit.ELFS -= 1
			inputs[self.y][self.x] = '.'
			return True, index
		return False, 0

	def __str__(self):
		return ('Elf' if self.type == 'E' else 'Goblin') + f' with {self.health} HP at position ({self.x}, {self.y})'

for y, row in enumerate(inputs):
	for x, tile in enumerate(row):
		if tile in 'GE':
			Unit((x, y), tile)

rnd = 0

while Unit.ELFS > 0 and Unit.GOBLINS > 0:
	Unit.UNITS.sort(key=lambda unit: (unit.y, unit.x))
	index = 0
	while index < len(Unit.UNITS):
		Unit.UNITS[index].move()
		killed, pIndex = Unit.UNITS[index].attack()
		if killed and pIndex < index:
			index -= 1
		index += 1
	rnd += 1
rnd -= 1
[print("".join(x)) for x in inputs]
print(list(map(str, Unit.UNITS)))
print('Finished on round', rnd)
print(f'{"Elves" if Unit.ELFS > 0 else "Goblins"} won with a total health of {sum([unit.health for unit in Unit.UNITS])}')
print(f'The score is {rnd * sum([unit.health for unit in Unit.UNITS])}')