import datetime
inputs = [x for x in open('input.txt', 'r').read().split('\n')]
inputs.sort(key=lambda x: x[1:17])
shifts = {}
currentGuard = None
lastminute = 0
for line in inputs:
	splits = line.split()
	if splits[2] == 'Guard':
		currentGuard = splits[3][1:]
	elif currentGuard:
		minute, isAsleep = int(splits[1].split(':')[1][:-1]), True if splits[2] == 'falls' else False
		if currentGuard in shifts:
			if isAsleep:
				lastminute = minute
			else:
				for i in range(lastminute, minute):
					if i in shifts[currentGuard]:
						shifts[currentGuard][i] += 1
					else:
						shifts[currentGuard][i] = 1
		else:
			shifts[currentGuard] = {}
			lastminute = minute

shifts = [[int(x), sum(shifts[x].values()), sorted([[y, shifts[x][y]] for y in shifts[x]], key=lambda d: d[1])[-1][0]] for x in shifts]
shifts.sort(key=lambda x: x[1])
print(shifts[-1][0] * shifts[-1][2])