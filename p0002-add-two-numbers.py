# 
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 

from typing import List
import pdb

#
# Definition for singly-linked list.
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 3/28: I spent 15 mins to write addTwoNumbers()
# 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        pre_node = None
        head = None
        carry = 0
        while True:
            if n1 == None:
                v1 = 0
            else:    
                v1 = n1.val
            
            if n2 == None:
                v2 = 0
            else:    
                v2 = n2.val
            
            v3 = v1 + v2 + carry
            if v3 >= 10:
                v3 -= 10
                carry = 1
            else:
                carry = 0
            n3 = ListNode(v3)
            
            if head == None:
                head = n3
            
            if pre_node != None:
                pre_node.next = n3
            pre_node = n3
            
            #print(v1, v2, v3, carry)
            
            if n1 != None:
                n1 = n1.next
            
            if n2 != None:
                n2 = n2.next
                
            if n1 == None and n2 == None:
                break
        
        if carry == 1:        
            n3 = ListNode(1)
            pre_node.next = n3
        
        return head
        
    #
    # 3/28: I spent 15 mins to write to_linked_list() and to_list()
    #        
            
    def to_linked_list(self, ls):
        head = ListNode(ls[0])
        n0 = head
        for i in range(1, len(ls)):
            n1 = ListNode(ls[i])
            n0.next = n1
            n0 = n1
        return head

    def to_list(self, head):
        ls = []
        node = head
        while True:
            ls.append(node.val)
            if node.next == None:
                break
            node = node.next
        return ls    
        
        

 