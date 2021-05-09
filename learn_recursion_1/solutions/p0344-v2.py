from typing import List
import pdb

#
# 2021/5/9: 2, 2, 204 ms, 41.7 MB
#

class Solution:
    def reverseString(self, s: List[str]) -> None:
    	n = len(s)
    	i = 0
    	j = n - 1
    	reverseString(s, i, j)

def reverseString(s, i, j):
	d = False
	if i >= j:
		return

	if d: 
		print(i, j)	
	s[i], s[j] = s[j], s[i]
	reverseString(s, i+1, j-1)
	
