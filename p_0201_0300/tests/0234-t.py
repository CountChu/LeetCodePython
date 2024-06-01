
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, ls, target):
    print("ls = %s, target = %s" % (ls, target))
    head = ls_to_ll(ls)

    out = sln.isPalindrome(head)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [1, 2, 2, 1], True)
    test_solution(sln, [1, 2], False)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

def ls_to_ll(ls):
    head = None
    nd0 = None
    for val in ls:
        nd1 = ListNode(val)
        if head == None:
            head = nd1
            nd0 = nd1
        else:
            nd0.next = nd1 
            nd0 = nd1

    return head

def dump(head):
    s = ''
    nd = head
    while True:
        if nd == None:
            break 

        nd += '%d ->' % nd.val 
        nd = nd.next

    print(s)

