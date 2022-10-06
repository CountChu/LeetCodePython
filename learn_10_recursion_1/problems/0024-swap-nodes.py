#
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values 
# in the list's nodes (i.e., only nodes themselves may be changed.)
#
# Example 1:
#       Input: head = [1,2,3,4]
#       Output: [2,1,4,3]
#
# Example 2: 
#       Input: []
#       Output: []
# 
# Example 3: 
#       Input: [1]
#       Output: [1]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def swapPairs(self, head: ListNode) -> ListNode:
        pass
   
