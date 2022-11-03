#
# Implement queue with linked list.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/12",
    "design": 0,
    "coding": 0,
    "runtime": "155 ms",
    "fasterThan": "33%",
    "memory": "15.6 MB" 
}

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

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
    fr -> N
    h
    0 -> 0 -> 0 

    enQueue(1)      hfr
                    1 -> 0 -> 0
    enQueue(2)      hf   r 
                    1 -> 2 -> 0
    enQueue(3)      hf        r 
                    1 -> 2 -> 3
    enQueue(4)      False
    Rear()          3
    isFull()        True
    deQueue()       h    f    r 
                    1 -> 2 -> 3
    enQueue(4)      hr   f
                    4 -> 2 -> 3
    Rear()          4

'''
class MyCircularQueue:

    def __init__(self, k: int):
        assert k >= 1

        self.size = 0
        self.k = k

        nd = Node(0)
        self.h = nd
        for i in range(1, self.k):
            nd.next = Node(0)
            nd = nd.next
        nd.next = self.h

        self.f = None
        self.r = None

    def dump(self):
        print('size: %d' % self.size)
        s = ''
        nd = self.h
        for i in range(self.k):
            s += '%s -> ' % nd.val
            nd = nd.next
        print(s)
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        elif self.isEmpty():
            self.f = self.h
            self.r = self.h

        else:
            self.r = self.r.next

        self.r.val = value
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False        

        self.f = self.f.next
        self.size -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1                

        return self.f.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1        

        return self.r.val

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.k
