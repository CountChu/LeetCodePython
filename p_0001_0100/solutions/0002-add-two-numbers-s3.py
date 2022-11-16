#
# https://leetcode.com/problems/add-two-numbers/
#

from typing import List
import pdb

solution_json = {
    "date": "2022/8/17",
    "coding": 0,
    "runtime": "113 ms",
    "fasterThan": "43%",
    "memory": "14 MB"
}  

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2 
        l3 = None
        n3 = None  
        c = 0
        while True:
            if n1 != None and n2 != None:
                #print(n1.val, n2.val)
                val = n1.val + n2.val + c
            elif n1 != None and n2 == None:
                #print(n1.val, '')
                val = n1.val + c
            elif n1 == None and n2 != None:
                #print('', n2.val)
                val = n2.val + c
            elif n1 == None and n2 == None:
                break
            else:
                assert False 

            if val >= 10:
                val -= 10 
                c = 1 
            else:
                c = 0

            if l3 == None:
                l3 = ListNode()
                n3 = l3
                n3.val = val
            else: 
                n3.next = ListNode()
                n3.next.val = val 
                n3 = n3.next 

            if n1 != None:
                n1 = n1.next 

            if n2 != None:
                n2 = n2.next 

        if c == 1:
            n3.next = ListNode()
            n3.next.val = 1
            n3 = n3.next 

        #pdb.set_trace()
        return l3

        

 