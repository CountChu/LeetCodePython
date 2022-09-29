from typing import List
import pdb

solution_json = {
    "date": "2021/4/24",
    "design": 6,
    "coding": 3,
    "runtime": "44 ms",
    "memory": "15.8 MB"
}    

class Solution:
    def climbStairs(self, n: int) -> int:
    	d = False

    	step = {}
    	for i in range(1, n+1):
    		if i == 1:
    			step[1] = 1
    		elif i == 2:
    			step[2] = 2
    		else:
    			step[i] = step[i-2] + step[i-1]

    		if d:
    			print(i, step[i])

    	#pdb.set_trace()
    	return step[n]