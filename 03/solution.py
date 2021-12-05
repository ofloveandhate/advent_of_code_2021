def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

import collections

def part1():
	data = read_data()

	num_its = len(data[0])

	gamma, epsilon = '',''
	matches = data
	for ii in range(num_its):
		front_letters = [s[ii] for s in matches]
		c = collections.Counter(front_letters)
		
		if c['0'] == c['1']:
			m = '1'
			n = '0'
		else:
			m = c.most_common()[0][0]
			n = c.most_common()[1][0]

		gamma = gamma+m
		epsilon = epsilon+n


	return int(gamma,2)*int(epsilon,2)


###



def part2():
	data = read_data()

	num_its = len(data[0])



	matches = data
	for ii in range(num_its):
		if len(matches)==1:
			break

		current_letters = [s[ii] for s in matches]
		c = collections.Counter(current_letters)
		
		if c['0'] == c['1']:
			m = '1'
		else:
			m = c.most_common()[0][0]

		matches = [s for s in matches if s[ii]==m]

	generator = int(matches[0],2)


	matches = data
	for ii in range(num_its):
		if len(matches)==1:
			break

		
		current_letters = [s[ii] for s in matches]
		c = collections.Counter(current_letters)
		



		if c['0'] == c['1']:
			m = '0'
		else:
			m = c.most_common()[1][0]

		matches = [s for s in matches if s[ii]==m]

	scrubber = int(matches[0],2)


	return generator*scrubber

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
