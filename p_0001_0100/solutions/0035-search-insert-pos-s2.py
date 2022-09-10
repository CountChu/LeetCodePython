from typing import List
import pdb

solution_json = {
    "date": "2021/4/23",
    "coding": 5,
    "runtime": "52 ms",
    "memory": "15.1 MB"                    
}  

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	d = False
    	n = len(nums)

    	idx = -1
    	for i in range(n):
    		v = nums[i]
    		if d:
    			print(i, v, target)
    		if v >= target:
    			idx = i
    			break

    	if idx == -1:
    		idx = n

    	return idx