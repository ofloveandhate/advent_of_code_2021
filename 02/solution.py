def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()

	position, depth = 0,0

	for ii in range(len(data)):
		d = data[ii]
		direction,x = d.split()
		x = int(x)

		if direction=='forward':
			position += x
		elif direction=='up':
			depth += x
		elif direction=='down':
			depth -= x
			
	return position*depth, position, depth


###



def part2():
	data = read_data()
	
	position, depth, aim = 0,0,0

	for ii in range(len(data)):
		d = data[ii]
		direction,x = d.split()
		x = int(x)

		if direction=='forward':
			position += x
			depth += aim*x

		elif direction=='up':
			aim -= x

		elif direction=='down':
			aim += x
		
	return position*depth, position, depth

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
