"""
All in one file since second is also calculated
"""

class Point:
	def __init__(self, pos, vel):
		self.pos = pos
		self.vel = vel
	
	def applyVelocity(self):
		self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

points = []

with open('input.txt', 'r') as inputFile:
	for line in inputFile.readlines():
		line = line.replace('velocity=<', '').replace('position=<', '').replace('>', '').replace(',', '').strip().split()
		x,y, vX,vY = int(line[0]), int(line[1]), int(line[2]), int(line[3])
		points.append(Point((x, y),(vX, vY)))


foundSmall = False
second = 0
size_x = 1000000000000
size_y = 1000000000000

mX = ()
mY = ()

lastWasSmaller = True
while not foundSmall:
	min_x,min_y,max_x,max_y = 10000000000000000, 10000000000000000, -10000000000000000, -10000000000000000
	for i in range(len(points)):
		points[i].applyVelocity()
		if points[i].pos[0] > max_x:
			max_x = points[i].pos[0]
		if points[i].pos[0] < min_x:
			min_x = points[i].pos[0]
		if points[i].pos[1] > max_y:
			max_y = points[i].pos[1]
		if points[i].pos[1] < min_y:
			min_y = points[i].pos[1]
	sX = max_x - min_x
	sY = max_y - min_y
	if size_x > sX and size_y > sY:
		size_x = sX
		size_y = sY
		mX = (min_x, max_x)
		mY = (min_y, max_y)
	else:
		foundSmall = True
	second += 1

mPrint = [[' ' for x in range(size_x + 1)] for y in range(size_y + 1)]
for point in points:
	point.pos = (point.pos[0] - point.vel[0], point.pos[1] - point.vel[1])
	x = point.pos[0] - mX[0]
	y = point.pos[1] - mY[0]
	mPrint[y][x] = '#'
print(f'Found on second {second - 1}\n')
[print("".join(line)) for line in mPrint]