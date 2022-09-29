from typing import List
import pdb

solution_json = {
    "date": "2021/6/15",
    "design": 5,
    "coding": 14,
    "runtime": "32 ms",
    "memory": "15.8 MB"
} 

class Solution:
    def __init__(self):
        pass

    

class MyStack:

    def __init__(self):
        self.d = False

        self.q1 = []
        self.f1 = -1
        self.r1 = -1

        self.q2 = []   
        self.f2 = -1
        self.r2 = -1
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q1 == []:
            self.f1 = 0
            self.r1 = 0
        else:
            self.r1 += 1    
        self.q1.append(x)

        if self.d:
            print('push(): f1 = %d, r1 = %d, q1 = %s' % (self.f1, self.r1, self.q1))
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        top = None
        while True:
            if self.f1 == self.r1:
                top = self.q1[self.f1]
                break

            if self.q2 == []:
                self.f2 = 0
                self.r2 = 0
            else:
                self.r2 += 1

            self.q2.append(self.q1[self.f1])
            self.f1 += 1

        if self.d:
            print('pop(): f1 = %d, r1 = %d, q1 = %s' % (self.f1, self.r1, self.q1))            
            print('pop(): f2 = %d, r2 = %d, q2 = %s' % (self.f2, self.r2, self.q2))

        self.q1 = self.q2
        self.f1 = self.f2
        self.r1 = self.r2

        self.q2 = []
        self.f2 = -1
        self.r2 = -1

        if self.d:
            print('pop(): f1 = %d, r1 = %d, q1 = %s' % (self.f1, self.r1, self.q1))            
            print('pop(): f2 = %d, r2 = %d, q2 = %s' % (self.f2, self.r2, self.q2))

        return top                            

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[self.r1]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return self.f1 == -1 and self.r1 == -1
