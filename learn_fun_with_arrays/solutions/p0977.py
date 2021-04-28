from typing import List
import pdb

#
# 2021/4/25: 4 mins, 252 ms, 17.4 MB
#

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d = False
        n = len(nums)
        out = []
        for i in range(n):
        	v1 = nums[i]
        	v2 = v1 * v1
        	if d:
        		print(i, v1, v2)
        	out.append(v2)

        out.sort()	
        return out
