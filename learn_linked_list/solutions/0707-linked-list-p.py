#
# https://leetcode.com/problems/design-linked-list/
#
# Design your implementation of the linked list. You can choose to use a singly 
# or doubly linked list.
#
# A node in a singly linked list should have two attributes: val and next. 
#
# val is the value of the current node, and next is a pointer/reference 
# to the next node.
#
# If you want to use the doubly linked list, you will need one more attribute prev 
# to indicate the previous node in the linked list. 
#
# Assume all nodes in the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
#   MyLinkedList() 
#       Initializes the MyLinkedList object.
#   int get(int index) 
#       Get the value of the indexth node in the linked list. 
#       If the index is invalid, return -1.
#   void addAtHead(int val) 
#       Add a node of value val before the first element of the linked list. 
#       After the insertion, the new node will be the first node of the linked list.
#   void addAtTail(int val) 
#       Append a node of value val as the last element of the linked list.
#   void addAtIndex(int index, int val) 
#       Add a node of value val before the indexth node in the linked list. 
#       If index equals the length of the linked list, the node will be appended 
#       to the end of the linked list. 
#       If index is greater than the length, the node will not be inserted.
#   void deleteAtIndex(int index) 
#       Delete the indexth node in the linked list, if the index is valid.
#
# Example 1:
#       Input: 
#           [
#               "MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", 
#               "deleteAtIndex", "get"
#           ],
#           [
#               [], [1], [3], [1, 2], [1], 
#               [1], [1]
#           ]
#       Output:
#           [
#               null, null, null, null, 2, 
#               null, 3
#           ]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/21",
    "design": 0,
    "coding": 0,
    "runtime": "575 ms",
    "fasterThan": "8%",
    "memory": "14.7 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findNumbers(self, nums: List[int]) -> int:
        return 0

#
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)        
#

class Node:
    def __init__(self):
        self.val = None 
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None 

    def __str__(self):
        s = ''
        node = self.head 
        while True:
            if node == None:
                break
            s += '%s, ' % node.val  
            node = node.next
        return s

    def dump(self):
        print(str(self))        

    def addAtHead(self, val: int) -> None:
        node = Node()
        node.val = val
        if self.head != None:
            node.next = self.head 

        self.head = node

    def addAtTail(self, val: int) -> None:
        tail = self.find_tail()
        if tail == None:
            self.addAtHead(val)
        else:
            node = Node()
            node.val = val 
            tail.next = node 

    def find_node(self, index):
        idx = 0
        node = self.head
        found_node = None  
        while True:
            if node == None:
                break 
            if idx == index:                
                found_node = node 
                break 
            node = node.next 
            idx += 1 

        return found_node

    def find_tail(self):
        n0 = self.head
        if n0 == None:
            return None 

        if n0.next == None:
            return n0

        while True:
            n1 = n0.next
            if n1 == None:
                return n0 
            n0 = n1

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= 1:
            pre_node = self.find_node(index-1)
            if pre_node == None:
                return

            node = Node()
            node.val = val 
            node.next = pre_node.next
            pre_node.next = node

        else:
            self.addAtHead(val)             

    def get(self, index: int) -> int:
        node = self.find_node(index)
        if node == None:
            return -1 
        else:
            return node.val

    def deleteAtIndex(self, index: int) -> None:
        if index >= 1:
            pre_node = self.find_node(index-1)
            if pre_node == None:
                return

            node = pre_node.next
            if node == None:
                return

            pre_node.next = node.next 

        else:
            self.head = self.head.next


