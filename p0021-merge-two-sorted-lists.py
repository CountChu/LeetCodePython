#
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:       
        n1 = l1
        n2 = l2
        pre_n3 = None
        first_n3 = None
        while True:

            if n1 == None and n2 == None:
                break
            elif n1 == None and n2 != None:
                min_val = n2.val
                n2 = n2.next
            elif n2 == None and n1 != None:
                min_val = n1.val
                n1 = n1.next
            elif n1.val <= n2.val:
                min_val = n1.val
                n1 = n1.next
            else:
                min_val = n2.val
                n2 = n2.next

            #print('min_val = %d' % min_val)
            n3 = ListNode(min_val)
            if first_n3 == None:
                first_n3 = n3
            if pre_n3 != None:
                pre_n3.next = n3
            pre_n3 = n3

        return first_n3
        
    def list_to_link(self, list):
        pre_node = None
        first_node = None
        for i in range(len(list)):
            node = ListNode(list[i])
            if first_node == None:
                first_node = node
            if pre_node != None:
                pre_node.next = node
            pre_node = node
        return first_node
            
    def print_link(self, link):
        node = link
        line = ''
        while True:    
            line += (str(node.val) + ' -> ')
            node = node.next
            if node == None:
                break
        print(line)    

    def link_to_list(self, link):
        node = link
        list = []
        while True:    
            if node == None:
                break
            list.append(node.val)
            node = node.next
            
        return list   


