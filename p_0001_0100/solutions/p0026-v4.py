from typing import List
import pdb

#
# 11 mins, 10 mins, 88 ms, 17.3 MB
#

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

