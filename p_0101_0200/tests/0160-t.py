
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, intersectVal, listA, listB, skipA, skipB, target):
    print("intersectVal = %d, listA = %s, listB = %s, skipA = %d, skipB = %d, target = %s" % (intersectVal, listA, listB, skipA, skipB, target))
    head_a, head_b = build_links(intersectVal, listA, listB, skipA, skipB)
    nd = sln.getIntersectionNode(head_a, head_b)
    out = link_to_ls(nd)
    print("out = %s" % out)
    print('')

    assert out == target

def build_links(val, list_a, list_b, skip_a, skip_b):
    head_a = ls_to_link(list_a)
    head_b = ls_to_link(list_b)

    if val == 0:
        return head_a, head_b
    
    else:
        #dump(head_a)
        #dump(head_b)

        if skip_a == 0 and skip_b == 0:
            head_b = head_a
            return head_a, head_b

        nd_a = head_a
        for i in range(skip_a):
            nd_a = nd_a.next
        #print(nd_a.val)

        nd_b = head_b
        for i in range(skip_b - 1):
            nd_b = nd_b.next
        #print(nd_b.val)
        #br()

        nd_b.next = nd_a
        #dump(head_b)        

        return head_a, head_b

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None        

def ls_to_link(ls):
    head = None
    nd0 = None
    for v in ls:
        nd1 = ListNode(v)
        if head == None:
            head = nd1
            nd0 = nd1
        else:
            nd0.next = nd1
            nd0 = nd1
    return head

def link_to_ls(head):
    out = []
    nd = head 
    while nd != None:
        out.append(nd.val)
        nd = nd.next

    return out

def dump(head):
    s = ''
    nd = head
    while nd != None:
        s += '%d' % nd.val + ' -> '
        nd = nd.next 
    print(s)

def run(sln):
    test_solution(sln, 8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3, [8, 4, 5])
    test_solution(sln, 2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1, [2, 4])
    test_solution(sln, 0, [2, 6, 4], [1, 5], 3, 2, [])
    test_solution(sln, 1, [1], [1], 0, 0, [1])



