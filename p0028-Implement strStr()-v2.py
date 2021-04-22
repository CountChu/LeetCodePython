from typing import List
import pdb

#
# 2021/4/22: 7 mins. Time Limit Exceeded
#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	d = False

    	if needle == "":
    		return 0

    	n = len(haystack)
    	m = len(needle)
    	out = -1
    	for i in range(n):
    		c = haystack[i]

    		matched = True
    		for j in range(m):
    			if i + j >= n:
    				matched = False
    				break
    			if haystack[i + j] != needle[j]:
    				matched = False
    				break

    		if d:
    			print(i, c, matched)

    		if matched:
    			out = i
    			break

    	#pdb.set_trace()
    	return out
