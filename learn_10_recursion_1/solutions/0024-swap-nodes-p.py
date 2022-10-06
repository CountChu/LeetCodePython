#
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values 
# in the list's nodes (i.e., only nodes themselves may be changed.)
#
# Example 1:
#       Input: head = [1,2,3,4]
#       Output: [2,1,4,3]
#
# Example 2: 
#       Input: []
#       Output: []
# 
# Example 3: 
#       Input: [1]
#       Output: [1]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "38 ms",
    "fasterThan": "84%",
    "memory": "14 MB" 
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    0    1    2    3
    1 -> 2 -> 3 -> 4
    2 -> 1 -> 4 -> 3

    func(pre, nd0)
        nd1 = nd0.next
        nd2 = nd1.next
        nd1 -> nd0
        pre -> nd1

        func(nd0, nd2)
        
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def swapPairs(self, head: ListNode) -> ListNode:
        ctx = {
            'head': None
        }

        if head == None:
            return None 

        if head.next == None:
            return head 

        func(None, head, ctx)
        #dump(ctx['head'])
        return ctx['head']

def func(pre, nd0, ctx):
    if nd0 == None:
        return
    #print(nd0.val)


    nd1 = nd0.next
    if nd1 == None:
        pre.next =  nd0        
        return

    nd2 = nd1.next

    nd1.next = nd0 
    if pre != None:
        pre.next =  nd1
    
    if ctx['head'] == None:
        ctx['head'] = nd1

    nd0.next = None
    func(nd0, nd2, ctx)

def dump(nd):
    
    while True:
        if nd == None:
            print('')
            break 

        print('%d ->' % nd.val, end='')
        nd = nd.next 


   
