import numpy as np

def read_data():
	with open ('input.txt') as f:
		data = f.readlines()
	return [d.strip() for d in data]

def write_data(data):
	with open('output.txt','w') as f:
		for d in data:
			f.write(str(d)+'\n')


def coords(line):
	a,b = line.split(' -> ')
	x1,y1 = [int(i) for i in a.split(',')]
	x2,y2 = [int(i) for i in b.split(',')]

	return (x1,y1),(x2,y2)
###

def part1():
	data = read_data()

	data = [coords(d) for d in data]

	start = np.array([d[0] for d in data])
	end = np.array([d[1] for d in data])


	n = np.max(np.hstack((np.max(start,axis=0),np.max(end,axis=0))))+1

	counts = np.zeros((n,n))
	
	h = start[:,0]==end[:,0]
	v = start[:,1]==end[:,1]

	start = np.vstack((start[h,:],start[v,:]))
	end = np.vstack((end[h,:],end[v,:]))

	assert(start.shape[0]==end.shape[0])

	for ii in range(start.shape[0]):
		x1,y1 = start[ii,:]
		x2,y2 = end[ii,:]

		if x2<x1:
			x1,x2 = x2,x1
		if y2<y1:
			y1,y2 = y2,y1

		counts[x1:(x2+1), y1:(y2+1)] = counts[x1:(x2+1), y1:(y2+1)]+1

	counts = np.transpose(counts)

	
	return np.sum(counts>1)


###



def part2():
	data = read_data()

	data = [coords(d) for d in data]

	start = np.array([d[0] for d in data])
	end = np.array([d[1] for d in data])


	n = np.max(np.hstack((np.max(start,axis=0),np.max(end,axis=0))))+1

	# create matrix to store data into
	counts = np.zeros((n,n))
	
	assert(start.shape[0]==end.shape[0])

	for ii in range(start.shape[0]):

		x1,y1 = start[ii,:]
		x2,y2 = end[ii,:]

		# I want the lower left and upper right.  lower left is origin in my mind.
		blx = min(x1, x2)
		bly = min(y1, y2)

		urx = max(x1+1, x2+1)
		ury = max(y1+1, y2+1)

		nx = urx-blx
		ny = ury-bly

		if (nx==1) or (ny==1):

			# straight line
			accumulate_me = np.ones((nx, ny))
		else:
			# diagonal line
			
			assert(nx==ny)
			n = nx

			if (blx==x1 and bly==y1) or (blx==x2 and bly==y2):
				accumulate_me = np.identity(n)
			else:
				accumulate_me = np.flipud(np.identity(n))


		counts[blx:urx, bly:ury] += accumulate_me

	return np.sum(counts>1)

print("part 1: {}".format(part1()))
print("part 2: {}".format(part2()))
