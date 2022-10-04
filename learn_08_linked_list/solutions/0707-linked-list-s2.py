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
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "608 ms",
    "fasterThan": "9%",
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
    def __init__(self, val):
        self.val = val
        self.next = None 

def get_tail(head):
    assert head != None
    nd = head 
    while True:
        out = nd
        nd = nd.next
        if nd == None:
            break
    return out

class MyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        nd = self.head
        s = ''
        while True:
            if nd == None:
                break 
            s += '%d, ' % nd.val
            nd = nd.next 
        return s

    def dump(self):
        print(str(self))        

    def get(self, index: int) -> int:
        i = 0
        nd0 = self.head 
        while True:
            if nd0 == None:
                return -1

            if i == index:
                return nd0.val
            nd0 = nd0.next 
            i += 1
        
    def addAtHead(self, val: int) -> None:
        nd = Node(val)

        if self.head == None:
            self.head = nd
        else:
            nd.next = self.head 
            self.head = nd

    def addAtTail(self, val: int) -> None:
        nd = Node(val)

        if self.head == None:
            self.head = nd 
            return

        tail = get_tail(self.head)
        tail.next = nd 

    '''
             v
        0 -> 1 -> 2
    '''
    def addAtIndex(self, index: int, val: int) -> None:
        nd = Node(val)

        if index == 0:
            if self.head == None:
                self.head = nd 
                return

            nd0 = self.head 
            self.head = nd
            nd.next = nd0
            return

        i = 0 
        nd0 = self.head 
        while True:
            if nd0 == None:
                return

            if i == index - 1:
                nd1 = nd0.next 
                nd0.next = nd
                nd.next = nd1 
                break

            nd0 = nd0.next
            i += 1

    '''
             v
        0 -> 1 -> 2
    '''
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            nd0 = self.head 
            nd1 = nd0.next 
            self.head = nd1
            return

        i = 0
        nd0 = self.head 
        while True:
            if nd0 == None:
                return

            if i == index - 1:
                nd1 = nd0.next 
                if nd1 == None:
                    return 

                nd2 = nd1.next 
                nd0.next = nd2
                break 

            nd0 = nd0.next
            i += 1











