from typing import List
import pdb

solution_json = {
    "date": "2021/4/18",
    "coding": 34,
    "runtime": "44 ms",
    "memory": "15.6 MB"
}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        debug = False
        
        #
        # Find tail and count
        #

        n = head
        tail = None
        count = 0
        while True:
            if n == None:
                break
            tail = n
            n = n.next
            count += 1
        if tail == None:
            return None

        if debug:
            print('tail.val = %d, count = %d' % (tail.val, count))

        #
        # Connect tail and head to build a cicle.
        #

        tail.next = head

        #
        # Move forwared in steps.
        # count = 5, k = 2, step = 5*1 - 2 = 3
        # count = 3, k = 4, step = 3*2 - 4 = 2
        #
        # step = count * i - k >= 0
        # count * i >= k
        # i >= k / count
        #

        i = k // count
        if k % count != 0:
            i += 1
        step = count * i - k    

        if debug:
            print('step = %d' % step)

        new_pre = tail
        new_head = head
        for i in range(step):
            new_pre = new_pre.next
            new_head = new_head.next

        if debug:
            print('new_head.val = ', new_head.val)
        
        new_pre.next = None
        #pdb.set_trace()    
        return new_head


    def list_to_ll(self, ls):
        
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
        
    def ll_to_list(self, head):         
        ls = []
        n = head
        while True:
            if n == None:
                break
            ls.append(n.val)
            n = n.next
        return ls   
