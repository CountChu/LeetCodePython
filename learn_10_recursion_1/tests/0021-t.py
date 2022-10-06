from data_structure import *
import pdb

def test(sln, ls1, ls2, answer):
    print('ls1 = %s, ls2 = %s, answer = %s' % (ls1, ls2, answer))

    head1 = linked_list.list_to_ll(ls1)
    head2 = linked_list.list_to_ll(ls2)
    
    out = sln.mergeTwoLists(head1, head2)
    out_ls = linked_list.ll_to_list(out)
    assert out_ls == answer, out_ls

def run(sln):
    test(sln, [1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    test(sln, [], [], [])
    test(sln, [], [0], [0])