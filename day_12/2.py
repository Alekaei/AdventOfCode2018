lines = [x.strip('\n') for x in open('input.txt', 'r').readlines()]

class Pot:
	__slots__ = ['next', 'prev', 'val', 'index']
	def __init__(self, val, nex, prev):
		self.val = val
		self.next = nex
		self.prev = prev
		self.index = self.prev.index + 1 if self.prev else -3 # -3 since pots start at index -3 and go to infinity

	def __str__(self):
		return self.printBehind()[:-1] + '[' + self.val + ']' + self.printAhead()[1:]

	def getState(self):
		s = ''
		if self.prev:
			if self.prev.prev:
				s += self.prev.prev.val
			else:
				s += '.'
			s += self.prev.val
		else:
			s += '..'
		s += self.val
		if self.next:
			s += self.next.val
			if self.next.next:
				s += self.next.next.val
			else:
				s+= '.'
		else:
			s += '..'
		
		return s

	def printAhead(self):
		s = ''
		cur = self
		while cur:
			s += cur.val
			cur = cur.next
		return s
	
	def printBehind(self):
		s = ''
		cur = self
		while cur:
			s += cur.val
			cur = cur.prev
		return s[::-1]

	def getRoot(self):
		cur = self
		while cur.prev:
			cur = cur.prev
		return cur
	
firstPot = Pot('.', None, None)
state = ['.', '.'] + [x for x in lines[0][15:]]
head = firstPot
for s in state:
	new_pot = Pot(s, None, head)
	head.next = new_pot
	head = new_pot

posibilities = {x.split()[0]:x.split()[2] for x in lines[2:]}
last_diff = 0
last_sum = 0
print(f'Gen  0: {firstPot.printAhead()}')
for gen in range(50000000000):
	prev = last_sum
	last_sum = 0
	new = Pot('.', None, None)
	curPot = firstPot
	while curPot:
		if not curPot.next and curPot.val + curPot.prev.val != '..':
			print('Fucking with shit')
			curPot.next = Pot('.', None, curPot)
		s = curPot.getState()
		if s in posibilities:
			new.val = posibilities[s]
		
		if new.val == '#':
			last_sum += new.index
		
		new.next = Pot('.', None, new)
		new = new.next
		curPot = curPot.next
	firstPot = new.getRoot()

	if last_diff == last_sum - prev: # growth becomes constant therefore we can stop simulating and instead do some math
		remaining_gens = 50000000000 - (gen + 1)
		last_sum += last_diff * remaining_gens  
		break
	last_diff = last_sum - 
	
print(last_sum)