lines = [x.strip('\n') for x in open('input.txt', 'r').readlines()]

state = ['.', '.', '.'] + [x for x in lines[0][15:]]
posibilities = {x.split()[0]:x.split()[2] for x in lines[2:]}

last_sum = 0
print(f'Gen  0: {"".join(state)}')
for gen in range(20):
	last_sum = 0
	new_state = ['.' for i in range(len(state))]
	for i in range(0, len(state)):
		if len(state) - i - 1 < 2:
			for g in range(len(state) - i):
				state.append('.')
				new_state.append('.')
		s = "".join(state[i-2:i+3])
		if s in posibilities:
			new_state[i] = posibilities[s]
		else:
			new_state[i] = '.'
		if new_state[i] == '#':
			last_sum += i - 3
	state = new_state
	print(f'Gen {gen + 1:>2}: {"".join(state)}')
print(last_sum)