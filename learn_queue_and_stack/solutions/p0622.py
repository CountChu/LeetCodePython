from typing import List
import pdb

#
# 2021/5/12: 14, 39, 73 ms, 16.4 MB
#

class MyCircularQueue:

    def __init__(self, k: int):
        self.d = False
        self.v = [-1]*k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        out = False

        if self.head == -1 and self.tail == -1:
            self.head += 1
            self.tail += 1
            self.v[self.tail] = value
            out = True
        else:
            if self.isFull():
                out = False
            else:
                self.tail += 1
                if self.tail == len(self.v):
                    self.tail = 0
                self.v[self.tail] = value
                out = True

        if self.d:
            print('en: %d, %s, %d, %d' % (value, self.v, self.head, self.tail))

        return out


    def deQueue(self) -> bool:
        out = False

        if self.isEmpty():
            out = False
        else:
            self.v[self.head] = -1
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head += 1
                if self.head == len(self.v):
                    self.head = 0
            out = True

        if self.d:
            print('de: %s, %d, %d' % (self.v, self.head, self.tail))            

        return out

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.v[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.v[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1 and self.tail == -1

    def isFull(self) -> bool:
        return self.tail - self.head + 1 in [len(self.v), 0]

class Solution:
    def __init__(self):
        pass