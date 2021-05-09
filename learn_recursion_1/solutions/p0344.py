from typing import List
import pdb

#
# 2021/5/9: 9, 12, 216 ms, 66.4 MB 
#

class Solution:
    def reverseString(self, s: List[str]) -> None:
    	reverseString(s, len(s), 0)

def reverseString(s, n, i):
	d = False

	last = s[n-1]
	if n >= 2:
		reverseString(s, n-1, i+1)	

	s[i] = last

	if d:
		print('s[%d] = %s' % (i, s[i]))