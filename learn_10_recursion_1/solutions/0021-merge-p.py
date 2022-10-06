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
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "71 ms",
    "fasterThan": "39%",
    "memory": "14 MB" 
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    1 -> 2 -> 4
    1 -> 3 -> 4
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        nd1 = list1 
        nd2 = list2 

        head = None
        pre = None
        while True:
            if nd1 == None and nd2 != None:
                v = nd2.val 
                nd2 = nd2.next 
            
            elif nd1 != None and nd2 == None:
                v = nd1.val 
                nd1 = nd1.next
            
            elif nd1 == None and nd2 == None:
                break    
            
            else:
                if nd1.val < nd2.val:
                    v = nd1.val
                    nd1 = nd1.next 
                else:
                    v = nd2.val
                    nd2 = nd2.next 

            nd3 = ListNode(v)
            if head == None:
                head = nd3
            if pre != None:
                pre.next = nd3
            pre = nd3

        return head

