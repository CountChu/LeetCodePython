from typing import List
import pdb

#
# 2021/5/9: 2, 8
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_ll(ls):

	head = None
	pre = None
	for i in range(len(ls)):
		node = ListNode(ls[i])

		if head == None:
			head = node
		
		if pre != None:
			pre.next = node	
		pre = node
	
	return head

def ll_to_list(ll):
	ls = []

	node = ll
	while True:
		if node == None:
			break
		ls.append(node.val)
		node = node.next
	return ls

