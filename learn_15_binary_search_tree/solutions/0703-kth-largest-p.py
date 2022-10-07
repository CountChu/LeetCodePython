#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#
# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.
# 
# Implement KthLargest class:
#       
#       - KthLargest(int k, int[] nums) Initializes the object 
#       with the integer k and the stream of integers nums.
#
#       - int add(int val) Appends the integer val to the stream 
#       and returns the element representing the kth largest element in the stream.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/7",
    "design": 0,
    "coding": 0,
    "runtime": "1804 ms",
    "fasterThan": "6%",
    "memory": "18.3 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        self.nums = self.nums[:self.k]

    def add(self, val: int) -> int:  
        self.nums.append(val)
        self.nums.sort(reverse=True)
        self.nums = self.nums[:self.k]
        return self.nums[-1]

    def dump(self):
        print(self.nums)

#
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
#

