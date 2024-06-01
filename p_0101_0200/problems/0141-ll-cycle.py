#
# https://leetcode.com/problems/linked-list-cycle/
#
# Given head, the head of a linked list, determine if the linked list has a cycle 
# in it.
# 
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node 
# that tail's next pointer is connected to. Note that pos is not passed 
# as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return false.
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

#
# Definition for singly-linked list.
# 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def hasCycle(self, head: ListNode) -> bool:
        return True
