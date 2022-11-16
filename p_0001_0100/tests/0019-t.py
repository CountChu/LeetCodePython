from data_structure import *
import pdb
br = pdb.set_trace

def test(sln, ls, n, answer):
    print('ls = %s, n = %d, answer = %s' % (ls, n, answer))
    head = linked_list.list_to_ll(ls)
    out = sln.removeNthFromEnd(head, n)
    out_ls = linked_list.ll_to_list(out)
    print('out_ls = %s' % out_ls)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    test(sln, [1], 1, [])
    test(sln, [1, 2], 1, [1])
    test(sln, [1, 2], 2, [2])

