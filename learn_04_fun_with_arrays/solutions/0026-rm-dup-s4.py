from typing import List
import pdb

solution_json = {
    "date": "2021/4/28",
    "design": 11,
    "coding": 10,
    "runtime": "88 ms",
    "memory": "17.3 MB"
}     

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = False

        v = nums
        n = len(v)
        i = 0
        j = 1
        while True:

        	if j >= n:
        		break        	

        	if v[i] == v[j]:
        		j += 1

        	else:
        		if d:
        			print(i, j, v[i], v[j])
        		i += 1
        		v[i] = v[j]


        #pdb.set_trace()
        return i + 1

