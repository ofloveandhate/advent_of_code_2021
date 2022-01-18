import numpy as np
import pandas as pd

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()[0]
	return np.array([int(d.strip()) for d in data.split(',')])

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')

###

def part1():
	data = read_data()

	return int(np.min([np.sum(np.abs(data - ii)) for ii in range(np.min(data),np.max(data)+1)]))
	


###



def part2():
	data = read_data()

	m = np.min(data)
	M = np.max(data) 

	fuel_costs = [np.abs(data - ii) for ii in range(m,M+1)]

	modded_fuel = [np.sum((f*(f+1))/2) for f in fuel_costs]

	# print(modded_fuel)
	return int(np.min(modded_fuel))


print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
