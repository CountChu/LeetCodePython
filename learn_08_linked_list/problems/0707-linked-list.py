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
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
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

class MyLinkedList:
    def __init__(self):
        pass

    def __str__(self):
        return ''

    def dump(self):
        print(str(self))        

    def get(self, index: int) -> int:
        return 0
        

    def addAtHead(self, val: int) -> None:
        pass

    def addAtTail(self, val: int) -> None:
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        pass

    def deleteAtIndex(self, index: int) -> None:
        pass