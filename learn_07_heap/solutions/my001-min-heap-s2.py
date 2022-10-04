#
# https://leetcode.com/explore/learn/card/heap/643/heap/4017/
#
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

"""
      0
   1     2
  3 4   5 6
"""

def parent(i):
    if i % 2 == 0:
        return (i - 1) // 2
    else:
        return i // 2

def left(i):
    return i * 2 + 1

def right(i):
    return (i + 1) * 2 

"""
    3            1    
  1      --->  3 
"""

def heapify(a):
    n = len(a)
    i = n - 1
    while True:
        if i == 0:
            break

        if a[i] < a[parent(i)]:
            swap(a, i, parent(i))
            i = parent(i)
        else:
            break

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]        

'''
    10       10         10
  3    5   3   20     5    3  
'''
def down_heapify(a):
    n = len(a)
    i = 0 
    while True:
        idx = None 
        if left(i) <= n - 1:
            if a[left(i)] < a[i]:
                idx = left(i)

        if right(i) <= n - 1:
            if a[right(i)] < a[i]:
                if idx == None:
                    idx = right(i)
                else:
                    if a[right(i)] < a[idx]:
                        idx = right(i)

        if idx == None:
            break

        swap(a, idx, i)
        i = idx             

#
# Implementing "Min Heap"
#

class MinHeap:
    def __init__(self, heapSize):
        self.a = []
        self.max = heapSize
        pass

    #
    # Example:
    #   obj = MinHeap()
    #   ...
    #   print(str(obj))
    #       [1,2,3]
    #

    def __str__(self):
        return "%s" % self.a        

    def dump(self):
        print('%s' % self.a)

    #
    # Function to add an element
    # element >= 1
    #    
    """
        3
      1   2
    """
    def add(self, element):
        self.a.append(element)
        heapify(self.a)
        pass
    
    #
    # Get the top element of the Heap
    #

    def peek(self):
        return self.a[0]
    
    #
    # Delete the top element of the Heap
    #

    def pop(self):
        last_i = len(self.a) - 1
        swap(self.a, 0, last_i)
        min_v = self.a.pop()
        down_heapify(self.a)
        return min_v
    
    #
    # return the number of elements in the Heap
    #

    def size(self):
        return 0
