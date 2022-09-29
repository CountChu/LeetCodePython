#
# https://leetcode.com/explore/learn/card/heap/644/common-applications-of-heap/4145/
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

br = pdb.set_trace

#
#       0
#   1       2
# 3   4   5   6
#


#
#        12
#     9      10
#   6   4  5    3
#


def parent(idx):
    if idx == 0:
        return -1

    if idx % 2 == 1:
        return idx // 2 
    else:
        return (idx // 2) - 1 

def left(idx):
    return idx * 2 + 1 

def right(idx):
    return (idx + 1) * 2

def is_leaf(arr, idx):
    left_idx = left(idx)
    return left_idx >= len(arr)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def down_heapify(arr, idx):
    if is_leaf(arr, idx):
        return
    
    left_idx = left(idx)
    right_idx = right(idx)
    
    if arr[idx] > arr[right_idx]:
        swap(arr, idx, right_idx)
        down_heapify(arr, right_idx)

    if arr[idx] > arr[left_idx]:
        swap(arr, idx, left_idx)
        down_heapify(arr, left_idx)

class Solution:
    def heapify(self, arr):
        n = len(arr)
        for i in reversed(range(n)):
            if is_leaf(arr, i):
                continue 
            else:
                down_heapify(arr, i)
        pass
