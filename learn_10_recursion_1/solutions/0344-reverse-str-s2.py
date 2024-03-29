from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/9",
    "design": 2,
    "coding": 2,
    "runtime": "204 ms",
    "memory": "41.7 MB"
}      

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

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
	
