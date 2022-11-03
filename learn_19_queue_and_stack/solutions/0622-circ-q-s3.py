#
# https://leetcode.com/problems/design-circular-queue/
#
# Design your implementation of the circular queue. 
# The circular queue is a linear data structure in which the operations 
# are performed based on FIFO (First In First Out) principle 
# and the last position is connected back to the first position 
# to make a circle. It is also called "Ring Buffer".
#
# Constraints:
#
#   1 <= k <= 1000
#   0 <= value <= 1000
#   At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, 
#   and isFull.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/11",
    "design": 0,
    "coding": 0,
    "runtime": "69 ms",
    "fasterThan": "95%",
    "memory": "14.6 MB" 
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

'''
  fr
  -1   0   1   2 
      [0,  0,  0]       isEmpty(): True
    
       fr  
  -1   0   1   2
      [1,  0,  0]       enQueue(1)
        
       f   r   
  -1   0   1   2       
      [1,  2,  0]       enQueue(2)
    
       f       r
  -1   0   1   2
      [1,  2,  3]       enQueue(3)
                        isFull(): True

           f   r
  -1   0   1   2
      [1,  2,  3]       deQueue()

       r   f   
  -1   4   1   2
      [1,  2,  3]       enQueue(4)

'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.a = [0] * self.k
        self.f = -1
        self.r = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.r += 1
        self.r = self.r % self.k
        self.a[self.r] = value 

        if self.f == -1:
            self.f = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.f == self.r:
            self.f = self.r = -1
        else:
            self.f += 1
            self.f = self.f % self.k

        return True        

    def Front(self) -> int:
        if self.isEmpty():
            return -1  

        return self.a[self.f]              

    def Rear(self) -> int:
        if self.isEmpty():
            return -1        

        return self.a[self.r]

    def isEmpty(self) -> bool:
        return self.f == self.r == -1
        
    def isFull(self) -> bool:
        return (self.r + 1) % self.k == self.f

    def dump(self):
        print('a = %s, f = %d, r = %d' % (self.a, self.f, self.r))




