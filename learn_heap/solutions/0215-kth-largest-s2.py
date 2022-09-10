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
    "date": "2022/9/5",
    "design": 0,
    "coding": 0,
    "runtime": "2085 ms",
    "fasterThan": "16.18%",
    "memory": "27.3 MB" 
}


"""
        0
    1       2
   3 4     5 6
"""

def parent(idx):
    if idx % 2 == 1:
        idx = idx // 2 
    else:
        idx = idx // 2 
        idx -= 1
    return idx

def left(idx):
    return idx * 2 + 1 

def right(idx):
    return (idx + 1) * 2

def is_leaf(n, idx):
    return left(idx) >= n

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def down_heapify(nums, n, idx):
    left_idx = left(idx)
    right_idx = right(idx)

    swap_type = 'no'
    if left_idx < n:
        if nums[left_idx] > nums[idx]:
            swap_type = 'left'
            if right_idx < n: 
                if nums[right_idx] > nums[left_idx]:
                    swap_type = 'right'
        else:
            if right_idx < n:
                if nums[right_idx] > nums[idx]:
                    swap_type = 'right'

    if swap_type == 'left':
        swap(nums, left_idx, idx)
        down_heapify(nums, n, left_idx)
    elif swap_type == 'right':
        swap(nums, right_idx, idx)
        down_heapify(nums, n, right_idx)


"""
            3
        2       1
      5   6   4  


            6
        5       4
      2   3   1  

"""

def heapify(nums, n):
    for i in reversed(range(n)):
        if is_leaf(n, i):
            continue 

        down_heapify(nums, n, i)

def pop(nums, n):
    #assert n >= 1
    max_val = nums[0]
    swap(nums, 0, n-1)
    n -= 1
    down_heapify(nums, n, 0)
    return max_val, n


class Solution:
    def __init__(self):
        #self.module = sys.modules[__name__]
        pass

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums, n)
        #print(nums)

        max_val = None
        for i in range(k):
            max_val, n = pop(nums, n)
        
        return max_val



