#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/
#
# Implement Disjoint Set with weighted quick union and path compression.
#
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/3",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]


class UnionFind:
    def __init__(self, size):
        self.w = [1] * size 
        self.a = [i for i in range(size)]

    def init(self, a, w):
        self.a = a
        self.w = w

    def __str__(self):
        return ''

    def dump(self):
        print(str(self))

    def get_a(self):
        return self.a

    def get_w(self):
        return self.w         

    def find(self, x):
        i = x
        s = []
        r_i = None 
        while True:
            if self.a[i] == i:
                r_i = i
                break

            s.append(i)
            i = self.a[i]

        for i in s:
            self.a[i] = r_i

        return r_i

    """
        union(1, 2)
            x  y
         0  1  2  3  4  5  6  7  8  9
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = a
        [      1                     ] 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] = w
        [   2                        ] 

        union(2, 5)
            v  x        y
         0  1  2  3  4  5  6  7  8  9
        [0, 1, 1, 3, 4, 5, 6, 7, 8, 9] = a
        [               1            ]
        [1  2  1  1  1  1  1  1  1  1] = w
    """
    def union(self, x, y):
        x_r_i = self.find(x)
        y_r_i = self.find(y)
        if self.w[x_r_i] == self.w[y_r_i]: 
            self.a[y_r_i] = x_r_i
            self.w[x_r_i] += 1
        elif self.w[x_r_i] > self.w[y_r_i]:
            self.a[y_r_i] = x_r_i
        else:
            self.a[x_r_i] = y_r_i 

    def connected(self, x, y):
        return self.find(x) == self.find(y)
      
