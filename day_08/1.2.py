"""
Both parts in same file because of the use of a class it made sense to keep it in one file
"""
license = [int(x) for x in open('input.txt', 'r').read().split()]

class Node:
	def __init__(self):
		self.children = []
		self.meta = []

	def getMetaSum(self):
		return sum(self.meta) + sum([child.getMetaSum() for child in self.children])
	
	def getValue(self):
		if len(self.children) == 0:
			return sum(self.meta)
		else:
			return sum([self.children[meta - 1].getValue() for meta in self.meta if meta > 0 and meta - 1 < len(self.children)])

def parse(license):
	noChildren, noMeta, *tail = license
	node = Node()

	for _ in range(noChildren):
		childNode, tail = parse(tail)
		node.children.append(childNode)	

	node.meta = tail[:noMeta]
	return node, tail[noMeta:]


root, _ = parse(license) 
print(root.getMetaSum())
print(root.getValue())