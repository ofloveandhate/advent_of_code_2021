import numpy as np

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
		data = [d.strip() for d in data]
	data = [d for d in data if d!=""]
	return data

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

def draw_numbers(data):
	q = data.pop(0)
	return np.array([int(d) for d in q.split(',')])

def board(data):
	q = [data.pop(0) for ii in range(5)]
	q = [ [int(d) for d in a.split()] for a in q ]
	return np.array(q)

def mark_number(b,n):
	b[b==n] = 0
	return b

def is_winner(b):
	return np.any(np.sum(b, axis=0)==0) \
		or np.any(np.sum(b, axis=1)==0) 
		# diagonals don't count


def score(b,n):
	s = np.sum(np.reshape(b,(1,25)))

	print(s,n)
	return s*n

###

def part1():
	data = read_data()

	numbers = draw_numbers(data)

	boards = [board(data) for ii in range(len(data)//5)]

	for ii in range(len(numbers)):
		n = numbers[ii]
		
		[mark_number(b,n) for b in boards]

		for b in boards:
			if (is_winner(b)):
				print(b)
				return score(b,n)

###



def part2():
	data = read_data()
	thing = []
	for a in thing:
		pass

	return

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
