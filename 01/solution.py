def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return np.array([int(d.strip()) for d in data])

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

import numpy as np

def part1():
	data = read_data()

	return sum( (data[1:] - data[:-1])>0 )


###



def part2():
	data = read_data()

	q = data[:-2]+data[1:-1]+data[2:]
	return sum( (q[1:] - q[:-1] )>0)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
