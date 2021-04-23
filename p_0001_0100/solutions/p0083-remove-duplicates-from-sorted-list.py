# 
# Given the head of a sorted linked list, delete all duplicates 
# such that each element appears only once. 
# Return the linked list sorted as well.
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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    
        if head == None:
            return None
    
        node = head
        pre_node = None
        new_head = None
        new_node = None
        while True:
            line = ''
            if pre_node == None:                
                new_node = ListNode(node.val)
                new_head = new_node 
                pre_node = new_node
                #line += '1: pre_node.val = %d, ' % pre_node.val
            else:
                if pre_node.val != node.val:
                    new_node = ListNode(node.val)
                    pre_node.next = new_node
                    pre_node = new_node
                    #line += '2: pre_node.val = %d, ' % pre_node.val
                    
            #print(line)                
            node = node.next
            if node == None:
                break
        return new_head
            
        
    def to_ll(self, head):
        node = None
        next = None
        for i in reversed(range(len(head))):
            node = ListNode(head[i], next)
            next = node
        return node
        
    def to_array(self, ll):
        node = ll
        list = []
        while True:
            list.append(node.val)
            node = node.next
            if node == None:
                break
        return list        
        