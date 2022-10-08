from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, ls, target):
    print("ls = %s, target = %s" % (ls, target))
    root = binary_tree_v3.ls_to_tree(ls)
    out = sln.isBalanced(root)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [3, 9, 20, None, None, 15, 7], True)
    test_solution(sln, [1, 2, 2, 3, 3, None, None, 4, 4], False)
    test_solution(sln, [], True)
