#
# https://leetcode.com/problems/add-two-numbers/
#

from typing import List
import pdb

solution_json = {
    "date": "2022/?/??",
    "coding": 0,
    "runtime": "?? ms",
    "memory": "?? MB"
}  

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return None
                
    def to_linked_list(self, ls):
        head = None
        pre_node = None
        for val in ls:
            node = ListNode(val)
            if pre_node != None:
                pre_node.next = node
            if head == None:
                head = node
            pre_node = node    
            #print(val)

        return head

    def to_list(self, linked_list):
        ls = []
        node = linked_list
        while True:
            val = node.val
            #print(val)
            ls.append(val)
            node = node.next
            if node == None:
                break
                
        return ls
        

 