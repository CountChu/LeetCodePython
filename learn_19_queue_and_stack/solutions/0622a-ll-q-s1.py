from typing import List
import sys
import pdb

solution_json = {
    "date": "2022/9/2",
    "design": 0,
    "coding": 0,
    "runtime": "108 ms",
    "fasterThan": "50%",
    "memory": "14.7 MB" 
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

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

    def __repr__(self):
        s1 = ''
        n = self  
        while True:
            if n == None:
                break

            s1 += str(n.val) + " -> " 
            n = n.next
        return s1

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False

        node = Node(value)

        if self.head == None:
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node 
            self.tail = node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.head == None:
            return False

        self.head = self.head.next
        if self.head == None:
            self.tail = None 
        self.size -= 1
        return True        

    def Front(self) -> int:
        if self.head == None:
            return -1                
        else:
            return self.head.val

    def Rear(self) -> int:
        if self.tail == None:
            return -1        
        else:
            return self.tail.val


    def isEmpty(self) -> bool:
        return self.size ==0
        
    def isFull(self) -> bool:
        return self.size == self.max_size
