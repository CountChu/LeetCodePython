from typing import List
import pdb

solution_json = {
    "date": "2021/4/18",
    "coding": 12,
    "runtime": "52 ms",
    "memory": "15.8 MB"
}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 2021/4/18: 12 mins, Runtime: 52 ms, Memory: 15.8 MB
#

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = None
        pre = None

        n1 = l1
        n2 = l2
        while True:
            v = None
            if n1 == None and n2 == None:
                break
            elif n1 == None and n2 != None:
                v = n2.val
                n2 = n2.next
            elif n1 != None and n2 == None:
                v = n1.val
                n1 = n1.next
            else:
                v1 = n1.val
                v2 = n2.val
                if v1 < v2:
                    v = v1
                    n1 = n1.next
                else:
                    v = v2
                    n2 = n2.next
            #assert v != None        (it takes 20 ms)
            
            n3 = ListNode(v)
            if head == None:
                head = n3
            if pre != None:
                pre.next = n3
            pre = n3

        return head

    def list_to_ll(self, ls):

        head = None
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



