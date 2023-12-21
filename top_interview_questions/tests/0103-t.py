
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
    if True:
        test_solution(sln, [3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]])

    if True:
        test_solution(
            sln, 
            [0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8],
            [[0], [4, 2], [1, 3, -1], [8, 6, 1, 5]])

    if True:
        test_solution(sln, [1], [[1]])

    if True:
        test_solution(sln, [], [])
    
    if True:
        test_solution(sln, [1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]])


