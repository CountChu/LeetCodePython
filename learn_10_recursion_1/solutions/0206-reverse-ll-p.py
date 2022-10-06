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
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "67 ms",
    "fasterThan": "42%",
    "memory": "20.5 MB" 
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
       1 -> 2 -> 3 -> 4 -> 5 -> N
  N <- 1 <- 2 <- 3 <- 4 <- 5

       0    1    2
  N <- 1 <- 2 
  N <- 1 <- 2 <- 3 
    
'''        
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def reverseList(self, head: ListNode) -> ListNode:        
        if head == None:
            return None

        ctx = {
            'head': None
        }
        nd0 = head 
        nd1 = nd0.next
        nd0.next = None
        func(nd0, nd1, ctx)
        
        return ctx['head']

def func(nd0, nd1, ctx):
    if nd1 == None:
        ctx['head'] = nd0
        return

    nd2 = nd1.next
    nd1.next = nd0
    func(nd1, nd2, ctx)













