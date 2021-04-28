from typing import List
import pdb

#
# 2021/4/25: 3 mins, 7 mins, 1584 ms, 16.4 MB
#

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
    	d = False

    	n = len(arr)
    	i = 0
    	while True:
    		v = arr[i]
    		if v == 0:
    			for j in range(n-1, i, -1):
    				if j == i + 1:
    					arr[j] = 0
    				else:
    					arr[j] = arr[j-1]
    			i += 2
    		else:
    			i += 1
    					
    		if d:
    			print(i, v, arr)

    		if i >= n:
    			break

    	#pdb.set_trace()
