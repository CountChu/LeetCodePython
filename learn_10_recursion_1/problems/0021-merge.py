#
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Example 1:
#       Input: list1 = [1,2,4], list2 = [1,3,4]
#       Output: [1,1,2,3,4,4]
#
# Example 2: 
#       Input: list1 = [], list2 = []
#       Output: []
#
# Example 3:
#       Input: list1 = [], list2 = [0]
#       Output: [0]
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

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        pass      
