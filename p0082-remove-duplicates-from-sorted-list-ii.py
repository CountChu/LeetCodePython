from typing import List
import pdb

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 2021/4/18: 17 mins, Runtime: 44 ms, Memory: 15.8 MB
#

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        debug = False

        hash = {}

        n = head
        while True:
            if n == None:
                break
            
            if debug:
                print(n.val)
            
            if n.val not in hash:
                hash[n.val] = 0
            hash[n.val] += 1

            n = n.next

        if debug:
            print('hash = %s' % hash)

        new_head = None 
        new_pre = None
        n = head
        while True:
            if n == None:
                break

            if hash[n.val] == 1:
                new_n = ListNode(n.val)
                if new_head == None:
                    new_head = new_n
                if new_pre != None:
                    new_pre.next = new_n
                new_pre = new_n

            n = n.next

        #pdb.set_trace()
        return new_head





    def ls_to_ll(self, ls):
        head = None
        pre = None
        for v in ls:
            n = ListNode(v)
            if head == None:
                head = n
            if pre != None:
                pre.next = n
            pre = n
        return head

    def ll_to_ls(self, head):
        ls = []
        
        n = head
        while True:
            if n == None:
                break
            ls.append(n.val)
            n = n.next

        return ls

