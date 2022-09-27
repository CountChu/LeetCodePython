
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, ls, target):
    print("ls = %s, target = %s" % (ls, target))
    node = sln.ls_to_n_ary_tree(ls)
    out = sln.n_ary_tree_to_str(node)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    if False:
        test_solution(
            sln, 
            [
                1,
                None, 3, 2, 4,
                None, 5, 6
            ],        
            "1, (3, 2, 4), (5, 6)"
        )

    if True:
        test_solution(
            sln, 
            [
                1,
                None, 2, 3, 4, 5,
                None, None, 6, 7, None, 8, None, 9, 10,
                None, None, 11, None, 12, None, 13, None,
                None, 14
            ],        
            "1, (2, 3, 4, 5), (), (6, 7), (8), (9, 10), (), (11), (12), (13), (), (14)"
        )

