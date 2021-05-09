from typing import List
import pdb

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# 2021/4/18: 25 mins, Runtime: 64 ms, Memory: 15.5 MB
#  

class Solution:
    def swapPairs(self, head):
    	debug = False

    	new_head = None
    	new_pre = None

    	n0 = head
    	while True:

    		if n0 == None:
    			break
    		new_n1 = ListNode(n0.val)
    		
    		n1 = n0.next
    		if n1 == None:
    			if new_head == None:
    				new_head = new_n1
    			if new_pre != None:
    				new_pre.next = new_n1
    			break
    		new_n0 = ListNode(n1.val)


    		if debug:
    			print(n0.val, n1.val)

    		n0 = n1.next

    		new_n0.next = new_n1

    		if new_head == None:
    			new_head = new_n0

    		if new_pre != None:
    			new_pre.next = new_n0

    		new_pre = new_n1

    	return new_head			
