#
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Given an integer array nums and an integer k, return the kth largest element 
# in the array.
#
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.
#
# You must solve it in O(n) time complexity.
#
# Example 1:
#       Input: nums = [3,2,1,5,6,4], k = 2
#       Output: 5
#
# Example 2: 
#       Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#       Output: 4
# 

from typing import List
import pdb
import sys
br = pdb.set_trace

solution_json = {
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "5922 ms",
    "fasterThan": "5%",
    "memory": "25.4 MB"
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
    return left(i) >= n


'''
    1         2
  2    ->   1

    1         3
  2   3 ->  2   1

    1         3
  3   2 ->  1   2 
'''
def down_heapify(a, n, i):
    

    while True:
        idx = None
        
        if left(i) <= n - 1:
            if a[left(i)] > a[i]:
                idx = left(i)

        if right(i) <= n - 1:
            if a[right(i)] > a[i]:
                if idx == None:
                    idx = right(i)
                else:
                    if a[right(i)] > a[idx]:
                        idx = right(i)

        if idx == None:
            break 

        swap(a, i, idx)
        i = idx 

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

'''
       3     
    2     1  
  5  6  4    
'''
def heapify(nums):
    n = len(nums)
    for i in reversed(range(n)):
        if is_leaf(n, i):
            continue
        
        #print(i)
        down_heapify(nums, n, i)

'''
           6
        5     4
       3 2   1   
'''
def pop(nums):
    swap(nums, 0, len(nums) - 1)
    out = nums.pop()
    down_heapify(nums, len(nums), 0)
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        out = None
        for i in range(k):
            out = pop(nums)
        return out
