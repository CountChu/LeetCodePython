from typing import List
import pdb

solution_json = {
    "date": "2021/4/10",
    "coding": 28
}   

#
# Definition for singly-linked list.
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 2021/4/10: 28 mins
#

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        n1 = l1
        n2 = l2
        c = 0
        n3_head = None
        n3_pre = None
        while True:

            if n1 == None and n2 == None:
                break
                
            v1 = 0    
            if n1 != None:
                v1 = n1.val
                n1 = n1.next
            
            v2 = 0 
            if n2 != None:
                v2 = n2.val
                n2 = n2.next
                
            v3 = v1 + v2 + c
            c = 0
            if v3 >= 10:
                v3 -= 10
                c = 1

            n3 = ListNode(v3)
            if n3_head == None:
                n3_head = n3
            if n3_pre != None:
                n3_pre.next = n3
            n3_pre = n3    

            #print(v1, v2, v3, c)    
            
        if c == 1:
            n3 = ListNode(c)
            n3_pre.next = n3
            
        return n3_head
        

        

 