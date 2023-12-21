solution_json = {
    "date": "2023/12/9",
    "design": 0,
    "coding": 0,
    "runtime": "633 ms",
    "fasterThan": "18%",
    "memory": "49.44 MB" 
}

#
# https://leetcode.com/problems/palindrome-linked-list/
#
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

'''
    1 -> 2 -> 2 -> 1

'''

lg = print

#
# Definition for singly-linked list.
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPalindrome(self, head: ListNode) -> bool:    

        nd = head
        ls = []
        while True:
            if nd == None:
                break 
            #lg(nd.val)
            ls.append(nd.val) 
            nd = nd.next

        n = len(ls)
        i = 0 
        j = n - 1 
        while True:
            if i > j:
                break 

            if ls[i] != ls[j]:
                return False 

            i += 1 
            j -= 1

        return True

