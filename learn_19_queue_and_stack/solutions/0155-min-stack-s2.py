#
# https://leetcode.com/problems/min-stack/
#
# Design a stack that supports push, pop, top, and retrieving the minimum element 
# in constant time.
# 
# Implement the MinStack class:
# 
#       MinStack() initializes the stack object.
#       void push(int val) pushes the element val onto the stack.
#       void pop() removes the element on the top of the stack.
#       int top() gets the top element of the stack.
#       int getMin() retrieves the minimum element in the stack.
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

class MinStack:

    def __init__(self):        
        self.s = []                     # stack
        self.t = -1                     # index of top. size = t + 1
        self.min = None                 # The min value of the stack.
        self.refresh_min = False        # Determine if refreshing min.

    def __repr__(self):
        if self.min == None:
            return '%d, None, %s, %s' % (self.t, self.refresh_min, self.s)
        else:
            return '%d, %d, %s, %s' % (self.t, self.min, self.refresh_min, self.s)
       
    def push(self, val: int) -> None:
        self.t += 1
        if len(self.s) <= self.t:
            self.s.append(val)
        else:
            self.s[self.t] = val

        if self.min == None:
            self.min = val 
        else:
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if self.t == -1: 
            return

        if self.s[self.t] == self.min:
            self.refresh_min = True 

        self.t -= 1

    def top(self) -> int:
        if self.t >= 0:
            return self.s[self.t]
        else: 
            return None

    def getMin(self) -> int:
        if not self.refresh_min:
            return self.min

        self.min = None 
        for i in range(self.t+1):
            if self.min == None:
                self.min = self.s[i]
            else:
                if self.s[i] < self.min:
                    self.min = self.s[i]

        self.refresh_min = False
        return self.min