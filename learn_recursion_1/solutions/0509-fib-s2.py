from typing import List
import pdb

#
# 2021/5/9: 3, 7, 36 ms, 15.6 MB
#

solution_json = {
    "date": "2021/5/9",
    "design": 3,
    "coding": 7,
    "runtime": "36 ms",
    "memory": "15.6 MB"
} 

class Solution:
    def fib(self, n: int) -> int:
    	f = {}
    	out = fib(n, f)
    	return out

def fib(n, f):
	d = False

	if n == 0:
		f[n] = 0
		return f[n]

	if n == 1:
		f[n] = 1
		return f[n]

	if n >= 2:

		out = 0

		if n-2 in f:
			out += f[n-2]
		else:
			out += fib(n-2, f)

		if n-1 in f:
			out += f[n-1]
		else:
			out += fib(n-1, f)

		f[n] = out

		return f[n]




