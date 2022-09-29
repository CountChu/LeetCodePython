#
# https://leetcode.com/explore/learn/card/heap/643/heap/4017/
#
#

from typing import List
import sys
import pdb

solution_json = {
    "date": "2022/9/3",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

br = pdb.set_trace

#
#        0
#    1       2
#  3   4   5   6
#

def parent(idx):
    if idx == 0:
        return -1 

    if idx % 2 == 1:
        return idx // 2 
    else:
        return idx // 2 - 1

def left(idx):
    return idx * 2 + 1

def right(idx):
    return (idx + 1) * 2

def swap(tree, i, j):
    tree[i], tree[j] = tree[j], tree[i]

#
# Implementing "Min Heap"
#

class MinHeap:
    def __init__(self, heapSize):
        self.tree = [0] * heapSize      # Implement heap with complete binary tree.
        self.i = -1                     # Index of the last element in the tree. i + 1 = size
        self.max_size = heapSize

    #
    # Example:
    #   obj = MinHeap()
    #   ...
    #   print(str(obj))
    #       [1,2,3]
    #

    def __str__(self):
        return "%s" % self.tree[0: self.i+1]

    def dump(self):
        print("%d, %d, %s" % (self.i, self.max_size, self.tree))

    def heapify(self):
        idx = self.i

        while True:
            p_idx = parent(idx)
            if p_idx == -1:
                break

            if self.tree[idx] < self.tree[p_idx]:
                swap(self.tree, idx, p_idx)
            else:
                break

    def down_heapify(self):
        idx = 0
 
        while True:
            left_idx = left(idx)
            right_idx = right(idx)
     
            if left_idx > self.i:
                return 
     
            if self.tree[idx] > self.tree[left_idx]:
                swap(self.tree, idx, left_idx)
                idx = left_idx 
            else:
                if right_idx > self.i:
                    return
                if self.tree[idx] > self.tree[right_idx]:
                    swap(self.tree, idx, right_idx)
                    idx = right_idx

    #
    # Function to add an element
    # element >= 1
    #

    def add(self, element):
        assert self.i < self.max_size, self.max_size 
        assert element >= 1 

        self.i += 1
        self.tree[self.i] = element

        self.heapify()
    
    #
    # Get the top element of the Heap
    #

    def peek(self):
        if self.i == -1:
            return -1

        return self.tree[0]
    
    #
    # Delete the top element of the Heap
    #

    def pop(self):
        if self.i == -1:
            return -1

        out = self.tree[0]
        self.tree[0] = self.tree[self.i]
        self.i -= 1

        self.down_heapify()
        return out
    
    #
    # return the number of elements in the Heap
    #

    def size(self):
        return 0
    


