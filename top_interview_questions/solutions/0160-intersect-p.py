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

solution_json = {
    "date": "2022/11/1",
    "design": 0,
    "coding": 0,
    "runtime": "412 ms",
    "fasterThan": "21%",
    "memory": "30.4 MB" 
}

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def dump(head):
    s = ''
    nd = head
    while nd != None:
        s += '%d' % nd.val + ' -> '
        nd = nd.next 
    #print(s)        

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        node_set = set()
        nd = headA
        while nd != None:
            node_set.add(nd)
            nd = nd.next

        out = None
        nd = headB
        while nd != None:
            if nd in node_set:
                out = nd
                break

            nd = nd.next

        return out
