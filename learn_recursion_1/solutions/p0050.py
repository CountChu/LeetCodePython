from typing import List
import pdb

#
# 2021/5/9: 6, 12, 44 ms, 15.6 MB
#

class Solution:
    def myPow(self, x: float, n: int) -> float:
    	if n == 0:
    		return 1

    	h = {}
    	if n >= 0:
    		out = pow(x, n, h)
    	else:
    		n = -n
    		out = pow(x, n, h)
    		out = 1/out
    	return out

def pow(x, n, h):
	if n == 1:
		h[n] = x
		return h[n]

	if n >= 2:
		if n % 2 == 0:
			if n//2 not in h:
				h[n//2] = pow(x, n//2, h)
			h[n] = h[n//2] * h[n//2]

		else:
			if n//2 not in h:
				h[n//2] = pow(x, n//2, h)
			if 1 not in h:
				h[1] = pow(x, 1, h)
			h[n] = h[n//2] * h[n//2] * h[1]

		return h[n]

