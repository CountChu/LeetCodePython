
from data_structure import *
import pdb
br = pdb.set_trace

def build_ll(ls, pos):
    head = None
    tail = None
    head2 = None
    for i, val in enumerate(ls):
        node = linked_list.ListNode(val)
        if head == None:
            head = node
            tail = node
        else:
            tail.next = node 
            tail = node
        
        if pos != -1 and i == pos:
            head2 = tail

    if pos != -1:
        tail.next = head2

    return head

def test_solution(sln, head, pos, target):
    print("head = %s, pos = %d, target = %s" % (head, pos, target))

    head_node = build_ll(head, pos)
    

    out = sln.hasCycle(head_node)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [3, 2, 0, -4], 1, True)
    test_solution(sln, [1, 2], 0, True)
    test_solution(sln, [1], -1, False)
    test_solution(sln, [], -1, False)
