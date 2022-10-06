from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/9",
    "design": 0,
    "coding": 7,
    "runtime": "956 ms",
    "fasterThan": "23%",    
    "memory": "13.8 MB"
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def fib(self, n: int) -> int:
    	out = f(n)
    	return out

def f(n):
	if n == 0:
		return 0

	if n == 1:
		return 1

	if n >= 2:
		return f(n-2) + f(n-1)




