from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/6/15",
    "design": 5,
    "coding": 12,
    "runtime": "32 ms",
    "memory": "15.7 MB" 
}  

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []                    # stack 1
        self.s2 = []                    # stack 2
        pass
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        d = False

        while True:
            if self.s1 == []:
                break

            top = self.s1.pop()
            self.s2.append(top)

        self.s1.append(x)
        

        while True:
            if self.s2 == []:
                break

            top = self.s2.pop()
            self.s1.append(top)    

        if d:
            print('push():', self.s1)        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        d = False

        top = self.s1.pop()
        if d:
            print('pop():', self.s1)
        return top


    def peek(self) -> int:
        """
        Get the front element.
        """

        top = self.s1[-1]
        return top


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return self.s1 == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()