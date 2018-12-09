playerCount, lastMarble = (lambda x: [int(x[0]), int(x[6])])(open('input.txt', 'r').read().split(' '))

marbles = [0]

players = {i:0 for i in range(playerCount)}
lastMarblePlaced = 0
currPlayer = 0
currIndex = 0
while lastMarblePlaced < lastMarble:
	placeMarble = lastMarblePlaced + 1
	if placeMarble % 23 == 0:
		index = (currIndex - 7) % len(marbles)
		players[currPlayer] += placeMarble + marbles[index]
		marbles = marbles[:index] + marbles[index+1:]
	else:
		index = (currIndex + 2) % len(marbles)
		marbles = marbles[:index] + [placeMarble] + marbles[index:]
	currIndex = index
	lastMarblePlaced += 1
	currPlayer = (currPlayer + 1) % playerCount

print(max(players.values()))