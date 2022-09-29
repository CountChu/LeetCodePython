from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/15",
    "design": 0,
    "coding": 6,
    "runtime": "88 ms",
    "fasterThan": "62%",
    "memory": "17.8 MB"
}   

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class MinStack:

    def __init__(self):
    	self.min = None
    	self.s = []
    	self.d = False
       
    def push(self, val: int) -> None:    	
    	self.s.append(val)
    	if self.min == None:
    		self.min = val
    	elif self.min > val:
    		self.min = val

    	if self.d:
    		print('push: %s' % self.s)

    def pop(self) -> None:
    	val = self.s.pop()
    	if val > self.min:
    		return

    	self.min = None
    	for v in self.s:
    		if self.min == None:
    			self.min = v
    		elif self.min > v:
    			self.min = v

    def top(self) -> int:
    	n = len(self.s)
    	v = self.s[n-1]
    	return v

    def getMin(self) -> int:
    	return self.min
