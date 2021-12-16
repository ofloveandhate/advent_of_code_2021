import numpy as np
# import pandas as pd

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [int(d.strip()) for d in data[0].split(',')]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')



###

from collections import Counter, defaultdict

def part1():
	return solution(80)

def part2():
	return solution(256)



def solution(days):

	ages = read_data()
	ages.sort()

	data = defaultdict(int,Counter(ages))

	fish = np.zeros((9))
	for ii in range(9):
		fish[ii] = data[ii]


	nums = np.zeros((days))
	for ii in range(days):
		

		n = fish[0]

		fish = np.roll(fish,-1)

		fish[8] = n
		fish[6] += n

		nums[ii] = sum(fish)
		

	print(nums[17])
	print(nums[79])


	return nums[-1]


###



print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
