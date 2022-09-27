
from data_structure import *
import pdb
br = pdb.set_trace

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def test_solution(sln, ls, target):
    print("ls = %s, target = %s" % (ls, target))
    root = n_ary_tree.ls_to_n_ary_tree(ls)
    out = sln.postorder(root)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    if True:
        test_solution(
            sln, 
            [1, None, 3, 2, 4, None, 5, 6], 
            [5, 6, 3, 2, 4, 1]
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
            [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
        )
