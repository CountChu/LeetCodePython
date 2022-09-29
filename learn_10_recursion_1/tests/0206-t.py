from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    head = linked_list.list_to_ll(nums)
    ls = linked_list.ll_to_list(head)
    assert ls == nums, ls

    out = sln.reverseList(head)
    out_ls = linked_list.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln, module):
    test(sln, [1,2,3,4,5], [5,4,3,2,1])
    test(sln, [1,2], [2,1])
    test(sln, [], [])

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    	pass
'''    	