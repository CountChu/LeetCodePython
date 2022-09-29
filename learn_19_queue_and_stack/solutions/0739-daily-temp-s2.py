from typing import List
import pdb

solution_json = {
    "date": "2021/5/22",
    "design": 18,
    "coding": 16,
    "runtime": "640 ms",
    "memory": "22.1 MB"
}   

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    	d = False
    	v = temperatures
    	n = len(v)
    	ctx = {'out': []}
    	stack = []			# stack = [(idx, temp)]
    	for i in range(n):
    		handle(ctx, stack, i, v[i])
    		if d:
    			print('%d: %s' % (i, stack))
    	
    	for idx, temp in stack:
    		ctx['out'].append((idx, 0))

    	ctx['out'].sort(key = lambda x: x[0])
    	out = [x[1] for x in ctx['out']]

    	return out

def handle(ctx, stack, idx, temp):
	if stack == []:
		stack.append((idx, temp))
	else:
		while True:
			if len(stack) == 0:
				break
			if temp > stack[-1][1]:
				last_idx, last_temp = stack.pop()
				ctx['out'].append((last_idx, idx - last_idx))
			else:
				break
		stack.append((idx, temp))	




