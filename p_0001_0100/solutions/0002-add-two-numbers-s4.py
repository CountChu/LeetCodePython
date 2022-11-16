#
# https://leetcode.com/problems/add-two-numbers/
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 8,
    "runtime": "80 ms",
    "fasterThan": "83%",    
    "memory": "14 MB"
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
    [2, 4, 3]
    [5, 6, 4]
    [7, 0, 8]
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nd1 = l1
        nd2 = l2
        c = 0
        out = None
        nd3_0 = None
        while True:
            if nd1 == None and nd2 == None:
                break
            
            c, v = adder(nd1, nd2, c)
            nd3_1 = ListNode(v)
            if out == None:
                out = nd3_1
                nd3_0 = nd3_1
            else:
                nd3_0.next = nd3_1 
                nd3_0 = nd3_1

            if nd1 != None:
                nd1 = nd1.next

            if nd2 != None:
                nd2 = nd2.next

        if c == 1:
            nd3_1 = ListNode(c)
            nd3_0.next = nd3_1

        return out

def adder(nd1, nd2, c):
    #print(nd1.val, nd2.val, c)
    v = c
    if nd1 != None:
        v += nd1.val 
    if nd2 != None:
        v += nd2.val

    c = 0
    if v >= 10:
        v -= 10
        c = 1
    return c, v
