#
# https://leetcode.com/problems/reverse-linked-list/
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#       Input: head = [1,2,3,4,5]
#       Output: [5,4,3,2,1]
#
# Example 2: 
#       Input: Input: head = [1,2]
#       Output: Output: [2,1]
# 
# Example 3:
#       Input: []
#       Output: []
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

    def reverseList(self, head: ListNode) -> ListNode:
        pass
