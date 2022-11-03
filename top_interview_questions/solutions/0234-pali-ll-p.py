#
# https://leetcode.com/problems/palindrome-linked-list/
#
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 3,
    "runtime": "942 ms",
    "fasterThan": "82%",
    "memory": "46.9 MB" 
}

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
        while nd != None:
            #print(nd.val)
            ls.append(nd.val)
            nd = nd.next

        i = 0 
        j = len(ls) - 1
        while True:
            if i > j:
                break

            if ls[i] != ls[j]:
                return False

            i += 1
            j -= 1

        return True


