#
# Implement queue with linked list.
#

from typing import List
import sys
import pdb

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
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

class MyCircularQueue:

    def __init__(self, k: int):
        pass
        
    def enQueue(self, value: int) -> bool:
        return False

    def deQueue(self) -> bool:
        return False        

    def Front(self) -> int:
        return -1                

    def Rear(self) -> int:
        return -1        

    def isEmpty(self) -> bool:
        return False
        
    def isFull(self) -> bool:
        return False
