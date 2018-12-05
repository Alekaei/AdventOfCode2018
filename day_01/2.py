inputs = [int(x) for x in open('input.txt', 'r').read().split('\n')]
seen = set()
curr = 0
iters = 0
notFound = True
while notFound:
	for i in inputs:
		curr += i
		if curr in seen:
			print(curr)
			notFound = False
			break
		seen.add(curr)
	iters += 1
print (iters)