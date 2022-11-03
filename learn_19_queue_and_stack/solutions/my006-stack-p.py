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
    "date": "2022/10/19",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
} 

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

'''
    t
   -1
     []

    push(-2)
             t
        -1   0 
           [-2]

    push(0)
                t
        -1   0  1
           [-2, 0]

    push(-3)
                    t
        -1   0  1   2
           [-2, 0, -3]

    pop()
                t
        -1   0  1   2
           [-2, 0, -3]

    push(1)
                    t
        -1   0  1   2
           [-2, 0,  1]
'''
class Stack:

    def __init__(self):
        self.stack = []
        self.t = -1

    def dump(self):
        print(self.t, self.stack)

    def push(self, val: int) -> None:    
        self.t += 1	
        if self.t == len(self.stack):
            self.stack.append(val)
        else:
            self.stack[self.t] = val

    def pop(self) -> None:
        if self.t == -1:
            return

        self.t -= 1

    def top(self) -> int:
        if self.t == -1:
            return None 

        return self.stack[self.t]


