
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, ls, target):
    print("s = %s, target = %s" % (ls, target))
    root = binary_tree_v3.ls_to_tree(ls)
    out = sln.zigzagLevelOrder(root)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]])
    test_solution(sln, [1], [[1]])
    test_solution(sln, [], [])



