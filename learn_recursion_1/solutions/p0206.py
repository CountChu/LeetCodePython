from typing import List
import pdb

#
# 2021/5/9: 6, 13, 60 ms, 21.7 MB
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	ctx = {}
    	ctx['head'] = None
    	ctx['pre'] = None
    	reverse(head, ctx)
    	return ctx['head']

def reverse(node, ctx):
	d = False

	if node is None:
		return

	n0 = node
	n1 = node.next

	reverse(n1, ctx)

	v = n0.val
	if d:
		print(v)

	new_n = ListNode(v) 

	if ctx['pre'] != None:
		ctx['pre'].next = new_n
	ctx['pre'] = new_n

	if ctx['head'] == None:
		ctx['head'] = new_n	


