from typing import List
import pdb

#
# 2021/5/9: 0, 7, 976 ms, 15.7 MB
#

class Solution:
    def fib(self, n: int) -> int:
    	out = fib(n)
    	return out

def fib(n):
	d = False

	if n == 0:
		return 0

	if n == 1:
		return 1

	if n >= 2:
		return fib(n-2) + fib(n-1)




