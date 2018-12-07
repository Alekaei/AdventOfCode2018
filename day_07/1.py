inputs = [(x.split()[1], x.split()[7]) for x in open('input.txt', 'r').readlines()]

order = ''

while len(inputs) > 0:
	available = [i for i in inputs if i[0] not in [x[1] for x in inputs]]
	available.sort(key=lambda x: (x[0], x[1]))
	selected = available[0]
	if selected[0] not in order:
		order += selected[0]
	if len(inputs) == 1:
		order += selected[1]
	inputs = [x for x in inputs if x[0] not in order]
print(order)