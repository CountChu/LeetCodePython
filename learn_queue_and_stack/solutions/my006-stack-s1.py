#
# Design a stack that supports push, pop, and top in constant time.
# 
# Implement the Stck class:
# 
#       Stck() initializes the stack object.
#       void push(int val) pushes the element val onto the stack.
#       void pop() removes the element on the top of the stack.
#       int top() gets the top element of the stack.
#
# You must implement a solution with O(1) time complexity for each function.
# 

from typing import List
import sys
import pdb

solution_json = {
    "date": "2022/9/3",
    "design": 0,
    "coding": 0,
    "runtime": "75 ms",
    "fasterThan": "77%",
    "memory": "17.9 MB" 
} 

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class Stack:

    def __init__(self):        
        self.s = []                     # stack
        self.t = -1                     # index of top. size = t + 1

    def __repr__(self):
        return '%d, %s' % (self.t, self.s)
       
    def push(self, val: int) -> None:
        self.t += 1
        if len(self.s) <= self.t:
            self.s.append(val)
        else:
            self.s[self.t] = val

    def pop(self) -> None:
        if self.t == -1: 
            return

        self.t -= 1

    def top(self) -> int:
        if self.t >= 0:
            return self.s[self.t]
        else: 
            return None
