#
# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue 
# (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#   void push(int x) Pushes element x to the back of the queue.
#   int pop() Removes the element from the front of the queue and returns it.
#   int peek() Returns the element at the front of the queue.
#   boolean empty() Returns true if the queue is empty, false otherwise.
#
# Notes:
#   You must use only standard operations of a stack, which means only push to top, 
#   peek/pop from top, size, and is empty operations are valid.
#
#   Depending on your language, the stack may not be supported natively. 
#   You may simulate a stack using a list or deque (double-ended queue) 
#   as long as you use only a stack's standard operations.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/28",
    "design": 0,
    "coding": 0,
    "runtime": "40 ms",
    "fasterThan": "79%",
    "memory": "14 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]


'''
    push(1)     [1]
    push(2)     [1, 2]
    pop()       [2],    1
'''
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return None
        
    def pop(self) -> int:
        
        my_stack = []
        while self.stack != []:
            my_stack.append(self.stack.pop())
        
        out = my_stack.pop()

        while my_stack != []:
            self.stack.append(my_stack.pop())

        return out
        
    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:   
        return self.stack == []
