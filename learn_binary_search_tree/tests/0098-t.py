from data_structure import *
import pdb

def test(sln, nums, answer):
    print('nums = %s, answer = %s' % (nums, answer))
    root = binary_tree_v3.ls_to_tree(nums)
    out = sln.isValidBST(root)
    assert out == answer, out

def run(sln):
    test(sln, [5, 2, 6, 1, 4, None, 7, None, None, 3], True)
    test(sln, [1, 1], False)
    test(sln, [2, 1, 3], True)
    test(sln, [5, 1, 4, None, None, 3, 6], False)
