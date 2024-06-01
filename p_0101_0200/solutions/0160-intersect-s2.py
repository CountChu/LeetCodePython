solution_json = {
    "date": "2023/12/23",
    "design": 0,
    "coding": 6,
    "runtime": "74 ms",
    "fasterThan": "99%",
    "memory": "28.6 MB"
}

#
# https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
     0  1  2  3  4
    [4, 1, 8, 4, 5]
           .  .  .

     0  1  2  3  4  5
    [5, 6, 1, 8, 4, 5]
              .  .  .

'''

def build_set(head):
    out = set()
    nd = head
    while True:
        if nd == None:
            break 

        out.add(nd)
        nd = nd.next

    return out

def dump_set(nd_set):
    for nd in nd_set:
        lg('%d, ' % nd.val, end='')
    lg('')

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        set0 = build_set(headA)
        #dump_set(set0)
        
        out = None
        nd = headB
        while True:
            if nd == None:
                break

            if nd in set0:
                out = nd
                break 

            nd = nd.next 

        return out






