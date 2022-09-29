from typing import List
import pdb

solution_json = {
    "date": "2021/4/29",
    "design": 0,
    "coding": 7,
    "runtime": "48 ms",
    "memory": "15.4 MB"     
}

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    	d = False
    	v = nums
    	n = len(v)

    	hash = {}
    	for i in range(n):
    		if v[i] not in hash:
    			hash[v[i]] = True

    	ls = [*hash.keys()]
    	ls.sort(reverse=True)
    	if d:
    		print(ls)

    	n = len(ls)
    	if n >= 3:
    		out = ls[2]
    	elif n in [1, 2]:
    		out = ls[0]
    	else:
    		out = None

    	return out

