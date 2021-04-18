from typing import List
import pdb

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 2021/4/18: 31 mins, Runtime: 32 ms, Memory: 14.2 MB
#

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        debug = False

        n1 = head
        idx = 0
        while True:
            if n1 == None:
                break
            if debug:
                print(idx, n1.val)
            
            n1 = n1.next
            if n1 == None:
                break

            idx += 1

        idx0 = idx - n
        if debug:
            print('idx0 = ', idx0)

        if idx0 == -1:
            head = head.next
            return head

        n0 = head
        idx = 0
        while True:
            if n0 == None:
                break

            if idx == idx0:
                n1 = n0.next
                if debug:
                    print('Remove %d' % n1.val)
                n0.next = n1.next
                break

            n0 = n0.next

            if n0 == None:
                break

            idx += 1            

        return head


    def list_to_ll(self, ls):       

        head = None
        n1 = None
        n0 = None
        for v in ls:
            n1 = ListNode(v)
            if head == None:
                head = n1
            if n0 != None:
                n0.next = n1
            n0 = n1
        return head

    def ll_to_list(self, head):
        ls = []
        n = head
        while True:
            if n == None:
                break
            ls.append(n.val)
            n = n.next

        return ls