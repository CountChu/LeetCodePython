from typing import List
import pdb

#
# 2021/5/9: 6, 4, 44 ms, 15.5 MB
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        swapPairs(head)
        return head

def swapPairs(node):
	if node is None:
		return

	if node.next is None:
		return

	n0 = node
	n1 = node.next
	n0.val, n1.val = n1.val, n0.val
	
	n2 = node.next.next
	swapPairs(n2)
