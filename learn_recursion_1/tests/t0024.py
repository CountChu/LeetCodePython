from data_structure import *
import pdb

def test(sln, ls, answer):
    print('ls = %s, answer = %s' % (ls, answer))
    out = linked_list.list_to_ll(ls)
    ls2 = linked_list.ll_to_list(out)
    assert ls == ls2

    sln.swapPairs(out)
    
    out_ls = linked_list.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln, module):
    test(sln, [1, 2, 3, 4], [2, 1, 4, 3])
    test(sln, [], [])
    test(sln, [1], [1])
    test(sln, [1, 2, 3], [2, 1, 3])

'''
from typing import List
import pdb

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        debug = False    
'''        