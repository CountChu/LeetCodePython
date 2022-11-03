from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/14",
    "design": 7,
    "coding": 20,
    "runtime": "144 ms",
    "memory": "20.4 MB"
}   

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numIslands(self, grid: List[List[str]]) -> int:
    	d = False
    	m = len(grid)
    	n = len(grid[0])
    	if d:
    		print('m = %d, n = %d' % (m, n))

    	out = 0
    	h = {}   # h[(i, j)] = label, label >= 1
    	for i in range(m):
    		for j in range(n):
    			if d:
    				print('(%d, %d)' % (i, j))

    			if (i, j) in h:
    				continue

    			if grid[i][j] != '1':
    				continue

    			if d:
    				print('        go')

    			out += 1
    			go(grid, m, n, i, j, h, out)

    	return out

def go(grid, m, n, i, j, h, num):
	d = False

	h[(i, j)] = num
	q = [(i, j)]
	while True:

		'''
		if count == 20:
			pdb.set_trace()
		'''

		if len(q) == 0:
			break

		if d:
			print(q)

		nd = q.pop(0)
		nd_i, nd_j = nd

		if nd_i <= m - 2:
			if grid[nd_i+1][nd_j] == '1':	# down
				next_nd = (nd_i+1, nd_j)
				if next_nd not in h:
					q.append(next_nd)
					h[next_nd] = num

		if nd_j <= n - 2:
			if grid[nd_i][nd_j+1] == '1': 	# right
				next_nd = (nd_i, nd_j+1)
				if next_nd not in h:
					q.append(next_nd)
					h[next_nd] = num

		if nd_i >= 1:
			if grid[nd_i-1][nd_j] == '1':	# top
				next_nd = (nd_i-1, nd_j)
				if next_nd not in h:
					q.append(next_nd)
					h[next_nd] = num

		if nd_j >= 1:
			if grid[nd_i][nd_j-1] == '1':	# left
				next_nd = (nd_i, nd_j-1)
				if next_nd not in h:
					q.append(next_nd)
					h[next_nd] = num
