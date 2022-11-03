#
# https://leetcode.com/problems/design-circular-queue/
#
# Design your implementation of the circular queue. 
# The circular queue is a linear data structure in which the operations 
# are performed based on FIFO (First In First Out) principle 
# and the last position is connected back to the first position 
# to make a circle. It is also called "Ring Buffer".
#

from typing import List
import sys
import pdb

solution_json = {
    "date": "2022/9/3",
    "design": 0,
    "coding": 0,
    "runtime": "77 ms",
    "fasterThan": "85%",
    "memory": "14.5 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

#
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
#


"""
      0   1   2 
    [-1, -1, -1]
      h
      t

    enQueue(1)
    [1, -1, -1]
     h
     t

    enQueue(2)
    [1, 2, -1]
     h
        t

    enQueue(3)
    [1, 2, 3]
     h
           t

    deQueue()
    [-1, 2, 3]
         h
            t

    enQueue()
    [4, 2, 3]
        h
     t
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.s = len(self.q)
        self.h = 0
        self.t = 0

    def dump(self):
        print('h: %d, t: %d, q: %s' % (self.h, self.t, self.q))

    def next(self, idx):
        return (idx + 1) % self.s
        
    def enQueue(self, value: int) -> bool:
        assert value >= 0

        if self.isFull():
            return False

        if self.Front() == -1:
            assert self.h == self.t 
            self.q[self.h] = value 
        else:
            self.t = self.next(self.t) 
            self.q[self.t] = value 

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.h] = -1 
        idx = self.next(self.h)
        if self.q[idx] >= 0:
            self.h = idx

        return True        

    def Front(self) -> int:
        return self.q[self.h]         

    def Rear(self) -> int:
        return self.q[self.t] 

    def isEmpty(self) -> bool:
        return self.h == self.t and self.q[self.h] == -1
        
    def isFull(self) -> bool:
        idx = self.next(self.t)
        return self.q[idx] != -1
