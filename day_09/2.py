playerCount, lastMarble = (lambda x: [int(x[0]), int(x[6]) * 100])(open('input.txt', 'r').read().split(' '))

"""
Original DoubleList from : http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
"""

class Node(object):
	
	def __init__(self, data, prev, next):
		self.data = data
		self.prev = prev
		self.next = next
	
	def getSevenBehind(self):
		return self.prev.prev.prev.prev.prev.prev.prev
	
	def remove(self):
		self.prev.next = self.next
		self.next.prev = self.prev

class DoubleList(object):
 
	head = None
	tail = None
 
	def append(self, data):
		new_node = Node(data, None, None)
		if self.head is None:
			self.head = self.tail = new_node
			new_node.prev = new_node.next = new_node
		else:
			new_node.prev = self.tail
			new_node.next = self.head
			self.tail.next = new_node
			self.tail = new_node
		
	def getList(self):
		vals = [self.head.data]
		current = self.head.next
		while current != self.head:
			vals.append(current.data)
			current = current.next
		return vals

marbles = DoubleList()
marbles.append(0)
players = {i:0 for i in range(playerCount)}
currMarble = marbles.head

currPlayer = 0

for i in range(1, lastMarble + 1):
	if i % 23 == 0:
		removeMarble = currMarble.getSevenBehind()
		players[currPlayer] += i + removeMarble.data
		currMarble = removeMarble.next
		removeMarble.remove()
	else:
		insertAfter = currMarble.next
		new_marble = Node(i, insertAfter, insertAfter.next)
		if insertAfter.next:
			insertAfter.next.prev = new_marble
		insertAfter.next = new_marble
		currMarble = new_marble
	
	currPlayer = (currPlayer + 1) % playerCount

print(max(players.values()))