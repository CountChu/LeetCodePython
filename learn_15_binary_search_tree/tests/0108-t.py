
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, nums, target):
    print("nums = %s, target = %s" % (nums, target))
    root = sln.sortedArrayToBST(nums)
    out = binary_tree_v3.tree_to_ls(root)
    print("out = %s" % out)
    print('')

    assert out == target

def run(sln):
    test_solution(sln, [-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5])
    test_solution(sln, [1, 3], [3, 1])

