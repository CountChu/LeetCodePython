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

solution_json = {
    "date": "2023/12/6",
    "design": 0,
    "coding": 0,
    "runtime": "132 ms",
    "fasterThan": "34%",
    "memory": "31.54 MB" 
}

'''
    A   4 1 8 4 5
    B   5 6 1 8 4 5
'''

def build_ls(head):
    out = []
    nd = head
    while True:
        if nd == None:
            break
        out.append(nd)
        nd = nd.next     

    return out

def lg_ls(ls):
    for nd in ls:
        print('%d -> ' % nd.val, end='')
    print('')

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        ls0 = build_ls(headA)
        #lg_ls(ls0)
        ls1 = build_ls(headB) 
        #lg_ls(ls1)

        out = None
        while True:
            if len(ls0) == 0:
                break

            if len(ls1) == 0:
                break

            nd0 = ls0.pop()
            nd1 = ls1.pop()
            #lg(nd0, nd1)
            if nd0 == nd1:
                out = nd0
            else:
                break

        return out
