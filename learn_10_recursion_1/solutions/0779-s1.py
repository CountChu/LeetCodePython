from typing import List
import pdb

solution_json = {
    "date": "2021/5/10",
    "design": 14,
    "coding": 9,
    "runtime": "40 ms",
    "memory": "15.7 MB"
}

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
    	d = False

    	idx = 0
    	for  i in range(n-1):
    		idx += 2**i
    	idx += k - 1

    	if d:
    		print('idx = %d' % idx)

    	path = []
    	while True:
    		if idx == 0:
    			break
    		idx, dir = parent(idx)
    		path.append((idx, dir))

    	if d:
    		print('path = %s' % path)

    	out = 0
    	for i in reversed(range(len(path))):
    		if d:
    			print(path[i])
    		idx, dir = path[i]
    		if dir == 'R':
    			if out == 0:
    				out = 1
    			elif out == 1:
    				out = 0
    			else:
    				assert False

    	#pdb.set_trace()
    	return out
    	
def parent(idx):
	if idx % 2 == 0:
		p_idx = (idx - 2) // 2    	
		return p_idx, 'R'
	else:
		p_idx = (idx - 1) // 2
		return p_idx, 'L'
