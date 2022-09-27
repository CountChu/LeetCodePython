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
# Example 1:
#       Input: head = [3,2,0,-4], pos = 1
#       Output: true
#
# Example 2: 
#       Input: head = [1,2], pos = 0
#       Output: true
# 
# Example 3: 
#       Input: head = [1], pos = -1
#       Output: false
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/22",
    "design": 0,
    "coding": 0,
    "runtime": "147 ms",
    "fasterThan": "6%",
    "memory": "17.6 MB" 
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


        step1 = head 
        step2 = head 

        while True:
            if step1 == None:
                return False

            step1 = step1.next

            if step2 == None:
                return False

            if step2.next == None:
                return False

            step2 = step2.next.next 

            if step1 == step2:
                return True 

