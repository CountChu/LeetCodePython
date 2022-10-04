#
# https://leetcode.com/explore/learn/card/heap/644/common-applications-of-heap/4145/
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

'''
        0
     1     2
    3 4   5 6 
'''
def parent(i):
    if i % 2 == 0:
        return i // 2 - 1
    else:
        return i // 2

def left(i):
    return i * 2 + 1

def right(i):
    return (i + 1) * 2

def is_leaf(n, i):
    return left(i) > n-1

'''
    10       10         10
  3    5   3   20     5    3  
'''
def down_heapify(a, n, i):

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

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

class Solution:
    '''
               12
          9          10
        6   4      5    3     
    '''
    def heapify(self, arr):
        n = len(arr)
        for i in reversed(range(n)):
            if is_leaf(n, i):
                continue 
            down_heapify(arr, n, i)


