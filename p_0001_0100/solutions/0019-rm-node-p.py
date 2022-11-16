#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 20,
    "runtime": "61 ms",
    "fasterThan": "58%",
    "memory": "14 MB" 
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
        0    1    2    3    4
        1 -> 2 -> 3 -> 4 -> 5
        1 -> 2 -> 3 ------> 5      n = 2, step = 3
  

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = get_length(head)
        if length == 1 and n == 1:
            return None

        steps = length - n
        #print(steps)

        if steps == 0:
            head = head.next
            return head

        nd0 = head
        nd1 = head.next
        i = 0
        while True:
            if nd1 == None:
                break
            
            #print(i, nd0.val, nd1.val)
            if i == steps - 1:
                nd0.next = nd1.next
                break

            nd0 = nd0.next
            nd1 = nd1.next
            i += 1

        return head

def get_length(head):
    out = 0
    nd = head 
    while True:
        if nd == None:
            break

        out += 1
        nd = nd.next

    return out


